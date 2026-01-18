# ReAL: RAG-Enabled Active Learning

### Features
- Generate MCQ & fill-in-the-blank quizzes from lecture notes / PDFs
- RAG-powered citations with debug UI for inspecting retrieved chunks
- Ingest PDFs up to 50 pages
- Store quizzes and last 5 study sessions per user; documents themselves are not persisted to ensure privacy and reduce storage

### Stack
- Frontend: Next.js
- Backend: FastAPI
  - RAG Layer: BM25 lexical retrieval, optionally augmented with MiniLM embeddings for semantic similarity
- Database: SQLite (for quizzes & session metadata)