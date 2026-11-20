"""Arma la carpeta _netlify y el ZIP nova-academy-netlify.zip con rutas '/' (las que entiende Netlify).

Uso, desde la carpeta del proyecto:
    python herramientas/empaquetar_netlify.py

Copia las páginas HTML y solo las imágenes que esas páginas usan.
"""
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_netlify"
ZIP = ROOT / "nova-academy-netlify.zip"
PAGES = ["index.html", "gracias.html"]  # la master class va en su propio ZIP (ver abajo)
EXTRA = ["assets/og-nova.jpg"]  # imagen para redes, referenciada con URL absoluta

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()

files = set(EXTRA)
for page in PAGES:
    src = ROOT / page
    if not src.exists():
        continue
    shutil.copy2(src, OUT / page)
    for ref in re.findall(r'(?:src|href)="([^"#:?]+)"', src.read_text(encoding="utf-8")):
        if ref.endswith(".html") or ref in ("./", "/"):
            continue
        files.add(ref)

missing = []
for ref in sorted(files):
    src = ROOT / ref
    if not src.is_file():
        missing.append(ref)
        continue
    dst = OUT / ref
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)

if ZIP.exists():
    ZIP.unlink()
with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for path in sorted(p for p in OUT.rglob("*") if p.is_file()):
        z.write(path, path.relative_to(OUT).as_posix())

print(f"ZIP listo: {ZIP.name} ({ZIP.stat().st_size // 1024} KB)")
for name in zipfile.ZipFile(ZIP).namelist():
    print("  ", name)
if missing:
    print("FALTAN:", ", ".join(missing))


# ---- Sitio aparte para la master class: masterclass.html se publica como index.html ----
MC_OUT = ROOT / "_netlify_masterclass"
MC_ZIP = ROOT / "masterclass-netlify.zip"
if MC_OUT.exists():
    shutil.rmtree(MC_OUT)
(MC_OUT / "assets").mkdir(parents=True)
mc_src = ROOT / "masterclass.html"
shutil.copy2(mc_src, MC_OUT / "index.html")
mc_files = {"assets/og-masterclass.png"}
for ref in re.findall(r'(?:src|href)="([^"#:?]+)"', mc_src.read_text(encoding="utf-8")):
    if not ref.endswith(".html") and ref not in ("./", "/"):
        mc_files.add(ref)
for ref in sorted(mc_files):
    shutil.copy2(ROOT / ref, MC_OUT / ref)
if MC_ZIP.exists():
    MC_ZIP.unlink()
with zipfile.ZipFile(MC_ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for path in sorted(p for p in MC_OUT.rglob("*") if p.is_file()):
        z.write(path, path.relative_to(MC_OUT).as_posix())
print(f"ZIP listo: {MC_ZIP.name} ({MC_ZIP.stat().st_size // 1024} KB)")
for name in zipfile.ZipFile(MC_ZIP).namelist():
    print("  ", name)
