# Document Extractor – Team Exercise

A collaborative coding exercise. Each person implements one extractor for a
different file format; together you build a tool that can read Word, PDF, and
PowerPoint documents and summarise them using Claude.

---

## Project structure

```
Team Exercise/
├── models.py            # Shared Document dataclass  (do not modify)
├── base_extractor.py    # Abstract base class         (do not modify)
│
├── word_extractor.py    # YOUR TASK if you own .docx
├── pdf_extractor.py     # YOUR TASK if you own .pdf
├── ppt_extractor.py     # YOUR TASK if you own .pptx
│
├── llm_client.py        # Shared AI task – everyone contributes
├── main.py              # Entry point                 (do not modify)
│
├── tests/
│   ├── test_word_extractor.py
│   ├── test_pdf_extractor.py
│   └── test_ppt_extractor.py
│
├── requirements.txt
└── .gitignore
```

---

## Getting started

```bash
# 1. Clone the repository
git clone <repo-url>
cd team-exercise

# 2. Create a virtual environment and install dependencies
python -m venv .venv
.venv\Scripts\Activate.ps1      
pip install -r requirements.txt  # python -m pip install -r requirements.txt       

# 3. Set your Anthropic API key (needed for the LLM step)
export ANTHROPIC_API_KEY=sk-...  # Windows: set ANTHROPIC_API_KEY=sk-...
```

---

## Your tasks

### Step 1 – Implement your extractor

Open the file that matches your format (`word_extractor.py`, `pdf_extractor.py`,
or `ppt_extractor.py`). Read the TODO comment carefully — it lists the exact
steps and the library to use. Replace `raise NotImplementedError` with a working
implementation.

Run your extractor manually to see if it works:
```bash
python main.py path/to/your/sample.docx   # or .pdf / .pptx
```

### Step 2 – Make the tests pass

Open your test file in `tests/`. The first three tests are already written —
make sure they pass. Then complete the remaining TODO test that creates a real
file and checks the output.

```bash
pytest tests/test_word_extractor.py -v   # adjust filename for your format
```

### Step 3 – Implement the LLM summariser (shared task)

Open `llm_client.py` and implement the `summarise` function. Use the Anthropic
Python SDK. Run the full pipeline to see a summary printed in the terminal:

```bash
python main.py path/to/your/sample.docx
```

### Step 4 – Git workflow

Work on a feature branch, not directly on `main`:

```bash
git checkout -b feature/<your-name>-<format>   # e.g. feature/anna-pdf
# … make changes …
git add .
git commit -m "feat: implement PdfExtractor"
git push origin feature/<your-name>-<format>
```

Open a pull request against `main`. Review a teammate's PR before merging your
own.

---

## Stretch goals

Each extractor file lists stretch goals in its TODO comment. Some ideas that
span the whole project:

- Accept a `--question` flag in `main.py` and pass it through to `llm_client.summarise`.
- Add a `batch` command that processes every document in a folder.
- Stream the LLM response token-by-token instead of waiting for the full reply.
- Add type checking: run `mypy .` and fix all errors.

---

## Running all tests

```bash
pytest tests/ -v
```
