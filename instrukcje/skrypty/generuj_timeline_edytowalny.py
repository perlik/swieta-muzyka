"""
Generator W PEŁNI EDYTOWALNEJ osi czasu z obrazków (Etap 5 → montaż) dla
darmowej wersji DaVinci Resolve, z ruchem kadru typu Ken Burns.

Generuje `timeline_edytowalny_fcp7.xml`: legacy Final Cut Pro 7 XML (XMEML v5),
gdzie każdy still ma zadeklarowany masterclip dłuższy niż użyty fragment (zapas
`--handle` z każdej strony), więc trim/przejścia mają z czego brać. Naiwne
FCPXML z `<asset-clip>` importuje się poprawnie, ale klipy wychodzą ZABLOKOWANE
— obrazek statyczny nie ma tam żadnego zapasu.

Rozdzielczość sekwencji ustawiamy sztywno (`--width`/`--height`, domyślnie
2560x1440 — patrz styl-teledysku.md), a NIE odczytujemy z rzeczywistych wymiarów
plików w images/ — te bywają większe (np. 2944x1656) i podstawienie ich wprost
dawałoby złą rozdzielczość sekwencji przy imporcie do Resolve.

RUCH KADRU (Ken Burns) — metoda przeniesiona z projektu „Holy Creator"
(`docs/timeline-davinci-fcp7-xml.md`), sprawdzona tam na kilkudziesięciu filmach:

XML nie umie przenieść **Dynamic Zoom** — to funkcja wyłącznie Resolve'a, nie ma
jej ani w FCP7 XMEML, ani w FCPXML, więc importer nigdy nie zapali przełącznika DZ
ani nie ustawi zielonej/czerwonej ramki. Da się natomiast przenieść ten sam ruch
jako klatki kluczowe filtra „Basic Motion" — Resolve wczytuje je jako
**Transform → Zoom / Position** z keyframe'ami i na ekranie wychodzi to samo.
Montażysta poprawia ruch w sekcji Transform, przesuwając klatki kluczowe.

`--zoom` (domyślnie 25%) dokłada każdemu kadrowi najazd albo odjazd: 100% → 125%,
kierunek zmienia się co kadr (żeby sekwencja nie pulsowała w jednym rytmie),
a wygładzenie jest **wypieczone w klatki** — zamiast liczyć na to, że importer
uszanuje flagi interpolacji, krzywa `smoothstep` jest próbkowana do
`--zoom-klatek` klatek kluczowych. Efekt „Ease In and Out" przeżywa więc import
niezależnie od wersji Resolve'a.

**Zoom skaluje się długością kadru** (`--zoom-ref`, domyślnie 12 s): stała wartość
dla każdego kadru daje ruch o TEMPIE odwrotnie proporcjonalnym do jego długości,
więc te same 25%, które na kadrze 12-sekundowym płyną spokojnie, na 4-sekundowym
szarpią. Zoom liczony jest jako `zoom × długość / ref`, przycięty z góry do
`--zoom`, z dołu do `--zoom-min`. `--zoom-ref 0` wraca do stałej wartości.

`--pan` (domyślnie 6% szerokości kadru) dokłada ruch w bok: kadr jedzie w stronę,
po której siedzi główny motyw. Stronę bierzemy z pliku `kierunki-ruchu.tsv`
leżącego obok obrazków (`nazwa-pliku<TAB>lewo|prawo|auto`, `auto` = strony na
przemian); gdy pliku nie ma, wszystkie kadry idą „auto". Automatycznego wykrywania
strony nie ma i nie będzie — na akwareli detal tła (rozświetlone niebo, aureola,
brama światła przy krawędzi) bywa mocniejszy niż motyw główny, więc środek
ciężkości kontrastu myli się o jakieś 40% kadrów.

**Pan jest sprzężony z zoomem, nie niezależny** — przesunięcie w każdej klatce jest
stałym ułamkiem zapasu, jaki daje aktualne powiększenie. Dzięki temu w klatce
startowej najazdu (skala 100%) przesunięcie wynosi dokładnie 0 i **czarny pas przy
krawędzi nie może się pojawić w żadnym momencie ruchu**.

`--zoom 0` wyłącza ruch i wraca do gołej osi czasu, `--pan 0` zostawia sam zoom.

Uwaga: w tym projekcie WSZYSTKIE kadry są ilustracjami, więc ruch dostaje każdy
z nich. (W „Holy Creator" generator pomija karty tekstowe — tutaj nie ma czego
pomijać, bo napisy wchodzą jako napisy SRT z Etapu 2, nie jako kadry.)

Użycie:
    python3 generuj_timeline_edytowalny.py <katalog images/> \\
        [--out <plik.xml>] [--fps 60] [--name "..."] [--handle 10] \\
        [--zoom 25] [--zoom-ref 12] [--zoom-min 6] [--pan 6] \\
        [--kierunki <plik.tsv>] [--zoom-klatek 25] [--width 2560] [--height 1440]

Domyślnie zapisuje do `render/timeline_edytowalny_fcp7.xml` w folderze utworu —
skrypt szuka istniejącego katalogu `render/` w katalogach nadrzędnych względem
podanego `images/`, więc działa też, gdy kadry leżą w podfolderze (`images/v2/`).

W DaVinci Resolve: File -> Import -> Timeline... -> wskaż wygenerowany plik.
Jeśli klipy byłyby zablokowane: zaimportuj najpierw same JPG-i przez
File -> Import Media do Media Pool, potem importuj XML z ODZNACZONĄ opcją
„Automatically import source clips into media pool".

Po imporcie sprawdź na paru kadrach: czy Transform ma keyframe'y, czy w skrajnym
punkcie ruchu nie wchodzi czarny pas przy krawędzi, czy panorama nie jest dwa razy
mocniejsza niż zamawiana (patrz uwaga o jednostkach `center` w `filtr_ruchu`).
"""

