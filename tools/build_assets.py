"""Generates every SVG in ../assets. Edit PROJECTS below, then run:  python tools/build_assets.py

No dependencies (standard library only). All animation is SMIL inside the SVG,
which GitHub renders when the file is embedded with <img>.
"""
import textwrap
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

SANS = "Inter, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"
CYAN, VIOLET, BLUE = "#22D3EE", "#8B5CF6", "#3B82F6"
TEXT, MUTED, DIM = "#F8FAFC", "#94A3B8", "#64748B"

# ------------------------------------------------------------------ EDIT ME
# desc / stack / status are optional. Leave them out and the card stays clean.
PROJECTS = [
    dict(slug="incognitohub", name="IncognitoHub", accent=CYAN, status="Active",
         desc="Privacy-first Android messaging with secure pairing, real-time communication and P2P.",
         stack=["Kotlin", "Android", "WebSocket"]),
    dict(slug="signalx", name="SignalX 5G", accent=BLUE, status="Active",
         desc="Android network utility for viewing mobile network and 5G status, with quick access to system network settings.",
         stack=["Kotlin", "Jetpack Compose", "Material 3"]),
    dict(slug="rewindr", name="Rewindr", accent=VIOLET, status="Completed",
         desc="A modern video player with timestamp markers, quick navigation and a clean viewing experience.",
         stack=["HTML", "CSS", "JavaScript"]),
    dict(slug="jobfusion", name="Jobfusion", accent=VIOLET, status="Completed",
         desc="Full-stack job discovery platform connecting talent with career opportunities.",
         stack=["Node.js", "Express", "MongoDB"]),
    dict(slug="calculator", name="Angular + .NET Calculator", accent=CYAN, status="Completed",
         desc="Calculator application with an Angular frontend and a .NET backend API.",
         stack=["Angular", "TypeScript", ".NET"]),
    dict(slug="portfolio", name="Portfolio", accent=BLUE, status="Active",
         desc="Personal portfolio website with my projects, skills and contact details.",
         stack=["HTML", "CSS", "JavaScript"]),
]
LOCATION = "Maharashtra, India"
HEADLINE = "Full-Stack Developer building modern web, backend and Android applications."
ROTATING = [  # the animated terminal line in the header
    "building modern Angular + .NET applications",
    "exploring Android and real-time systems",
    "shipping privacy-focused products",
]
BUILDING = [
    ("IncognitoHub", "Building privacy-focused communication features.", CYAN),
    ("SignalX 5G", "Exploring Android networking and device capabilities.", BLUE),
]
FOCUS = ["Scalable web applications", "REST APIs", "Real-time communication", "Modern Angular applications",
         "Android applications", "Performance optimization", "Developer tools", "Privacy-focused products"]
JOURNEY = [
    ("2023", "Started software development journey"),
    ("2024", "Built academic and personal projects"),
    ("2025", "B.Tech and professional development"),
    ("2026", "Building production-oriented web, Android and developer projects"),
]
CTA = "Let's build something useful."
# ---------------------------------------------------------------------------


def write(name, body):
    (OUT / name).write_text(body, encoding="utf-8")


def defs(prefix=""):
    return f'''<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0B0F19"/><stop offset="1" stop-color="#0F1730"/></linearGradient>
<linearGradient id="ln" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="{VIOLET}"/></linearGradient>
<linearGradient id="wv" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="{CYAN}" stop-opacity="0.30"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0.30"/></linearGradient>
<radialGradient id="o1"><stop offset="0" stop-color="{CYAN}" stop-opacity="0.28"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
<radialGradient id="o2"><stop offset="0" stop-color="{VIOLET}" stop-opacity="0.26"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#FFFFFF" stroke-opacity="0.035"/></pattern>'''


def wave(y, amp, dur, opacity, shift, height):
    """Seamless horizontal wave (period 320px, scrolls two periods)."""
    d = f"M0,{y} " + " ".join(f"Q{x + 80},{y - amp} {x + 160},{y} T{x + 320},{y}" for x in range(0, 2560, 320))
    d += f" L2560,{height} L0,{height} Z"
    return (f'<path d="{d}" fill="url(#wv)" opacity="{opacity}" transform="translate({shift},0)">'
            f'<animateTransform attributeName="transform" type="translate" from="{shift} 0" to="{shift - 640} 0" '
            f'dur="{dur}s" repeatCount="indefinite"/></path>')


