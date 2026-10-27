# Codebase RAG AI Developer

Local-first codebase retrieval demo: line-aware source chunks, lexical ranking and file citations. It returns evidence rather than pretending an LLM answer was generated. Embeddings/vector storage/LLM synthesis are roadmap items.

Run: `pip install -r requirements.txt`; `python -m codebase_rag.cli ask "customer validation" --path examples/sample_repo`; `pytest`.

The local API accepts filesystem paths: keep it on localhost and add authentication/path allowlists before deployment. Index only repositories you are authorized to inspect.

## Explore more

- [MCP AI Developer Assistant](https://github.com/HardikPaghdar/mcp-ai-developer-assistant) — repository inspection tools.
- [Advanced Hybrid RAG with Reranking](https://github.com/HardikPaghdar/advanced-hybrid-rag-reranking) — retrieval and ranking.
- [Production RAG Pipeline](https://github.com/HardikPaghdar/production-rag-pipeline) — citations and evaluation.
- [More projects on my portfolio](https://hardikpaghdar.netlify.app/).
