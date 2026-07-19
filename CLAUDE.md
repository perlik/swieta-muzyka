# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

Not a software project — it's the production pipeline for **Święta Muzyka**, a YouTube channel of sung psalm paraphrases (Polish, watercolor-animated lyric videos). There is no build/lint/test; "development" means producing one song's assets through eight sequential stages, tracked per-folder.

Channel: https://www.youtube.com/@swieta-muzyka · Playlist "Psalmy śpiewane": https://www.youtube.com/playlist?list=PLx3JbKsW_a05aXyvEW1BSj1Ek3tMBE0UA

## Where the rules live

The user says only "przejdź do etapu N dla Psalmu X" — the actual rules live in `instrukcje/`, split up so a session working one stage doesn't have to load everything:

- `instrukcje/styl-teledysku.md` — master index: all 8 stages summarized, shared rules (target resolution, cooperation rules). **Read this first**, always applies.
- `instrukcje/etap1-lyrics.md` — Stage 1 (lyrics for Suno AI): paraphrase rules, rhyme/syllable/punctuation constraints, section-tag template, Style of Music field, feminine-grammar rule.
- `instrukcje/etap2-napisy.md` — Stage 2 (subtitles): Whisper-based sync method. Run right after Stage 1 (lyrics) — its exact per-line timestamps feed Stage 3's frame timing. Whisper's transcription is the authoritative content when it diverges from `lirycs.txt` (Suno sometimes ad-libs words not in the submitted lyrics).
- `instrukcje/etap3-prompty-stylu.md` — Stage 3 (image prompts): full visual style, canonical prompt block, negative prompt, shot pacing/timing rules — timed against Stage 2's subtitle timestamps.
- `instrukcje/etap4-generowanie-obrazkow.md` — Stage 4 (image generation): generate the actual image files from Stage 3's prompts via the Leonardo AI REST API directly from Claude Code, no browser. Default: standard mode (no Ultra), Full HD 1920×1080, one image per frame; report cost in PLN after every call.
- `instrukcje/etap5-obrobka-obrazkow.md` — Stage 5 (image post-processing): rename/crop/convert rules, no-content-judgment rule.
- `instrukcje/etap6-opis.md` — Stage 6 (YouTube description): description format, tag rules, title rules.
- `instrukcje/etap7-miniatura.md` — Stage 7 (thumbnail): panel/text/color rules, file naming.
- `instrukcje/etap8-timeline-davinci.md` — Stage 8 (editable DaVinci Resolve timeline): generates `render/timeline_edytowalny_fcp7.xml` from Stage 5's timestamp-named image files, producing trimmable clips instead of locked ones.
- `instrukcje/lista-psalmow.md` — the 20-psalm backlog with production status (✅/⬜) — check this to find "the next psalm."
- `instrukcje/baza-linków.md` — published video URLs, keyed by psalm number. Source of truth for cross-linking "Posłuchaj także" sections.
- `kanal/top-10-fraz-kluczowych.pdf` — vidIQ SEO keyword research; source for the required phrases in every description.

## The eight stages (per song)

Work happens in a folder named `psalm N/` (created fresh for a new song). Each stage's output lands there:

