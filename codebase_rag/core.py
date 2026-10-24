from pathlib import Path
from collections import Counter
import math,re
EXT={'.py','.js','.ts','.tsx','.md','.txt','.json','.yaml','.yml','.sql'}
SKIP={'.git','.venv','venv','node_modules','dist','build','__pycache__'}
TOKEN=re.compile(r'[A-Za-z_][A-Za-z0-9_]{1,}')
def index(root,max_lines=40,overlap=6):
 b=Path(root).resolve()
 if not b.is_dir(): raise ValueError('Repository path is not a directory')
 if max_lines<1 or overlap<0 or overlap>=max_lines: raise ValueError('Invalid chunk configuration')
 out=[]
 for p in sorted(b.rglob('*')):
  if not p.is_file() or p.suffix.lower() not in EXT or any(x in SKIP for x in p.parts) or p.stat().st_size>1000000: continue
  lines=p.read_text(encoding='utf-8',errors='replace').splitlines()
  for start in range(0,len(lines),max_lines-overlap):
   part=lines[start:start+max_lines]
   if part: out.append({'path':p.relative_to(b).as_posix(),'start_line':start+1,'end_line':start+len(part),'text':'\\n'.join(part)})
 return out
def search(question,chunks,limit=5):
 q=Counter(t.lower() for t in TOKEN.findall(question)); docs=[Counter(t.lower() for t in TOKEN.findall(c['text'])) for c in chunks]; lengths=[sum(d.values()) for d in docs]; avg=sum(lengths)/max(1,len(lengths)); scored=[]
 for c,d,n in zip(chunks,docs,lengths):
  score=0
  for term,count in q.items():
   tf=d[term]
   if tf:
    df=sum(term in doc for doc in docs); idf=math.log(1+(len(chunks)-df+.5)/(df+.5)); score+=idf*tf*2.2/(tf+1.2*(.25+.75*n/max(avg,1)))*min(count,3)
  if score: scored.append((score,c))
 scored.sort(key=lambda x:(-x[0],x[1]['path'],x[1]['start_line']))
 return [{'score':round(s,4),'source':c['path']+':'+str(c['start_line'])+'-'+str(c['end_line']),**c} for s,c in scored[:limit]]