import argparse
import os
import re
import sys
import unicodedata
from urllib.parse import quote

DEFAULT_FPS = 60
DEFAULT_WIDTH = 2560           # docelowa rozdzielczość projektu, patrz styl-teledysku.md
DEFAULT_HEIGHT = 1440
DEFAULT_HANDLE_SEC = 10        # zapas na trim/przejścia z każdej strony
DEFAULT_ZOOM_PROC = 25.0       # 100% -> 125%
DEFAULT_ZOOM_REF_SEC = 12.0    # przy tej długości kadru `--zoom` wchodzi w całości
DEFAULT_ZOOM_MIN_PROC = 6.0    # dolna granica najazdu dla krótkich kadrów
DEFAULT_PAN_PROC = 6.0         # przesunięcie w bok na końcu ruchu, w % szerokości kadru
DEFAULT_ZOOM_KLATEK = 25       # ile klatek kluczowych próbkuje krzywą wygładzenia
DEFAULT_PRZEJSCIE_SEC = 2.5    # Cross Dissolve na każdym cięciu (decyzja użytkownika 2026-08-01)
DEFAULT_NAZWA = "Auto Timeline"
PLIK_KIERUNKOW = "kierunki-ruchu.tsv"
PLIK_WYJSCIOWY = "timeline_edytowalny_fcp7.xml"
WZORZEC = re.compile(r"(\d+)m(\d+)s-(\d+)m(\d+)s")
ROZSZERZENIA = (".png", ".jpg", ".jpeg", ".tif", ".tiff")


def klatki(minuty, sekundy, fps):
    return int(round((int(minuty) * 60 + int(sekundy)) * fps))


def url_pliku(sciezka):
    """`file://localhost/...` z procentowaniem — ścieżki projektu mają spacje i polskie znaki.

    Ścieżkę normalizujemy do **NFC** przed procentowaniem. macOS zwraca nazwy plików
    w NFD (rozłożonej: `Ś` jako `S` + U+0301, `ę` jako `e` + U+0328), więc bez tego
    kroku w XML ląduje `_S%CC%81wie%CC%A8ta%20Muzyka` zamiast `_%C5%9Awi%C4%99ta%20Muzyka`.
    Python otwiera oba warianty i walidacja „czy plik istnieje" przechodzi, ale importer
    DaVinci Resolve dopasowuje ścieżkę dosłownie i **wszystkie klipy wchodzą jako
    Media Offline** — przy jednoczesnym poprawnym wczytaniu tych samych plików przez
    File → Import Media (bo tam ścieżka nie idzie przez nasz XML). Objaw: w Media Pool
    każdy kadr widnieje dwa razy, raz z podglądem i raz na czerwono. Wyłapane przy
    Psalmie 121 (2026-08-01).
    """
    return "file://localhost" + quote(unicodedata.normalize("NFC", sciezka), safe="/")


