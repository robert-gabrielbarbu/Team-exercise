from pathlib import Path

from base_extractor import DocumentExtractor
from models import Document


class PdfExtractor(DocumentExtractor):
    """Extracts text and metadata from .pdf files."""

    @property
    def supported_extensions(self) -> list[str]:
        return [".pdf"]

    def extract(self, path: Path) -> Document:
        """TODO: Implement PDF extraction.

        Suggested library: pypdf
            pip install pypdf

        Steps to implement:
        1. Open the PDF with `pypdf.PdfReader(path)`.
        2. Iterate over `reader.pages` and call `page.extract_text()` on each.
        3. Join all page texts into a single string for `Document.text`.
        4. Read document metadata from `reader.metadata` (author, creation date, etc.).
        5. Use the file stem as the title if no title is found in metadata.
        6. Return a Document instance.

        Stretch goals:
        - Store the page count in metadata.
        - Handle encrypted PDFs gracefully (catch `pypdf.errors.FileNotDecryptedError`).
        """
        import pypdf

        if not path.exists():
            raise FileNotFoundError(f"No such file: {path}")
        reader = pypdf.PdfReader(path)
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        meta = reader.metadata
        title = (meta.title if meta and meta.title else path.stem)
        return Document(source=path, title=title, text=text, metadata=dict(meta or {}))
