# Codebase RAG AI Developer

Local codebase retrieval demo with line-aware chunks, lexical ranking and file citations. It returns evidence, not fabricated LLM answers. Embeddings/vector DB/LLM synthesis are future adapters.

Run: `pip install -r requirements.txt`; `python -m codebase_rag.cli "customer validation" examples/sample_repo`; `pytest`.

The local API accepts filesystem paths: keep localhost-only and add authentication/path allowlists before deployment.
