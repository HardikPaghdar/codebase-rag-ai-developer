# Architecture

Discovery filters common generated/vendor folders and supported extensions. Chunks preserve relative paths and line ranges. A BM25-style lexical ranker returns inspectable evidence; no LLM synthesis is included yet.

Next: add a labelled retrieval evaluation set, optional embeddings/vector storage, incremental content-hash indexing, and a provider adapter that must cite selected evidence. The local index endpoint accepts filesystem paths, so keep it localhost-only until authenticated and allowlisted.