def domyslne_wyjscie(katalog):
    """`render/timeline_edytowalny_fcp7.xml` w folderze utworu.

    Kadry leżą zwykle w `images/`, ale bywają w podfolderze (`images/v2/` przy
    drugiej wersji utworu), dlatego szukamy istniejącego `render/` w katalogach
    nadrzędnych, zamiast zakładać sztywno „o jeden poziom wyżej".
    """
    biezacy = katalog
    for _ in range(3):
        rodzic = os.path.dirname(biezacy)
        kandydat = os.path.join(rodzic, "render")
        if os.path.isdir(kandydat):
            return os.path.join(kandydat, PLIK_WYJSCIOWY)
        biezacy = rodzic
    return os.path.join(os.path.dirname(katalog), "render", PLIK_WYJSCIOWY)


def zbierz_kadry(katalog, fps):
    kadry = []
    for nazwa in sorted(os.listdir(katalog)):
        if nazwa.startswith(".") or not nazwa.lower().endswith(ROZSZERZENIA):
            continue                      # pomija m.in. AppleDouble `._nazwa.jpg` na exFAT
        m = WZORZEC.search(nazwa)
        if not m:
            print(f"  pomijam (brak znacznika czasu w nazwie): {nazwa}", file=sys.stderr)
            continue
        start = klatki(m.group(1), m.group(2), fps)
        koniec = klatki(m.group(3), m.group(4), fps)
        if koniec <= start:
            print(f"  pomijam (koniec nie po początku): {nazwa}", file=sys.stderr)
            continue
        kadry.append((start, koniec, nazwa))
    kadry.sort()                          # sortowanie po klatkach, nie po nazwie
    return kadry


def sprawdz_ciaglosc(kadry, fps):
    """Kadry powinny kafelkować oś bez dziur i bez zakładek."""
    dziury, zakladki = [], []
    for (s1, k1, n1), (s2, _, n2) in zip(kadry, kadry[1:]):
        if s2 > k1:
            dziury.append((k1 / fps, s2 / fps, n1, n2))
        elif s2 < k1:
            zakladki.append((s2 / fps, k1 / fps, n1, n2))
    return dziury, zakladki


def wczytaj_kierunki(katalog, sciezka=None):
    """Strona, w którą ma jechać kadr, z pliku `kierunki-ruchu.tsv` obok obrazków.

    Format: `nazwa-pliku<TAB>lewo|prawo|auto`, `#` zaczyna komentarz. „lewo"/„prawo"
    mówi, po której stronie kadru siedzi główny motyw — tam pojedzie kadr. „auto"
    (i każdy plik bez wpisu) dostaje strony na przemian.

    Pliku nie da się wygenerować automatycznie — stronę wpisuje się z obejrzenia
    kadrów. Po każdej zmianie audio (nazwy plików niosą czas) trzeba go zaktualizować;
    generator wypisuje ostrzeżenie o wpisach wskazujących nieistniejące kadry.
    """
    plik = sciezka or os.path.join(katalog, PLIK_KIERUNKOW)
    if not os.path.exists(plik):
        return {}, None
    kierunki = {}
    with open(plik, encoding="utf-8") as fh:
        for nr, linia in enumerate(fh, 1):
            linia = linia.split("#")[0].strip()
            if not linia:
                continue
            czesci = [c.strip() for c in linia.split("\t") if c.strip()]
            if len(czesci) != 2 or czesci[1].lower() not in ("lewo", "prawo", "auto"):
                sys.exit(f"{plik}:{nr}: oczekiwano „nazwa<TAB>lewo|prawo|auto\", jest: {linia}")
            kierunki[czesci[0]] = czesci[1].lower()
    return kierunki, plik


