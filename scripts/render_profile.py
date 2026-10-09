#!/usr/bin/env python3
"""Build self-contained profile SVGs with outlined Syne type and quiet motion.

Only asset authoring needs FontTools (4.61.1). The resulting SVGs require no
fonts, scripts, remote images, or rendering service when GitHub displays them.
"""

import base64
from functools import lru_cache
from html import escape
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "profile"


@lru_cache
def font(weight):
    variable = TTFont(ASSETS / "fonts" / "Syne[wght].ttf")
    return instantiateVariableFont(variable, {"wght": weight}, inplace=True)


def wordmark(label, x, y, size, fill, max_width=None, weight=800):
    face = font(weight)
    glyphs = face.getGlyphSet()
    cmap = face.getBestCmap()
    pen = SVGPathPen(glyphs)
    cursor = 0
    for char in label:
        name = cmap[ord(char)]
        glyphs[name].draw(TransformPen(pen, (1, 0, 0, 1, cursor, 0)))
        cursor += face["hmtx"][name][0]
    scale = size / face["head"].unitsPerEm
    if max_width is not None:
        scale = min(scale, max_width / cursor)
    return f'<path d="{pen.getCommands()}" transform="translate({x} {y}) scale({scale:g} {-scale:g})" fill="{fill}"/>'


def text(x, y, label, size=12, fill="#acbccb", spacing=0, anchor="start"):
    return (
        f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" '
        f'font-size="{size}" fill="{fill}" letter-spacing="{spacing}" '
        f'text-anchor="{anchor}">{escape(label)}</text>'
    )


MOTION = """
.shimmer { animation: shimmer 14s linear infinite; }
.aura { animation: aura 7s ease-in-out infinite; }
.water { animation: water 16s linear infinite; }
.spark { animation: spark 8s ease-in-out infinite; }
.orbit { animation: orbit 16s linear infinite; transform-box:fill-box; transform-origin:center; }
.packet { animation: packet 6s ease-in-out infinite; }
.wave { animation: wave 2.8s ease-in-out infinite; transform-box:fill-box; transform-origin:center; }
@keyframes shimmer { 0%,45% {transform:translateX(-650px)} 85%,100% {transform:translateX(1100px)} }
@keyframes aura { 0%,100% {opacity:.18} 50% {opacity:.42} }
@keyframes water { to {stroke-dashoffset:-240} }
@keyframes spark { 0%,100% {opacity:.08;transform:translateY(0)} 50% {opacity:.55;transform:translateY(-8px)} }
@keyframes orbit { to {transform:rotate(360deg)} }
@keyframes packet { 0%,8% {opacity:0;transform:translate(0,0)} 18% {opacity:1;transform:translate(0,0)} 70% {opacity:1;transform:translate(70px,-16px)} 82%,100% {opacity:0;transform:translate(70px,-16px)} }
@keyframes wave { 0%,100% {transform:scaleY(.3)} 50% {transform:scaleY(1)} }
@media (prefers-reduced-motion:reduce) {
 .shimmer,.aura,.water,.spark,.orbit,.packet,.wave {animation:none!important}
 .shimmer {opacity:0!important}
 .packet {opacity:0!important}
 .aura {opacity:.22!important}
 .spark {opacity:.2!important}
}
"""


def svg_start(width, height, title, description=""):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>',
        f'<style>{MOTION}</style>',
    ]


@lru_cache
def image_data(name):
    return "data:image/png;base64," + base64.b64encode((ASSETS / "source" / name).read_bytes()).decode()


