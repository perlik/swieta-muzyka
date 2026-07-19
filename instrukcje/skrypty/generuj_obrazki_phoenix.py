"""
Generator kadrów przez Leonardo AI / Phoenix 1.0, tryb Ultra (Etap 2/3) — wywoływane
bezpośrednio z Claude Code przez REST API, bez wchodzenia w przeglądarkę Leonardo.

Wymaga klucza API Leonardo w zmiennej środowiskowej LEONARDO_API_KEY
(Leonardo → Settings → API Access; konto API rozliczane osobno od planu Essential,
PAYG — patrz rozmowa o kosztach). Klucza NIE wpisywać nigdzie w repo.

Użycie:
    export LEONARDO_API_KEY="..."
    python3 generuj_obrazki_phoenix.py "<opis sceny>" <folder_wyjsciowy> [prefiks_nazwy] [liczba_obrazow] [width] [height] [contrast]
    python3 generuj_obrazki_phoenix.py --raw "<pełny, gotowy prompt>" <folder_wyjsciowy> [prefiks_nazwy] [liczba_obrazow] [width] [height] [contrast]
    python3 generuj_obrazki_phoenix.py --standard "<opis lub --raw prompt>" <folder_wyjsciowy> ...  (jak wyżej, ale bez trybu Ultra — taniej, niższa rozdzielczość)
    python3 generuj_obrazki_phoenix.py --upscale <generatedImageId> <plik_wyjsciowy.jpg> [multiplier]
    # multiplier akceptuje ułamki, np. 1.34 to minimalne powiększenie z 1920x1080 (Full HD, --standard) do min. 2K (2560x1440)

Domyślnie: liczba_obrazow=1, width=1920, height=1080 (16:9), tryb Ultra włączony.
API Leonardo odrzuca generacje szersze niż 1920 px ("width must be between 32 and
1920") — nie da się zażądać bazowo od razu 2560×1440. W trybie Ultra nie trzeba
jednak osobnego upscale: sam podbija wynik do 3840×2160, czyli ponad wymagane 2K,
w cenie tej samej generacji.

Flaga --standard wyłącza tryb Ultra (mniej kredytów, ale wynik zostaje przy
zażądanym width×height — bez automatycznego podbicia do 3840×2160, więc żeby
dojść do min. 2K trzeba by dodatkowo użyć --upscale). --standard można łączyć z
--raw (kolejność: --standard --raw "prompt" ...).

Flaga --steps N ustawia liczbę kroków dyfuzji (num_inference_steps) ręcznie —
domyślnie, gdy pominięta, Leonardo sam dobiera 15. Niższa wartość = jeszcze
jeden poziom jakości niżej niż zwykły --standard (szybciej/taniej, mniej
detalu), przy tej samej rozdzielczości. Kolejność flag: --standard --steps N
--raw "prompt" ...

Opis sceny (bez --raw) podać BEZ kanonicznego bloku stylu i negative promptu —
te są już wpisane na stałe poniżej (patrz etap3-prompty-stylu.md), doklejane
automatycznie. Z flagą --raw podać kompletny, już ostylowany prompt (np.
skopiowany wprost z prompty.md / prompty-opus.md) — przydatne, gdy dany kadr ma
własny wariant palety wg łuku kolorystycznego i generyczny prefiks by go nadpisał.
"""

import json
import os
import ssl
import sys
import time
import urllib.request

import certifi

SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())
# urlretrieve (used to download generated images from a separate CDN host) ignores
# per-request contexts, so install this as the process-wide default HTTPS context.
urllib.request.install_opener(
    urllib.request.build_opener(urllib.request.HTTPSHandler(context=SSL_CONTEXT))
)

API_BASE = "https://cloud.leonardo.ai/api/rest/v1"
MODEL_ID_PHOENIX_1_0 = "de7d3faf-762f-48e0-b3b7-9d0ac3a3fcf3"

STYLE_PREFIX = (
    "Breathtaking watercolor painting, rich watercolor textures, intricate flowing "
    "details, dramatic composition, airy pastel palette of ivory white, pale gold, "
    "light sky blue and gentle rose, radiant heavenly light, full bleed with paint "
    "covering the entire canvas edge to edge, no white paper borders. "
)
STYLE_SUFFIX = " dreamy soft focus. 16:9 cinematic composition."

NEGATIVE_PROMPT = (
    "ordinary people, crowd, modern clothing, dark, gloomy, black, deep navy, heavy "
    "shadows, ominous mood, white paper border, unpainted edges, photorealistic, 3D "
    "render, text, watermark, three arms, extra limbs, deformed hands, fused bodies, "
    "merged figures, distorted face, face, facing camera, front view, detailed face, "
    "eye contact"
)


USD_TO_PLN = 3.76  # przybliżony kurs NBP/rynkowy — aktualizować w razie potrzeby


def print_cost(cost_obj):
    if not cost_obj:
        return
    usd = float(cost_obj["amount"])
    pln = usd * USD_TO_PLN
    print(f"koszt: ${usd:.4f} (~{pln:.2f} zł)")


def download_file(url, out_path):
    # Plain urlretrieve sends a "Python-urllib/x.y" User-Agent that the CDN hosting
    # generated images rejects with 403 — a browser-like UA is required.
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp, open(out_path, "wb") as f:
        f.write(resp.read())


def api_request(method, path, payload=None, api_key=None):
    url = f"{API_BASE}{path}"
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {api_key}")
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json")
    with urllib.request.urlopen(req, context=SSL_CONTEXT) as resp:
        return json.loads(resp.read())