def zoom_dla_dlugosci(dlugosc_s, zoom_proc, ref_sec, zoom_min_proc):
    """Ile procent najazdu dostaje kadr o danej długości.

    Stała wartość zoomu dla każdego kadru daje ruch o TEMPIE odwrotnie
    proporcjonalnym do długości ujęcia: 25% rozłożone na 12 s to 2.1%/s i wygląda
    spokojnie, ale te same 25% na kadrze 4-sekundowym to 6.3%/s — widz odbiera to
    jako szarpnięcie. Dlatego zoom skalujemy długością: `zoom = zoom_max * dlugosc / ref`.

    Dwa ograniczenia:
      * góra — `zoom_proc`, żeby długie ujęcia nie urosły do absurdalnego
        powiększenia (kadr 40 s dostałby 83%, czyli kadrowanie w połowie obrazu),
      * dół — `zoom_min_proc`, żeby najkrótsze kadry nie stanęły w miejscu; poniżej
        ok. 6% ruch przestaje być widoczny.

    `ref_sec=0` wyłącza skalowanie i wraca do stałego `zoom_proc` na każdym kadrze.
    """
    if not ref_sec:
        return zoom_proc
    return max(min(zoom_proc * dlugosc_s / ref_sec, zoom_proc), min(zoom_min_proc, zoom_proc))


def filtr_ruchu(dlugosc, handle, zoom_proc, pan_proc, klatek, do_srodka, znak_pan):
    """Klatki kluczowe „Basic Motion" (Scale + Center) odtwarzające ruch Dynamic Zoom.

    `do_srodka=True` to najazd (100% → 100+zoom), False to odjazd. Wygładzenie jest
    wypieczone: wartości idą po `smoothstep` (3t² - 2t³), więc ruch zwalnia na obu
    końcach nawet wtedy, gdy importer zignoruje flagi interpolacji.

    `znak_pan` to strona, w którą jedzie kadr: +1 gdy główny motyw siedzi po LEWEJ,
    -1 gdy po prawej, 0 gdy pan wyłączony. Znak jest odwrotny do intuicji, bo `center`
    przesuwa OBRAZ, a nie okno kadru: żeby okno pojechało w lewo (na motyw z lewej),
    obraz musi iść w prawo, czyli `horiz` rośnie dodatnio.

    Przesunięcie liczymy jako ułamek zapasu, jaki daje bieżące powiększenie, więc
    postęp panoramy jest ten sam co postęp zoomu (`u` niżej): przy skali 100% wynosi
    zero i czarny pas nie ma jak wejść w kadr. `pan_proc` jest podane w procentach
    SZEROKOŚCI kadru i dotyczy skrajnego punktu ruchu.

    Jednostki `center` w FCP7: 1.0 = połowa szerokości kadru, stąd `× 2`. Nawet gdyby
    dana wersja importera czytała to jako pełną szerokość, ruch zmieści się w zapasie —
    pilnuje tego limit `pan ≤ zoom/4` w `main()`.

    `when` liczymy w czasie MEDIÓW (od `in` do `out`), bo klip ma uchwyty, a parametry
    filtrów w FCP7 są kluczowane względem materiału, nie względem osi czasu.
    """
    kf_skala, kf_center = [], []
    for i in range(klatek):
        t_norm = i / (klatek - 1)
        wygl = t_norm * t_norm * (3 - 2 * t_norm)          # smoothstep
        u = wygl if do_srodka else 1.0 - wygl              # postęp powiększenia 0..1
        when = handle + round(t_norm * dlugosc)
        kf_skala.append((when, 100.0 + zoom_proc * u))
        kf_center.append((when, znak_pan * (pan_proc / 100.0) * u * 2))

    def wpisy(kf, formatuj):
        return "\n".join(
            f"                                        <keyframe>\n"
            f"                                            <when>{w}</when>\n"
            f"{formatuj(v)}\n"
            f"                                        </keyframe>" for w, v in kf)

    skala = wpisy(kf_skala, lambda v: f"                                            <value>{v:.3f}</value>")
    center = wpisy(kf_center, lambda v: (
        "                                            <value>\n"
        f"                                                <horiz>{v:.6f}</horiz>\n"
        "                                                <vert>0</vert>\n"
        "                                            </value>"))
    parametr_center = f"""
                                    <parameter>
                                        <parameterid>center</parameterid>
                                        <name>Center</name>
                                        <value>
                                            <horiz>{kf_center[0][1]:.6f}</horiz>
                                            <vert>0</vert>
                                        </value>
{center}
                                    </parameter>""" if znak_pan and pan_proc else ""

    return f"""                            <filter>
                                <effect>
                                    <name>Basic Motion</name>
                                    <effectid>basic</effectid>
                                    <effectcategory>motion</effectcategory>
                                    <effecttype>motion</effecttype>
                                    <mediatype>video</mediatype>
                                    <parameter>
                                        <parameterid>scale</parameterid>
                                        <name>Scale</name>
                                        <valuemin>0</valuemin>
                                        <valuemax>1000</valuemax>
                                        <value>{kf_skala[0][1]:.3f}</value>
{skala}
                                    </parameter>{parametr_center}
                                </effect>
                            </filter>"""