def anime_panel(character, mobile=False):
    hero = character == "goku"
    width = 440 if mobile else 1000
    height = (350 if hero else 260) if mobile else (320 if hero else 245)
    title = "Yash | AI Engineer | Goku Ultra Instinct and Satoru Gojo" if hero else "Outside work | Tanjiro from Demon Slayer"
    description = (
        "LLMs, agents, and backends. Based in India. Goku and Gojo in silver and cyan artwork with slow ambient motion. One more quick fix. Famous last words."
        if hero else "Anime and side projects. Tanjiro in matching silver-blue ink artwork."
    )
    parts = svg_start(width, height, title, description)
    if hero:
        name = (26, 263, 48, 220) if mobile else (42, 134, 62, 270)
        paths = wordmark("Yash", *name[:3], "url(#silver)", max_width=name[3], weight=700)
        clip_paths = paths.replace('fill="url(#silver)"', 'fill="white"')
    else:
        names = [(24, 207, 30, 260)] if mobile else [(42, 144, 64, 555)]
        paths = wordmark("AFTER HOURS", *names[0][:3], "url(#silver)", max_width=names[0][3])
        clip_paths = paths.replace('fill="url(#silver)"', 'fill="white"')
    parts += [
        '<defs>',
        f'<clipPath id="panel"><rect width="{width}" height="{height}" rx="14"/></clipPath>',
        f'<clipPath id="name-clip">{clip_paths}</clipPath>',
        '<linearGradient id="silver" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#f5f9fc"/><stop offset="1" stop-color="#b6c9d9"/></linearGradient>',
        '<linearGradient id="shine"><stop stop-color="white" stop-opacity="0"/><stop offset=".5" stop-color="white" stop-opacity=".65"/><stop offset="1" stop-color="white" stop-opacity="0"/></linearGradient>',
        '<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset=".3" stop-color="#080f17" stop-opacity="0"/><stop offset=".76" stop-color="#080f17" stop-opacity=".95"/><stop offset="1" stop-color="#080f17"/></linearGradient>',
        '<linearGradient id="leftfade"><stop stop-color="#080f17" stop-opacity=".2"/><stop offset=".52" stop-color="#080f17" stop-opacity=".07"/><stop offset="1" stop-color="#080f17" stop-opacity="0"/></linearGradient>',
        '</defs>',
        '<g clip-path="url(#panel)">',
        f'<rect width="{width}" height="{height}" fill="#080f17"/>',
    ]
    src = image_data(character + ".png")
    if mobile:
        img_width, img_height = (760, 253) if hero else (750, 250)
        x = -316 if hero else -310
        y = 0 if hero else -18
        parts.append(f'<image href="{src}" x="{x}" y="{y}" width="{img_width}" height="{img_height}" preserveAspectRatio="xMidYMid slice"/>')
        parts.append(f'<rect width="{width}" height="{height}" fill="url(#fade)"/>')
    else:
        parts.append(f'<image href="{src}" width="{width}" height="{height}" preserveAspectRatio="xMidYMid slice"/>')
        parts.append(f'<rect width="{width}" height="{height}" fill="url(#leftfade)"/>')
    if hero:
        parts += [
            f'<path class="aura" d="M{width-100} 22 Q{width-38} 120 {width-25} {height-35}" stroke="#8bddf3" stroke-width="2" fill="none" opacity=".2"/>',
            f'<path class="aura" d="M20 {height-15}H{width-20}" stroke="#67e8f9" stroke-width="1" opacity=".2" style="animation-delay:-3s"/>',
            paths,
            f'<g clip-path="url(#name-clip)"><rect class="shimmer" x="0" y="0" width="110" height="{height}" fill="url(#shine)"/></g>',
        ]
        parts.append(text(26 if mobile else 42, 32 if mobile else 64, "AI ENGINEER", 11 if mobile else 13, "#7dd8ee", 2.4))
        parts.append(text(26 if mobile else 42, 293 if mobile else 173, "LLMs / agents / backends", 14 if mobile else 17, "#c6d5e0"))
        if mobile:
            parts.append(text(26, 326, "One more quick fix. Famous last words.", 11, "#a2b5c4"))
        else:
            parts.append(text(42, 228, "One more quick fix.", 14, "#c6d5e0"))
            parts.append(text(42, 250, "Famous last words.", 12, "#899fae"))
            parts.append(text(42, 291, "BASED IN INDIA / WORKING REMOTELY", 9, "#899fae", 1.1))
    else:
        parts += [
            paths,
            text(24 if mobile else 42, 233 if mobile else 180, "ANIME / SIDE PROJECTS", 10 if mobile else 12, "#9eb8c9", 1.5),
            f'<path class="water" d="M-40 {height-22}C100 {height-52} 180 {height+12} 360 {height-28}S750 {height-10} {width+30} {height-52}" fill="none" stroke="#8de8f5" stroke-width="1.2" stroke-dasharray="35 85" opacity=".48"/>',
            f'<path class="aura" d="M20 {height-12}H{width-20}" stroke="#67e8f9" stroke-width="1" opacity=".2"/>',
        ]
    for i, (x, y) in enumerate([(width-52, 70), (width-160, 125), (width-95, height-55)]):
        parts.append(f'<circle class="spark" cx="{x}" cy="{y}" r="1.5" fill="#a4e6f6" style="animation-delay:-{i*2}s"/>')
    parts += [
        '</g>',
        f'<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="14" fill="none" stroke="#263b4d"/>',
        f'<path d="M16 39V16H39M{width-39} 16H{width-16}V39M16 {height-39}V{height-16}H39M{width-39} {height-16}H{width-16}V{height-39}" fill="none" stroke="#6ed4e9" stroke-width="1" opacity=".6"/>',
        '</svg>',
    ]
    return "\n".join(parts) + "\n"


