
from docx import settings
from pathlib import Path
from app.core.config import get_settings
from pydantic_settings import BaseSettings, SettingsConfigDict
from app.services.ingestion import load_file, chunk_documents


settings = get_settings()
from app.services.ingestion import load_file, chunk_documents
from pathlib import Path
#doc=load_file(Path("data/School_Kb/sri.pdf"))
doc=load_file(Path(settings.sample_kb_dir) / "sri.pdf")
print(len(doc))

