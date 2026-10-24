import argparse,json
from .core import index,search
def main():
 p=argparse.ArgumentParser(); s=p.add_subparsers(dest='cmd',required=True); i=s.add_parser('index'); i.add_argument('path'); a=s.add_parser('ask'); a.add_argument('question'); a.add_argument('--path',default='examples/sample_repo'); a.add_argument('--limit',type=int,default=5); x=p.parse_args(); chunks=index(x.path if x.cmd=='index' else x.path)
 print(json.dumps({'chunks':len(chunks),'evidence':search(x.question,chunks,x.limit)} if x.cmd=='ask' else {'chunks':len(chunks),'files':len({c['path'] for c in chunks})},indent=2))
if __name__=='__main__': main()
