#!/usr/bin/env python3
"""Offline content, assets, HTML link, WeChat style, and naming checks."""
from pathlib import Path
from urllib.parse import unquote
from html.parser import HTMLParser
import re, sys
root=Path(__file__).resolve().parents[1]
errors=[]
required=['README.md','GUIDE.md','index.html','article.html','wechat-article.html','docs/7-day-challenge.md','docs/sources.md','prompts/start-here.md','templates/README.md','docs/history.md','history.html','practice.html','prompts.html','sources.html','templates.html','LICENSE-CODE']
for name in required:
 if not (root/name).is_file():errors.append('Missing '+name)
for md in root.rglob('*.md'):
 body=md.read_text(encoding='utf-8')
 # Markdown links with local path targets only
 for href in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',body):
  href=href.strip().split('#')[0].split('?')[0]
  if not href or href.startswith(('http:','https:','mailto:','data:','//')):continue
  path=md.parent/unquote(href)
  if not path.exists():errors.append(str(md.relative_to(root))+' → missing '+href)
for page in ['index.html','article.html','wechat-article.html','history.html','practice.html','prompts.html','sources.html','templates.html']:
 body=(root/page).read_text(encoding='utf-8')
 for tag,href in re.findall(r'<(a|img|link|script)\b[^>]*(?:href|src)=[\"\']([^\"\']+)',body):
  if href.startswith(('http:','https:','mailto:','#','data:','//')):continue
  path=root/unquote(href.split('#',1)[0].split('?',1)[0])
  if not path.exists():errors.append(page+' → missing '+href)
 if re.search(r'text-align\s*:\s*(?:start|end)\b',body,re.I):errors.append('Nonstandard alignment '+page)
 if '<script' in body and page in ('article.html','wechat-article.html'):errors.append('unexpected script in article '+page)
assertname=(root/'README.md').read_text('utf-8')
if not assertname.startswith('# 孙学实操攻略'):errors.append('README title mismatch')
if not (root/'GUIDE.md').read_text('utf-8').startswith('# 我把孙宇晨'):errors.append('Guide headline mismatch')
for token in ['探图','黄毛理论','Small Ego','七天','GPT','邵艾伦']:
 if token not in (root/'GUIDE.md').read_text('utf-8'):errors.append('Guide missing '+token)
if '孙宇晨到底是一个什么样的人？孙学到底是啥？' not in (root/'GUIDE.md').read_text('utf-8'):errors.append('Author opening edited away')
if len(list((root/'prompts').glob('[0-9][0-9].md')))!=12:errors.append('12 expanded prompts not found')
if len(list(root.glob('assets/0[1-9]_*.png')))<9:errors.append('not enough editorial diagrams')
if (root/'assets/wechat-cover-900x383.png').exists():
 try:
  from PIL import Image
  if Image.open(root/'assets/wechat-cover-900x383.png').size!=(900,383):errors.append('WeChat cover wrong dimensions')
 except ImportError: pass
if '愿你的王国自由且富足' in (root/'README.md').read_text('utf-8'):errors.append('obsolete signature in README')
if errors:
 print('FAIL ('+str(len(errors))+')')
 for e in errors: print(' - '+e)
 sys.exit(1)
print('PASS: title, guide, images, internal links, HTML, prompts, cover, compatibility')
