from pathlib import Path
import re, shutil, markdown
root=Path(__file__).resolve().parents[1]
import argparse
parser=argparse.ArgumentParser(description='Render the profile palette preview (requires Python Markdown).')
parser.add_argument('--output', type=Path, required=True)
preview=parser.parse_args().output
preview.mkdir(parents=True,exist_ok=True)
css='''*{box-sizing:border-box}body{margin:0;padding:28px 20px;background:#fff;color:#1f2328;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}article{max-width:918px;margin:auto;padding:32px;border:1px solid #d1d9e0;border-radius:6px}img{max-width:100%;vertical-align:middle}img[width]{height:auto}h2{font-size:24px;font-weight:600;line-height:1.25;border-bottom:1px solid #d1d9e0;padding-bottom:8px;margin:28px 0 16px}h3{font-size:20px;margin:24px 0 16px}h4{font-size:16px;margin:24px 0 16px}a{color:#0969da;text-decoration:none}a:hover{text-decoration:underline}p{margin:0 0 16px}code{background:#818b981f;padding:.2em .4em;border-radius:6px;font-size:85%;white-space:normal}hr{border:0;height:3px;background:#d1d9e0;margin:24px 0}summary{cursor:pointer}blockquote{margin:0 0 16px;padding:0 1em;color:#59636e;border-left:.25em solid #d1d9e0}blockquote p:last-child{margin-bottom:0}.dark blockquote{color:#b1bac4;border-color:#3d444d}li{margin:4px 0}table{border-collapse:collapse;width:100%;margin-bottom:16px}th,td{border:1px solid #d1d9e0;padding:8px 12px;text-align:left}tr:nth-child(2n){background:#f6f8fa}.note{max-width:918px;margin:0 auto 16px;font-size:12px;color:#59636e;display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}body.dark{background:#0d1117;color:#e6edf3}.dark article,.dark h2,.dark th,.dark td{border-color:#30363d}.dark hr{background:#30363d}.dark tr:nth-child(2n){background:#161b22}.dark a{color:#83adff}.dark .note{color:#9aa7bb}article>p[align="center"]{line-height:1.8}article>p>a>img,article>p>img[width="270"]{margin-bottom:8px}@media(max-width:500px){body{padding:12px 8px}article{padding:16px}h2{font-size:21px}th,td{padding:6px}article>p[align="center"]{line-height:1.7}}'''
src=(root/'README.md').read_text()
src=re.sub(r'(<summary>.*?</summary>)(.*?)(</details>)',lambda m:m[1]+'\n'+markdown.markdown(m[2],extensions=['extra'])+'\n'+m[3],src,flags=re.S)
body=markdown.markdown(src,extensions=['extra','toc'])
shutil.copytree(root/'assets',preview/'assets',dirs_exist_ok=True)
for name,theme in [('index',''),('dark','dark')]:
 html='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Deng Yulin · GitHub profile</title><style>'+css+'</style><body class="'+theme+'"><div class="note"><span>GitHub-style preview · approximate layout, native UI colors</span><span><a href="/">Light</a> · <a href="/dark.html">Dark</a></span></div><article>'+body+'</article></body></html>'
 (preview/(name+'.html')).write_text(html)
print(preview)