def generate(scene_description, out_dir, name_prefix="gen", num_images=1, width=1920,
             height=1080, contrast=3.5, raw_prompt=False, ultra=True, steps=None):
    api_key = os.environ.get("LEONARDO_API_KEY")
    if not api_key:
        sys.exit("Brak LEONARDO_API_KEY w zmiennych środowiskowych.")

    prompt = scene_description if raw_prompt else f"{STYLE_PREFIX}{scene_description} {STYLE_SUFFIX}"

    payload = {
        "modelId": MODEL_ID_PHOENIX_1_0,
        "prompt": prompt,
        "negative_prompt": NEGATIVE_PROMPT,
        "width": width,
        "height": height,
        "contrast": contrast,
        "ultra": ultra,
        "num_images": num_images,
    }
    if steps is not None:
        payload["num_inference_steps"] = steps

    print("Wysyłanie zlecenia generacji...")
    created = api_request("POST", "/generations", payload, api_key)
    generation_id = created["sdGenerationJob"]["generationId"]
    print_cost(created["sdGenerationJob"].get("cost"))
    print(f"generationId={generation_id}, czekam na wynik...")

    while True:
        time.sleep(5)
        status = api_request("GET", f"/generations/{generation_id}", api_key=api_key)
        gen = status["generations_by_pk"]
        if gen["status"] == "COMPLETE":
            images = gen["generated_images"]
            break
        if gen["status"] == "FAILED":
            sys.exit(f"Generacja nie powiodła się: {gen}")
        print(f"  status={gen['status']}...")

    os.makedirs(out_dir, exist_ok=True)
    letters = "abcdefghij"
    for i, img in enumerate(images):
        suffix = f"_{letters[i]}" if len(images) > 1 else ""
        out_path = os.path.join(out_dir, f"{name_prefix}{suffix}.jpg")
        download_file(img["url"], out_path)
        print(f"zapisano {out_path} (generatedImageId={img['id']})")


def upscale(generated_image_id, out_path, multiplier=2):
    api_key = os.environ.get("LEONARDO_API_KEY")
    if not api_key:
        sys.exit("Brak LEONARDO_API_KEY w zmiennych środowiskowych.")

    payload = {
        "generatedImageId": generated_image_id,
        "upscaleMultiplier": multiplier,
        "ultraUpscaleStyle": "ARTISTIC",
        "creativityStrength": 5,
        "detailContrast": 5,
        "similarity": 5,
    }
    print("Wysyłanie zlecenia upscale...")
    created = api_request("POST", "/variations/universal-upscaler", payload, api_key)
    variation_id = created["universalUpscaler"]["id"]
    print_cost(created["universalUpscaler"].get("cost"))
    print(f"variationId={variation_id}, czekam na wynik...")

    while True:
        time.sleep(5)
        status = api_request("GET", f"/variations/{variation_id}", api_key=api_key)
        var = status["generated_image_variation_generic"][0]
        if var["status"] == "COMPLETE":
            url = var["url"]
            break
        if var["status"] == "FAILED":
            sys.exit(f"Upscale nie powiódł się: {var}")
        print(f"  status={var['status']}...")

    download_file(url, out_path)
    print(f"zapisano {out_path}")


def fetch(generation_id, out_dir, name_prefix="gen"):
    """Pobiera obrazy z już ukończonej generacji (bez ponownego płacenia za generację) —
    przydatne, gdy generacja się powiodła, ale sam download po stronie klienta zawiódł."""
    api_key = os.environ.get("LEONARDO_API_KEY")
    if not api_key:
        sys.exit("Brak LEONARDO_API_KEY w zmiennych środowiskowych.")

    status = api_request("GET", f"/generations/{generation_id}", api_key=api_key)
    gen = status["generations_by_pk"]
    if gen["status"] != "COMPLETE":
        sys.exit(f"Generacja nie jest ukończona (status={gen['status']}).")

    os.makedirs(out_dir, exist_ok=True)
    letters = "abcdefghij"
    for i, img in enumerate(gen["generated_images"]):
        suffix = letters[i] if i < len(letters) else str(i)
        out_path = os.path.join(out_dir, f"{name_prefix}_{suffix}.jpg")
        download_file(img["url"], out_path)
        print(f"zapisano {out_path} (generatedImageId={img['id']})")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--fetch":
        fetch(args[1], args[2], args[3] if len(args) > 3 else "gen")
        sys.exit(0)
    if args and args[0] == "--upscale":
        image_id = args[1]
        out_path = args[2]
        multiplier = float(args[3]) if len(args) > 3 else 2
        upscale(image_id, out_path, multiplier)
        sys.exit(0)

    ultra = True
    if args and args[0] == "--standard":
        ultra = False
        args = args[1:]
    steps = None
    if args and args[0] == "--steps":
        steps = int(args[1])
        args = args[2:]
    raw = False
    if args and args[0] == "--raw":
        raw = True
        args = args[1:]
    scene = args[0]
    out_dir = args[1]
    name_prefix = args[2] if len(args) > 2 else "gen"
    num_images = int(args[3]) if len(args) > 3 else 1
    width = int(args[4]) if len(args) > 4 else 1920
    height = int(args[5]) if len(args) > 5 else 1080
    contrast = float(args[6]) if len(args) > 6 else 3.5
    generate(scene, out_dir, name_prefix, num_images, width, height, contrast, raw_prompt=raw, ultra=ultra, steps=steps)