1. **Lyrics** (`etap1-lyrics.md`) → `txt/lirycs.txt`. Own paraphrase only, never a copyrighted translation. Psalmist's "I" is always grammatically feminine (female vocalist) in past/conditional forms; God stays masculine. **Always run this stage on Fable** — delegate to a subagent with `model: "fable"` if the current session isn't already on that model. **Right after this stage, create the folder structure** (see below) if it doesn't exist yet.
2. **Subtitles** (`etap2-napisy.md`) → `txt/napisy.srt`. Whisper-based transcription synced to `txt/lirycs.txt`, not naive silence detection — see that file for the exact method. **Whisper's transcription is the final, authoritative source for subtitle content when it diverges from `lirycs.txt`** — not just for timing: Suno sometimes ad-libs words/phrases during generation that weren't in the submitted lyrics, and if subtitles follow `lirycs.txt` alone in those spots they drift out of sync with the audio from that point on. Isolated Whisper misrecognitions (typos, wrong word forms) still defer to `lirycs.txt`; only a consistent, repeated surplus of words not present in `lirycs.txt` at all should be treated as a real Suno addition — confirm with the user if it's ambiguous which case applies. When the detected vocal onset is ambiguous, confirm the timing with the user rather than guessing. Deliberately run right after Stage 1, before Stage 3 — its exact per-line timestamps drive Stage 3's frame layout instead of Stage 3 estimating them from a raw audio pass. **Always run this stage on Sonnet, Thinking off, effort medium** — synchronization itself is handled by a deterministic script (`whisper_napisy.py`); see `etap2-napisy.md` for the exact model note.
3. **Image prompts** (`etap3-prompty-stylu.md`) → `prompts/prompty.md`. Requires audio already in `audio/` AND `txt/napisy.srt` already generated (Stage 2) — its exact per-line timestamps drive frame boundaries and the ~1s lead offset. Prompts only — actual image generation happens in Stage 4. **This stage also decides the thumbnail source frame** (recorded explicitly in `prompty.md`) — see Stage 7. **Always run this stage on Fable** — delegate to a subagent with `model: "fable"` if the current session isn't already on that model.
4. **Image generation** (`etap4-generowanie-obrazkow.md`) → `images/` (raw, numbered files like `7.jpg`). Generate the actual image files from Stage 3's prompts via the Leonardo AI REST API, directly from Claude Code — no browser. Default: standard mode (no Ultra), Full HD 1920×1080, one image per frame, 15 diffusion steps; report the cost in PLN after every generation/upscale call. If a specific frame needs to clear the 2K minimum, use the script's `--upscale` mode rather than switching that frame to Ultra. **Model: Haiku, effort low** — the images themselves are generated by Leonardo AI (Phoenix 1.0), not by Claude.
5. **Image post-processing** (`etap5-obrobka-obrazkow.md`) — rename to timestamps, crop to 16:9, convert (q100, 4:4:4, no upscaling below 2K), all inside `images/`. Purely mechanical — no content judgment at this stage unless asked. **Model: Haiku, effort low.**
6. **Description** (`etap6-opis.md`) → `txt/opis.txt`. **Always run this stage on Fable** — delegate to a subagent with `model: "fable"` if the current session isn't already on that model.
7. **Thumbnail** (`etap7-miniatura.md`) → `images/`, always built from the frame Stage 3 designated as the thumbnail source (recorded in `prompty.md`, not necessarily the first frame) — **no user confirmation needed, this stage just executes Stage 3's decision**; text "Psalm X" + "śpiewany" via a dark rounded panel (~65% opacity, color derived from the frame's dominant hue) for mobile legibility, equal padding on all sides. Thumbnail file name must match the main title exactly. **Scope is thumbnail creation only — this stage does not rename the video file in `wideo/`.** **Model: Haiku, effort low** — a script (Pillow) handles the actual rendering.
8. **DaVinci Resolve timeline** (`etap8-timeline-davinci.md`) → `render/timeline_edytowalny_fcp7.xml`. Requires Stage 5 already done (timestamp-named files in `images/`). Runs `instrukcje/skrypty/generuj_timeline_edytowalny.py`, which places clips on the timeline per the filename timestamps as legacy Final Cut Pro 7 XML (XMEML v5) with masterclip handles, so Resolve treats them as trimmable, transition-capable clips instead of locked ones. Sequence resolution is hardcoded to 2560×1440 in the script, independent of the source images' actual pixel size. Purely mechanical — no editorial decisions at this stage. **Model: Haiku, effort low.**

Target resolution throughout (images, crops, final export): **2560×1440 (2K), 16:9** — defined once in `styl-teledysku.md`, referenced everywhere else.

## Folder structure inside each `psalm N/`

Every song folder is split by file type into six subfolders, created right after Stage 1: `images/` (all graphics, including rejects in `images/_do_usuniecia/`), `audio/` (`audio.mp3`/`audio.wav`), `prompts/` (`prompty.md` and variants), `txt/` (`lirycs.txt`, `napisy.srt`, `opis.txt`), `render/` (`movavi.mepj`, plus the Stage 8 DaVinci Resolve timeline files), `wideo/` (final exported `.mp4`). Full rule: `instrukcje/styl-teledysku.md` § "Struktura katalogów w folderze utworu".

## Cross-cutting rules that aren't obvious from one file

- **Titles must be gender-neutral** (work for both a male and female viewer) — avoid adjectives/participles that decline by gender ("samotny/samotna"); prefer noun phrases. Rule and rationale: `etap6-opis.md` § "Neutralność płciowa w tytułach".
- **Ask before expanding scope.** If a task surfaces something else that looks worth fixing (another song's file, an older entry), don't touch it — ask first. Codified in `styl-teledysku.md` § "Zasady współpracy".
- No em dash ("—") anywhere in titles/descriptions — use a plain hyphen.
- `lista-psalmow.md` status is the record of what's actually finished; don't infer "done" purely from a folder having a video file in it — confirm with the user before flipping the checkbox.

## Local tooling notes

- Subtitle sync needs `ffmpeg`/`ffprobe`, Python `requests`, and an `OPENAI_API_KEY` (Whisper transcription) — not preinstalled in a fresh environment; install via `brew install ffmpeg` / `pip3 install requests` if missing.
- Thumbnail generation uses Pillow (`pip3 install Pillow`) and the Lora font (only `Lora-Regular.ttf` is available locally, bundled inside `/Applications/HP.app/.../Resources/`; no bold/italic weight on this machine).