def przejscie_xml(start, end, rate):
    """Cross Dissolve na cięciu, jako `<transitionitem>` (FCP7 XMEML).

    `alignment=center` znaczy, że przejście straddluje cięcie: pierwsza połowa bierze
    materiał z zapasu klipu wychodzącego, druga z zapasu wchodzącego. Dlatego długość
    osi czasu się NIE zmienia — przejście nie wydłuża sekwencji, tylko nakłada kadry
    na siebie w okolicy cięcia. Zapas (`--handle`, domyślnie 10 s) musi być większy
    niż połowa przejścia, co przy 2,5 s jest spełnione z dużym marginesem.

    `<start>`/`<end>` liczymy w klatkach OSI CZASU (inaczej niż `when` w klatkach
    kluczowych filtra ruchu, które idą w czasie mediów).
    """
    return f"""                        <transitionitem>
                            <start>{start}</start>
                            <end>{end}</end>
                            <alignment>center</alignment>
                            {rate}
                            <effect>
                                <name>Cross Dissolve</name>
                                <effectid>Cross Dissolve</effectid>
                                <effecttype>transition</effecttype>
                                <mediatype>video</mediatype>
                                <wipecode>0</wipecode>
                                <wipeaccuracy>100</wipeaccuracy>
                                <startratio>0</startratio>
                                <endratio>1</endratio>
                                <reverse>FALSE</reverse>
                            </effect>
                        </transitionitem>"""


