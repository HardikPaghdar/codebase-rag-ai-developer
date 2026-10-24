# Codebase RAG AI Developer

Local-first codebase retrieval demo: line-aware source chunks, lexical ranking and file citations. It returns evidence rather than pretending an LLM answer was generated. Embeddings/vector storage/LLM synthesis are roadmap items.

Run: `pip install -r requirements.txt`; `python -m codebase_rag.cli ask "customer validation" --path examples/sample_repo`; `pytest`.

The local API accepts filesystem paths: keep it on localhost and add authentication/path allowlists before deployment. Index only repositories you are authorized to inspect.