PROJECTS = [
    ("oryxenai", "01", "OryxenAI", "AGENT WORKFLOWS", "Context / review / Studio", "orbit"),
    ("quotamesh", "02", "QuotaMesh", "AI INFRASTRUCTURE", "Routing / cooldowns / fallback", "route"),
    ("receptionist", "03", "AI Receptionist", "VOICE AI / TEAM PROJECT", "Voice / tools / scheduling", "voice"),
]


def static_variant(svg):
    """An explicit static file also works when image CSS ignores page emulation."""
    quiet_style = '.shimmer,.packet {display:none} .aura {opacity:.22} .spark {opacity:.2}'
    return svg.replace(MOTION, quiet_style).replace(
        "with slow ambient motion", "with a static composition"
    ).replace("Decorative animated schematic", "Decorative schematic")


def save_variants(filename, svg):
    (ASSETS / filename).write_text(svg, encoding="utf-8")
    (ASSETS / filename.replace(".svg", "-static.svg")).write_text(static_variant(svg), encoding="utf-8")


def project_panel(project, dark=False, mobile=False):
    slug, number, name, category, caption, glyph = project
    width, height = (440, 98) if mobile else (1000, 126)
    bg, line, foreground, muted, accent = (
        ("#101922", "#253444", "#eaf2f8", "#9caebb", "#78dced") if dark
        else ("#f6f8fa", "#d4dde5", "#172b3b", "#526678", "#087e91")
    )
    parts = svg_start(width, height, name, caption + ". Decorative animated schematic; not a live status display.")
    parts += [
        f'<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="12" fill="{bg}" stroke="{line}"/>',
        f'<path d="M18 25V{height-25}" stroke="{accent}" stroke-width="2"/>',
        text(34, 32 if mobile else 37, f"{number} / {category}", 9 if mobile else 11, muted, 1.1),
        wordmark(name, 33, 73 if mobile else 83, 27 if mobile else 39, foreground, max_width=310 if mobile else 575),
    ]
    if not mobile:
        parts.append(text(width-32, 104, caption, 12, muted, anchor="end"))
    px, py = (391, 57) if mobile else (922, 49)
    parts.append(f'<g transform="translate({px} {py})" stroke="{accent}" fill="none" stroke-width="1.4">')
    if glyph == "orbit":
        parts += [
            '<ellipse rx="28" ry="10" transform="rotate(-28)"/><ellipse rx="28" ry="10" transform="rotate(28)"/>',
            f'<circle r="3" fill="{accent}" stroke="none"/>',
            f'<g class="orbit"><circle cx="23" cy="-9" r="2.4" fill="{accent}" stroke="none"/><circle cx="-23" cy="9" r="2.4" fill="{accent}" stroke="none"/></g>',
        ]
    elif glyph == "route":
        parts += [
            '<path d="M-40 0H-6L30 -16M-6 0L30 16"/>',
            f'<circle cx="-40" r="4" fill="{bg}"/><circle cx="30" cy="-16" r="4" fill="{bg}"/><circle cx="30" cy="16" r="4" fill="{bg}"/>',
            f'<circle class="packet" cx="-40" r="2.8" fill="{accent}" stroke="none"/>',
        ]
    else:
        for i, size in enumerate([10, 22, 35, 18, 42, 28, 13, 24, 8]):
            parts.append(f'<rect class="wave" x="{i*6-27}" y="{-size/2}" width="2.5" height="{size}" rx="1.25" fill="{accent}" stroke="none" style="animation-delay:-{i*.28:g}s"/>')
    parts += ['</g>', '</svg>']
    return "\n".join(parts) + "\n"


def main():
    for mobile in (False, True):
        for character, name in [("goku", "hero"), ("tanjiro", "after-hours")]:
            filename = name + ("-mobile" if mobile else "") + ".svg"
            save_variants(filename, anime_panel(character, mobile))
        for dark in (False, True):
            for project in PROJECTS:
                filename = project[0] + ("-mobile" if mobile else "") + ("-dark" if dark else "-light") + ".svg"
                save_variants(filename, project_panel(project, dark, mobile))
    print("Rendered 4 anime panels and 12 project panels, each with an explicit static variant.")


if __name__ == "__main__":
    main()