def zbuduj_xmeml(kadry, katalog, fps, width, height, handle_sec, nazwa_projektu,
                 zoom_proc=DEFAULT_ZOOM_PROC, zoom_klatek=DEFAULT_ZOOM_KLATEK,
                 pan_proc=DEFAULT_PAN_PROC, kierunki=None,
                 zoom_ref_sec=DEFAULT_ZOOM_REF_SEC, zoom_min_proc=DEFAULT_ZOOM_MIN_PROC,
                 uzyte_zoomy=None, przejscie_sec=0.0):
    handle = handle_sec * fps
    total = kadry[-1][1] if kadry else 0
    kierunki = kierunki or {}
    ZNAK = {"lewo": 1, "prawo": -1}      # patrz `filtr_ruchu`: obraz jedzie odwrotnie do okna

    rate = ("<rate>\n"
            f"                                <timebase>{fps}</timebase>\n"
            "                                <ntsc>FALSE</ntsc>\n"
            "                            </rate>")

    elementy = []
    for i, (start, koniec, nazwa) in enumerate(kadry, 1):
        dlugosc = koniec - start
        master = dlugosc + 2 * handle
        pathurl = url_pliku(os.path.join(katalog, nazwa))
        # najazd/odjazd zmienia się co kadr — inaczej cała sekwencja „oddycha" w jednym
        # rytmie; strona panoramy idzie z pliku kierunków, „auto" dostaje na przemian
        strona = kierunki.get(nazwa, "auto")
        znak = ZNAK.get(strona, 1 if i % 2 else -1) if pan_proc else 0
        # zoom (a z nim pan) skalowany długością kadru — patrz `zoom_dla_dlugosci`.
        # Pan idzie w tej samej proporcji, więc stosunek pan/zoom zostaje stały i limit
        # bezpieczeństwa `pan <= zoom/4` sprawdzony w `main()` obowiązuje na każdym kadrze.
        zoom_kadru = zoom_dla_dlugosci(dlugosc / fps, zoom_proc, zoom_ref_sec, zoom_min_proc)
        pan_kadru = pan_proc * (zoom_kadru / zoom_proc) if zoom_proc else 0.0
        if zoom_proc and uzyte_zoomy is not None:
            uzyte_zoomy.append((nazwa, dlugosc / fps, zoom_kadru))
        ruch = (filtr_ruchu(dlugosc, handle, zoom_kadru, pan_kadru, zoom_klatek,
                            do_srodka=bool(i % 2), znak_pan=znak)
                if zoom_proc else "")
        elementy.append(f"""                        <clipitem id="clipitem-{i}">
                            <name>{nazwa}</name>
                            <enabled>TRUE</enabled>
                            <duration>{master}</duration>
                            {rate}
                            <start>{start}</start>
                            <end>{koniec}</end>
                            <in>{handle}</in>
                            <out>{handle + dlugosc}</out>
                            <file id="file-{i}">
                                <name>{nazwa}</name>
                                <pathurl>{pathurl}</pathurl>
                                <duration>{master}</duration>
                                {rate}
                                <media>
                                    <video>
                                        <samplecharacteristics>
                                            <width>{width}</width>
                                            <height>{height}</height>
                                        </samplecharacteristics>
                                    </video>
                                </media>
                            </file>
{ruch}
                        </clipitem>""")
        # Cross Dissolve na każdym cięciu poza ostatnim kadrem — element musi stać
        # w torze między klipami, w kolejności czasowej.
        if przejscie_sec and i < len(kadry):
            dl = int(round(przejscie_sec * fps))
            polowa = dl // 2
            elementy.append(przejscie_xml(koniec - polowa, koniec + (dl - polowa), rate))

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xmeml>
<xmeml version="5">
    <sequence id="sequence-1">
        <name>{nazwa_projektu}</name>
        <duration>{total}</duration>
        {rate}
        <media>
            <video>
                <format>
                    <samplecharacteristics>
                        <width>{width}</width>
                        <height>{height}</height>
                        {rate}
                    </samplecharacteristics>
                </format>
                <track>
{chr(10).join(elementy)}
                    <enabled>TRUE</enabled>
                    <locked>FALSE</locked>
                </track>
            </video>
        </media>
    </sequence>
