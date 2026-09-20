import re
import sys
from pathlib import Path

def enhance_svg(file_path: Path):
    if not file_path.exists():
        return
    svg = file_path.read_text(encoding="utf-8")

    # 1. Fix missing '#' in hex colors (e.g., --cs:22D3EE -> --cs:#22D3EE)
    svg = re.sub(r'--cs:([0-9a-fA-F]{6});', r'--cs:#\1;', svg)
    svg = re.sub(r'--cs:purple;', r'--cs:#22D3EE;', svg)

    # 2. Make cells rounded modern squares instead of harsh pixel blocks
    svg = svg.replace('.c{shape-rendering:geometricPrecision;', '.c{shape-rendering:geometricPrecision;rx:3px;ry:3px;')

    # 3. Make the snake rounded and glowing with neon aura
    svg = svg.replace('.s{shape-rendering:geometricPrecision;', '.s{shape-rendering:geometricPrecision;rx:6px;ry:6px;filter:drop-shadow(0 0 5px #22D3EE);')

    # 4. Make progress bar rounded
    svg = svg.replace('.u{transform-origin:0 0;', '.u{rx:3px;ry:3px;transform-origin:0 0;')

    # 5. Add sleek rounded dark card background with border so it looks premium in both light & dark mode
    bg_card = (
        '<defs>'
        '<linearGradient id="snk-card-bg" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0" stop-color="#0E131F"/>'
        '<stop offset="1" stop-color="#0A0D14"/>'
        '</linearGradient>'
        '<linearGradient id="snk-card-border" x1="0" y1="0" x2="1" y2="0">'
        '<stop offset="0" stop-color="#22D3EE" stop-opacity="0.35"/>'
        '<stop offset="0.5" stop-color="#8B5CF6" stop-opacity="0.2"/>'
        '<stop offset="1" stop-color="#22D3EE" stop-opacity="0.1"/>'
        '</linearGradient>'
        '</defs>'
        '<rect x="-15.5" y="-31.5" width="879" height="191" rx="14" fill="url(#snk-card-bg)" stroke="url(#snk-card-border)" stroke-width="1.2"/>'
        '<text x="0" y="-12" font-family="\'SFMono-Regular\', Consolas, monospace" font-size="11" letter-spacing="2" fill="#22D3EE" opacity="0.85">● CONTRIBUTION RADAR</text>'
    )
    if 'id="snk-card-bg"' not in svg:
        svg = re.sub(r'(<style.*?</style>)', r'\1' + bg_card, svg, count=1, flags=re.DOTALL)

    file_path.write_text(svg, encoding="utf-8")
    print(f"Enhanced: {file_path}")

if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("dist")
    if target.is_dir():
        for p in target.glob("*.svg"):
            enhance_svg(p)
    elif target.is_file():
        enhance_svg(target)
