import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from models import Document
from pdf_extractor import PdfExtractor


@pytest.fixture
def extractor() -> PdfExtractor:
    return PdfExtractor()


def test_supports_pdf(extractor: PdfExtractor) -> None:
    assert extractor.supports(Path("report.pdf"))


def test_does_not_support_docx(extractor: PdfExtractor) -> None:
    assert not extractor.supports(Path("report.docx"))


def test_raises_for_missing_file(extractor: PdfExtractor, tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        extractor.extract(tmp_path / "nonexistent.pdf")


def test_extract_real_pdf(extractor: PdfExtractor, tmp_path: Path) -> None:
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.cell(text="Hello world")
    p = tmp_path / "sample.pdf"
    pdf.output(str(p))

    result = extractor.extract(p)

    assert result.text.strip() != ""
    assert "Hello" in result.text
    assert result.title == "sample"
    assert result.word_count() > 0