</xmeml>
"""


def main():
    ap = argparse.ArgumentParser(
        description="Edytowalna oś czasu FCP7 XML do DaVinci Resolve, z ruchem kadru "
                    "(Ken Burns), z kadrów nazwanych zakresem czasu po Etapie 5.")
    ap.add_argument("images", help="katalog z kadrami (nazwy 0m00s-0m16s.jpg)")
    ap.add_argument("--out", help=f"plik wynikowy (domyślnie render/{PLIK_WYJSCIOWY} "
                                  f"w folderze utworu)")
    ap.add_argument("--fps", type=int, default=DEFAULT_FPS,
                    help=f"klatkaż osi czasu — musi zgadzać się z projektem w Resolve "
                         f"(domyślnie {DEFAULT_FPS})")
    ap.add_argument("--name", default=DEFAULT_NAZWA, help="nazwa sekwencji widoczna w Resolve")
    ap.add_argument("--handle", type=int, default=DEFAULT_HANDLE_SEC,
                    help=f"zapas na trim/przejścia z każdej strony, w sekundach "
                         f"(domyślnie {DEFAULT_HANDLE_SEC})")
    ap.add_argument("--zoom", type=float, default=DEFAULT_ZOOM_PROC,
                    help=f"najazd w procentach (100%% -> 100+X), 0 wyłącza ruch; "
                         f"domyślnie {DEFAULT_ZOOM_PROC:.0f}")
    ap.add_argument("--zoom-ref", type=float, default=DEFAULT_ZOOM_REF_SEC,
                    help=f"długość kadru (s), przy której --zoom wchodzi w całości; krótsze "
                         f"kadry dostają proporcjonalnie mniej, 0 wyłącza skalowanie "
                         f"(domyślnie {DEFAULT_ZOOM_REF_SEC:.0f})")
    ap.add_argument("--zoom-min", type=float, default=DEFAULT_ZOOM_MIN_PROC,
                    help=f"dolna granica najazdu przy skalowaniu długością "
                         f"(domyślnie {DEFAULT_ZOOM_MIN_PROC:.0f})")
    ap.add_argument("--pan", type=float, default=DEFAULT_PAN_PROC,
                    help=f"ruch w bok na końcu najazdu, w %% szerokości kadru; 0 wyłącza "
                         f"(domyślnie {DEFAULT_PAN_PROC:.0f}, maks. bezpiecznie zoom/4)")
    ap.add_argument("--przejscia", type=float, default=DEFAULT_PRZEJSCIE_SEC,
                    help=f"Cross Dissolve na każdym cięciu, w sekundach; 0 wyłącza "
                         f"(domyślnie {DEFAULT_PRZEJSCIE_SEC})")
    ap.add_argument("--kierunki", help=f"plik ze stronami ruchu "
                                       f"(domyślnie <images>/{PLIK_KIERUNKOW}, jeśli istnieje)")
    ap.add_argument("--zoom-klatek", type=int, default=DEFAULT_ZOOM_KLATEK,
                    help=f"ile klatek kluczowych próbkuje wygładzenie "
                         f"(domyślnie {DEFAULT_ZOOM_KLATEK})")
    ap.add_argument("--width", type=int, default=DEFAULT_WIDTH)
    ap.add_argument("--height", type=int, default=DEFAULT_HEIGHT)
    args = ap.parse_args()

    katalog = os.path.abspath(args.images)
    if not os.path.isdir(katalog):
        sys.exit(f"Nie ma takiego katalogu: {katalog}")

    wyjscie = os.path.abspath(args.out) if args.out else domyslne_wyjscie(katalog)

    kadry = zbierz_kadry(katalog, args.fps)
    if not kadry:
        sys.exit("Nie znaleziono plików pasujących do wzorca (np. 0m17s-0m32s.jpg).")

    # Kontrola, że ścieżka w formie zapisywanej do XML (NFC) faktycznie się otwiera.
    # Gdyby wolumin akceptował tylko NFD, Resolve pokazałby Media Offline — patrz `url_pliku`.
    for _, _, nazwa in kadry:
        nfc = unicodedata.normalize("NFC", os.path.join(katalog, nazwa))
        if not os.path.exists(nfc):
            sys.exit(f"Ścieżka w formie NFC nie otwiera się: {nfc}\n"
                     f"Resolve pokazałby ten klip jako Media Offline. Sprawdź nazwę pliku "
                     f"albo przenieś kadry do katalogu bez znaków spoza ASCII.")

    dziury, zakladki = sprawdz_ciaglosc(kadry, args.fps)
    for od, do, n1, n2 in dziury:
        print(f"  DZIURA {od:.0f}-{do:.0f} s między {n1} a {n2}", file=sys.stderr)
    for od, do, n1, n2 in zakladki:
        print(f"  ZAKŁADKA {od:.0f}-{do:.0f} s między {n1} a {n2}", file=sys.stderr)

    if not args.zoom:
        # `--zoom 0` to świadome wyłączenie ruchu kadru — pan bez zoomu nie ma zapasu,
        # w którym mógłby się ruszać, więc gasimy go razem z zoomem (a nie przerywamy
        # na kontroli limitu niżej, bo każdy pan > 0 przekracza wtedy zoom/2).
        args.pan = 0.0
    if args.pan > args.zoom / 2:
        sys.exit(f"--pan {args.pan}% nie zmieści się w zapasie, jaki daje --zoom {args.zoom}% "
                 f"(maks. {args.zoom / 2:.1f}%) — w kadrze pokaże się czarny pas")
    if args.pan > args.zoom / 4:
        print(f"UWAGA: --pan {args.pan}% przekracza bezpieczne {args.zoom / 4:.1f}% "
              f"(zoom/4). Zmieści się tylko wtedy, gdy importer czyta „center\" tak jak FCP7 "
              f"(1.0 = pół szerokości kadru) — sprawdź krawędzie na osi czasu.", file=sys.stderr)

    kierunki, plik_kier = wczytaj_kierunki(katalog, args.kierunki)
    if args.zoom and args.pan:
        strony = [kierunki.get(n, "auto") for _, _, n in kadry]
        if plik_kier:
            print(f"pan: {strony.count('lewo')} w lewo, {strony.count('prawo')} w prawo, "
                  f"{strony.count('auto')} na przemian (wg {os.path.basename(plik_kier)})")
        else:
            print(f"pan: brak {PLIK_KIERUNKOW} obok kadrów — wszystkie {len(kadry)} "
                  f"kadry dostaną strony na przemian")
        for n in sorted(set(kierunki) - {n for _, _, n in kadry}):
            print(f"  UWAGA: {os.path.basename(plik_kier)} opisuje nieistniejący kadr {n} "
                  f"(zmieniły się nazwy po przeliczeniu audio?)", file=sys.stderr)

    if args.przejscia:
        polowa = args.przejscia / 2
        if polowa > args.handle:
            sys.exit(f"--przejscia {args.przejscia} s wymaga zapasu ≥ {polowa:.2f} s z każdej "
                     f"strony, a --handle to {args.handle} s")
        # Przejście wyrównane na cięciu zjada połowę swojej długości z każdego z sąsiadów,
        # więc kadr krótszy niż całe przejście zostałby przykryty z obu stron naraz.
        krotkie = [(n, (k - s) / args.fps) for s, k, n in kadry if (k - s) / args.fps < args.przejscia]
        if krotkie:
            sys.exit("Kadry krótsze niż długość przejścia — przejścia zjadłyby je w całości:\n" +
                     "\n".join(f"  {n}: {d:.1f} s < {args.przejscia} s" for n, d in krotkie))
        print(f"przejścia: Cross Dissolve {args.przejscia} s na {len(kadry) - 1} cięciach "
              f"(wyrównane na cięciu, po {polowa:.2f} s z zapasu każdego sąsiada)")

    uzyte = []
    tresc = zbuduj_xmeml(kadry, katalog, args.fps, args.width, args.height,
                         args.handle, args.name, args.zoom, args.zoom_klatek,
                         args.pan, kierunki, args.zoom_ref, args.zoom_min, uzyte,
                         args.przejscia)
    os.makedirs(os.path.dirname(wyjscie), exist_ok=True)
    with open(wyjscie, "w", encoding="utf-8") as fh:
        fh.write(tresc)

    if uzyte and args.zoom_ref:
        z = sorted(x[2] for x in uzyte)
        przy_gornej = sum(1 for v in z if v >= args.zoom - 1e-9)
        przy_dolnej = sum(1 for v in z if v <= min(args.zoom_min, args.zoom) + 1e-9)
        tempo = sorted(x[2] / x[1] for x in uzyte if x[1])
        print(f"zoom skalowany długością kadru (odniesienie {args.zoom_ref:.0f} s): "
              f"{z[0]:.1f}-{z[-1]:.1f}%, mediana {z[len(z) // 2]:.1f}%; "
              f"{przy_gornej} kadrów przy suficie {args.zoom:.0f}%, "
              f"{przy_dolnej} przy podłodze {min(args.zoom_min, args.zoom):.0f}%")
        print(f"tempo ruchu: {tempo[0]:.2f}-{tempo[-1]:.2f} %/s "
              f"(mediana {tempo[len(tempo) // 2]:.2f}, odniesienie "
              f"{args.zoom / args.zoom_ref:.2f})")

    koniec = kadry[-1][1] / args.fps
    zoom_opis = ("bez ruchu kadru" if not args.zoom else
                 (f"zoom 100->{100 + args.zoom:.0f}% (skalowany długością)" if args.zoom_ref
                  else f"zoom 100->{100 + args.zoom:.0f}%"))
    print(f"{len(kadry)} kadrów, {int(koniec // 60)} min {koniec % 60:.0f} s, "
          f"{args.width}x{args.height} @ {args.fps} fps, zapas {args.handle} s, "
          f"{zoom_opis}, pan {args.pan:.0f}% szerokości, "
          f"{f'przejścia {args.przejscia} s' if args.przejscia else 'bez przejść'}")
    print(f"-> {wyjscie}")
    print("\nW Resolve: File -> Import -> Timeline... -> wskaż ten plik.")


if __name__ == "__main__":
    main()
