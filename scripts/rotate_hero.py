"""Rebuild assets/hero.svg around a random DeepSeek-chan pose (never the current one).

Run hourly by .github/workflows/rotate-hero.yml. Pass a pose id to pick one: python scripts/rotate_hero.py 050
"""
import base64
import random
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
hero = root / "assets/hero.svg"

# pose id -> speech bubble: setup line, punchline
POSES = {
    "050": ("Code's deployed. Off to lunch —", "just one bowl!"),
    "123": ("Can I eat at your place?", "Just one bowl!"),
    "070": ("Okay, fine.", "Now I'm the user!"),
    "010": ("Read your code. Verdict:", "a high-end model!"),
}

FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei','Noto Sans CJK SC',sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="880" height="400" viewBox="0 0 880 400" role="img" aria-labelledby="t d" data-pose="{key}">
<title id="t">Hi, I'm Yulin · DYL521</title>
<desc id="d">AI application engineer and Python backend developer. DeepSeek-chan pose #{key} says: {line1} {line2}</desc>
<defs><clipPath id="c"><rect width="880" height="400" rx="28"/></clipPath></defs>
<g clip-path="url(#c)" font-family="{font}">
<rect width="880" height="400" fill="#121A4A"/>
<circle cx="690" cy="262" r="168" fill="#1B2766"/>
<circle cx="458" cy="330" r="6" fill="none" stroke="#3C5BB8" stroke-width="2"/>
<circle cx="852" cy="132" r="7" fill="none" stroke="#5E8FE8" stroke-width="2"/>
<circle cx="836" cy="160" r="4" fill="none" stroke="#5E8FE8" stroke-width="2"/>
<text x="48" y="74" font-family="{mono}" font-size="14" fill="#9FC9FF">› Thought for 3 seconds · decided to say hi</text>
<text x="46" y="142" font-size="52" font-weight="700" fill="#FFFFFF">Hi, I'm Yulin</text>
<text x="48" y="182" font-size="20" font-weight="500" fill="#E3ECFF">Yulin Deng · DYL521</text>
<text x="48" y="222" font-size="16" fill="#B8C8F0">AI application engineer · Python backend</text>
<text x="48" y="246" font-size="16" fill="#B8C8F0">8 years of RAG, agents and enterprise systems</text>
<g font-size="13" fill="#E3ECFF">
<rect x="48" y="286" width="56" height="28" rx="14" fill="none" stroke="#4A63B8" stroke-width="1.5"/><text x="62" y="305">RAG</text>
<rect x="112" y="286" width="110" height="28" rx="14" fill="none" stroke="#4A63B8" stroke-width="1.5"/><text x="126" y="305">Agents · MCP</text>
<rect x="230" y="286" width="96" height="28" rx="14" fill="none" stroke="#4A63B8" stroke-width="1.5"/><text x="244" y="305">LlamaIndex</text>
<rect x="334" y="286" width="76" height="28" rx="14" fill="none" stroke="#4A63B8" stroke-width="1.5"/><text x="348" y="305">FastAPI</text>
</g>
<image x="520" y="110" width="340" height="290" preserveAspectRatio="xMidYMax meet" href="data:image/webp;base64,{img}"/>
<rect x="450" y="24" width="296" height="72" rx="20" fill="#0B1138"/>
<rect x="450" y="18" width="296" height="72" rx="20" fill="#FFFFFF"/>
<path d="M650 88 L686 88 L694 112 Z" fill="#FFFFFF"/>
<text x="470" y="47" font-size="16" fill="#141B4D">{line1}</text>
<text x="470" y="74" font-size="20" font-weight="700" fill="#2449B8">{line2}</text>
</g>
</svg>
"""

current = re.search(r'data-pose="(\d+)"', hero.read_text()) if hero.exists() else None
choices = [k for k in POSES if not current or k != current[1]]
key = sys.argv[1] if len(sys.argv) > 1 else random.choice(choices)
line1, line2 = POSES[key]
img = base64.b64encode((root / f"assets/deepseek-chan/{key}.webp").read_bytes()).decode()
hero.write_text(TEMPLATE.format(key=key, line1=line1, line2=line2, img=img, font=FONT, mono=MONO))
print(key)
