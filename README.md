# Codebase RAG AI Developer

Local-first codebase retrieval demo with source citations. It indexes source/docs, chunks by line range, ranks with BM25-style lexical scoring, and exposes CLI + FastAPI. This baseline returns evidence rather than claiming LLM-generated answers; embeddings and synthesis are roadmap items.

## Run
`pip install -r requirements.txt`
`python -m codebase_rag.cli ask "customer validation" --path examples/sample_repo`
`uvicorn codebase_rag.api:app --reload`
`pytest`

The API accepts local paths: keep it on localhost and add authentication/path allowlists before deployment. Index only repositories you are authorized to inspect.
