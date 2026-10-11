#!/usr/bin/env bash
# Renders review screenshots of the site at the repo root.
# Override the browser with CHROME=...
# Writes PNGs to tools/review/. Run from anywhere: ./tools/render.sh
C=${CHROME:-/usr/bin/google-chrome}
TOOLS="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$TOOLS/.." && pwd)"
mkdir -p "$TOOLS/review"
# lazy images do not load in one-shot headless captures, so render from a temp copy with eager loading
T="$TOOLS/.render-tmp"
rm -rf "$T"
mkdir -p "$T"
cp -r "$ROOT/assets" "$ROOT"/*.html "$ROOT"/*.css "$T/"
# GNU and BSD sed both accept -i.bak
sed -i.bak 's/loading="lazy" decoding="async"//' "$T"/*.html
rm -f "$T"/*.bak
shot(){ "$C" --headless --no-sandbox --disable-gpu --hide-scrollbars --virtual-time-budget=4000 --force-device-scale-factor=1 --window-size=$2,$3 --screenshot="$TOOLS/review/$1.png" "file://$T/$4" 2>/dev/null; }
shot desktop-full 1280 5600 index.html
mframe(){ printf '<body style="margin:0;background:#888"><iframe src="%s" width="390" height="%s" style="border:0;display:block"></iframe>' "$1" "$2" > "$T/_m_$3.html"; shot "$3" 500 "$2" "_m_$3.html"; }
# Chrome headless has a 500px minimum window width, so 390 is rendered inside an iframe (true 390px viewport)
mframe index.html 6600 mobile-full
shot tablet-full 768 6400 index.html
shot privacy-desktop 1280 2200 privacy.html
mframe privacy.html 3600 privacy-mobile
rm -rf "$T"
