from pathlib import Path
from app.core.config import get_settings
from app.services.ingestion import load_file, chunk_documents
from app.rag.vectorstore import add_documents

settings = get_settings()

folder = Path(settings.sample_kb_dir)



# Get files only (skip subdirectories)
files = [p for p in folder.iterdir() if p.is_file()]

if not files:
    print(f"No files found in: {folder}")

all_docs = []

for path in files:
    print(f"Loading: {path.name}")
    all_docs.extend(load_file(path))

chunks = chunk_documents(all_docs)
ids = add_documents(chunks)

print(
    f"Indexed {len(files)} files -> "
    f"{len(chunks)} chunks -> "
    f"{len(ids)} Pinecone vectors"
)