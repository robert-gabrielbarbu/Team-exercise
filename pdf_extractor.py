from pathlib import Path

from base_extractor import DocumentExtractor
from models import Document

class PdfExtractor(DocumentExtractor):
    """Extracts text and metadata from .pdf files."""

    @property
    def supported_extensions(self) -> list[str]:
        return [".pdf"]

    def extract(self, path: Path) -> Document:
        import pypdf

        #Open the PDF with `pypdf.PdfReader(path)`.
        try:
            reader = pypdf.PdfReader(path)
        except pypdf.errors.FileNotDecryptedError:
            #Handle encrypted PDFs gracefully (catch `pypdf.errors.FileNotDecryptedError`).
            return Document(
                source=path,
                title=path.stem,
                text="",
                metadata={"error": "encrypted PDF"},
            )

        #Iterate over `reader.pages` and call `page.extract_text()` on each.
        text = "\n".join(
            page.extract_text() or "" for page in reader.pages
        )

        #Read document metadata from `reader.metadata` (author, creation date, etc.).
        meta = reader.metadata or {}

        #Use the file stem as the title if no title is found in metadata.
        title = (meta.get("/Title") or "").strip() or path.stem

        #Store the page count in metadata
        metadata = {"page_count": len(reader.pages)}
        if meta.get("/Author"):
            metadata["author"] = meta["/Author"]
        if meta.get("/CreationDate"):
            metadata["creation_date"] = meta["/CreationDate"]

        #Return a Document instance
        return Document(source=path, title=title, text=text, metadata=metadata)
    
    # To execute run the following command 
    # python .\main.py C:\Sonia_GIT\AI\Team-exercise\PDF_NAME.pdf  