def header():
    W, H = 1280, 360
    lines = ""
    for i, t in enumerate(ROTATING):
        lines += (f'<text x="80" y="266" font-family="{MONO}" font-size="16" fill="#67E8F9" opacity="0">'
                  f'<tspan fill="{VIOLET}">$ </tspan>{escape(t)}'
                  f'<animate attributeName="opacity" dur="{4 * len(ROTATING)}s" begin="{4 * i}s" repeatCount="indefinite" '
                  f'values="0;1;1;0;0" keyTimes="0;0.06;0.28;0.34;1"/></text>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Hi, I'm Sanket Yerwadkar. {escape(HEADLINE)}">
<defs>{defs()}<clipPath id="rc"><rect width="{W}" height="{H}" rx="18"/></clipPath></defs>
<rect width="{W}" height="{H}" rx="18" fill="url(#bg)"/>
<rect width="{W}" height="{H}" rx="18" fill="url(#grid)"/>
<circle cx="220" cy="60" r="260" fill="url(#o1)"><animateTransform attributeName="transform" type="translate" values="0 0;70 30;0 0" dur="16s" repeatCount="indefinite"/></circle>
<circle cx="1080" cy="300" r="280" fill="url(#o2)"><animateTransform attributeName="transform" type="translate" values="0 0;-60 -30;0 0" dur="18s" repeatCount="indefinite"/></circle>
<g fill="none" stroke="{CYAN}">
<circle cx="1040" cy="160" r="150" stroke-opacity="0.07"/>
<g><circle cx="1040" cy="160" r="110" stroke-opacity="0.22" stroke-dasharray="3 9"/><circle cx="1150" cy="160" r="5" fill="{CYAN}" stroke="none"/>
<animateTransform attributeName="transform" type="rotate" from="0 1040 160" to="360 1040 160" dur="36s" repeatCount="indefinite"/></g>
<g><circle cx="1040" cy="160" r="66" stroke="{VIOLET}" stroke-opacity="0.35" stroke-dasharray="2 6"/><circle cx="1040" cy="94" r="4" fill="{VIOLET}" stroke="none"/>
<animateTransform attributeName="transform" type="rotate" from="360 1040 160" to="0 1040 160" dur="24s" repeatCount="indefinite"/></g>
</g>
<text x="1040" y="162" font-family="{MONO}" font-size="46" fill="#FFFFFF" fill-opacity="0.10" text-anchor="middle" dominant-baseline="middle">&lt;/&gt;</text>
<text x="80" y="84" font-family="{MONO}" font-size="14" letter-spacing="4" fill="{CYAN}">HI, I'M</text>
<text x="77" y="158" font-family="{SANS}" font-size="70" font-weight="800" letter-spacing="-1.5" fill="{TEXT}">Sanket Yerwadkar</text>
<rect x="80" y="180" width="72" height="3" rx="1.5" fill="url(#ln)"/>
<text x="80" y="220" font-family="{SANS}" font-size="20" fill="{MUTED}">{escape(HEADLINE)}</text>
{lines}
<circle cx="1046" cy="44" r="3.5" fill="{CYAN}"><animate attributeName="opacity" values="1;0.25;1" dur="2.4s" repeatCount="indefinite"/></circle>
<text x="1200" y="49" font-family="{MONO}" font-size="13" fill="{DIM}" text-anchor="end">{escape(LOCATION)}</text>
<g clip-path="url(#rc)">{wave(318, 22, 14, 0.9, 0, H)}
{wave(332, 16, 22, 0.7, -160, H)}</g>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="#FFFFFF" stroke-opacity="0.09"/>
</svg>'''
    write("header.svg", svg)


def chip(x, y, label):
    w = len(label) * 7.3 + 24
    return (f'<rect x="{x}" y="{y}" width="{w:.0f}" height="28" rx="14" fill="#FFFFFF" fill-opacity="0.05" stroke="#FFFFFF" stroke-opacity="0.14"/>'
            f'<text x="{x + w / 2:.0f}" y="{y + 18}" font-family="{MONO}" font-size="12" fill="#CBD5E1" text-anchor="middle">{escape(label)}</text>'), w


def cards():
    W, H = 640, 250
    for i, p in enumerate(PROJECTS, 1):
        a = p["accent"]
        size = 28 if len(p["name"]) <= 22 else 23
        desc = p.get("desc") or "Source code and details on GitHub."
        dl = "".join(f'<text x="32" y="{140 + 22 * n}" font-family="{SANS}" font-size="14.5" fill="{MUTED}">{escape(l)}</text>'
                     for n, l in enumerate(textwrap.wrap(desc, 66)[:3]))
        pill = ""
        if p.get("status"):
            s = p["status"].upper()
            pw = len(s) * 8 + 36
            px = W - 32 - pw
            pill = (f'<rect x="{px:.0f}" y="24" width="{pw:.0f}" height="26" rx="13" fill="{a}" fill-opacity="0.12" stroke="{a}" stroke-opacity="0.45"/>'
                    f'<circle cx="{px + 15:.0f}" cy="37" r="3" fill="{a}"><animate attributeName="r" values="3;5;3" dur="2s" repeatCount="indefinite"/>'
                    f'<animate attributeName="opacity" values="1;0.35;1" dur="2s" repeatCount="indefinite"/></circle>'
                    f'<text x="{px + 27:.0f}" y="41.5" font-family="{MONO}" font-size="11" letter-spacing="1.2" fill="{a}">{escape(s)}</text>')
        chips, x = "", 32
        for t in p.get("stack", []):
            c, w = chip(x, H - 60, t)
            chips += c
            x += w + 8
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(p['name'])} project card">
<defs>{defs()}<radialGradient id="ac"><stop offset="0" stop-color="{a}" stop-opacity="0.35"/><stop offset="1" stop-color="{a}" stop-opacity="0"/></radialGradient></defs>
<rect width="{W}" height="{H}" rx="16" fill="url(#bg)"/>
<rect width="{W}" height="{H}" rx="16" fill="url(#grid)"/>
<circle cx="{W - 40}" cy="20" r="170" fill="url(#ac)"/>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="16" fill="none" stroke="#FFFFFF" stroke-opacity="0.11"/>
<rect x="32" y="0" width="56" height="3" rx="1.5" fill="{a}"/>
<text x="32" y="42" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{a}">{i:02d}</text>
{pill}
<text x="31" y="92" font-family="{SANS}" font-size="{size}" font-weight="700" letter-spacing="-0.4" fill="{TEXT}">{escape(p['name'])}</text>
<rect x="32" y="108" width="40" height="2.5" rx="1.25" fill="url(#ln)"/>
{dl}
{chips}
<text x="{W - 32}" y="{H - 41}" font-family="{MONO}" font-size="12" fill="{a}" text-anchor="end">GitHub  →</text>
</svg>'''
        write(f"card-{p['slug']}.svg", svg)


def building():
    W, H = 1280, 150
    panels = ""
    for i, (name, line, a) in enumerate(BUILDING):
        x = 0 if i == 0 else 648
        panels += f'''<g transform="translate({x},0)">
<rect x="0.5" y="0.5" width="631" height="{H - 1}" rx="16" fill="url(#bg)" stroke="#FFFFFF" stroke-opacity="0.11"/>
<circle cx="40" cy="42" r="5" fill="{a}"/><circle cx="40" cy="42" r="5" fill="none" stroke="{a}"><animate attributeName="r" values="5;14" dur="2.2s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.8;0" dur="2.2s" repeatCount="indefinite"/></circle>
<text x="62" y="47" font-family="{MONO}" font-size="12" letter-spacing="2.5" fill="{a}">IN DEVELOPMENT</text>
<text x="32" y="92" font-family="{SANS}" font-size="26" font-weight="700" fill="{TEXT}">{escape(name)}</text>
<text x="32" y="122" font-family="{SANS}" font-size="15" fill="{MUTED}">{escape(line)}</text></g>'''
    write("building.svg", f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Currently building: IncognitoHub and SignalX 5G"><defs>{defs()}</defs>{panels}</svg>')


def focus():
    W, H = 1280, 190
    tiles = ""
    for i, t in enumerate(FOCUS):
        x, y = (i % 4) * 326, (i // 4) * 100
        tiles += f'''<g transform="translate({x},{y})"><rect x="0.5" y="0.5" width="299" height="89" rx="14" fill="url(#bg)" stroke="#FFFFFF" stroke-opacity="0.11"/>
<rect x="24" y="0" width="32" height="2.5" rx="1.25" fill="url(#ln)"/>
<text x="24" y="34" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{CYAN}">{i + 1:02d}</text>
<text x="24" y="64" font-family="{SANS}" font-size="17" font-weight="600" fill="{TEXT}">{escape(t)}</text></g>'''
    write("focus.svg", f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Engineering focus: {escape(", ".join(FOCUS))}"><defs>{defs()}</defs><g transform="translate(-0,0)">{tiles}</g></svg>')


def journey():
    W, H = 1280, 210
    xs = [160, 480, 800, 1120]
    nodes = ""
    for x, (yr, txt) in zip(xs, JOURNEY):
        lines = "".join(f'<text x="{x}" y="{130 + 21 * n}" font-family="{SANS}" font-size="14.5" fill="{MUTED}" text-anchor="middle">{escape(l)}</text>'
                        for n, l in enumerate(textwrap.wrap(txt, 30)[:3]))
        nodes += (f'<circle cx="{x}" cy="60" r="7" fill="#0B0F19" stroke="{CYAN}" stroke-width="2"/>'
                  f'<text x="{x}" y="104" font-family="{SANS}" font-size="26" font-weight="800" fill="{TEXT}" text-anchor="middle">{yr}</text>{lines}')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Developer journey: {escape(' / '.join(y + ' ' + t for y, t in JOURNEY))}">
<defs>{defs()}</defs>
<rect width="{W}" height="{H}" rx="18" fill="url(#bg)"/>
<rect width="{W}" height="{H}" rx="18" fill="url(#grid)"/>
<rect x="160" y="59" width="960" height="2" fill="url(#ln)" opacity="0.5"/>
{nodes}
<circle r="5" cy="60" fill="{CYAN}"><animate attributeName="cx" values="160;1120;160" dur="10s" repeatCount="indefinite"/></circle>
<circle r="14" cy="60" fill="{CYAN}" opacity="0.18"><animate attributeName="cx" values="160;1120;160" dur="10s" repeatCount="indefinite"/></circle>
</svg>'''
    write("journey.svg", svg)


def footer():
    W, H = 1280, 240
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(CTA)}">
<defs>{defs()}<clipPath id="rc"><rect width="{W}" height="{H}" rx="18"/></clipPath></defs>
<rect width="{W}" height="{H}" rx="18" fill="url(#bg)"/>
<rect width="{W}" height="{H}" rx="18" fill="url(#grid)"/>
<circle cx="640" cy="40" r="300" fill="url(#o1)"><animateTransform attributeName="transform" type="translate" values="-80 0;80 20;-80 0" dur="18s" repeatCount="indefinite"/></circle>
<text x="640" y="92" font-family="{MONO}" font-size="13" letter-spacing="4" fill="{CYAN}" text-anchor="middle">CONTACT</text>
<text x="640" y="148" font-family="{SANS}" font-size="46" font-weight="800" letter-spacing="-1" fill="{TEXT}" text-anchor="middle">{escape(CTA)}</text>
<g clip-path="url(#rc)">{wave(206, 14, 16, 0.9, 0, H)}
{wave(220, 10, 24, 0.7, -160, H)}</g>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="#FFFFFF" stroke-opacity="0.09"/>
</svg>'''
    write("footer.svg", svg)


def divider():
    write("divider.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="8" viewBox="0 0 1280 8" role="presentation"><defs><linearGradient id="d" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="{CYAN}" stop-opacity="0"/><stop offset="0.5" stop-color="{CYAN}" stop-opacity="0.55"/><stop offset="0.75" stop-color="{VIOLET}" stop-opacity="0.55"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></linearGradient></defs><rect y="3" width="1280" height="1" fill="url(#d)"/></svg>''')


if __name__ == "__main__":
    header(); cards(); building(); focus(); journey(); footer(); divider()
    print("Assets written to", OUT)
