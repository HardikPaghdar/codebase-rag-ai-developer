from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from .core import index,search
app=FastAPI(title='Codebase RAG AI Developer'); chunks=[]
class IndexRequest(BaseModel): path:str=Field(min_length=1)
class AskRequest(BaseModel): question:str=Field(min_length=3); limit:int=Field(default=5,ge=1,le=10)
@app.get('/health')
def health(): return {'status':'ok','indexed':bool(chunks)}
@app.post('/index')
def do_index(r:IndexRequest):
 global chunks
 try: chunks=index(r.path)
 except ValueError as e: raise HTTPException(400,str(e))
 return {'chunk_count':len(chunks),'file_count':len({c['path'] for c in chunks})}
@app.post('/ask')
def ask(r:AskRequest): return {'question':r.question,'note':'Evidence retrieval only; no LLM answer synthesis.','evidence':search(r.question,chunks,r.limit)}
