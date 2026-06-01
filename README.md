# DocToMark

Convert any file to clean Markdown — instantly, in your browser.

> **Disclaimer:** DocToMark is an independent, open-source tool and is **not affiliated with or endorsed by Microsoft**. It uses the [Microsoft MarkItDown](https://github.com/microsoft/markitdown) library under the hood.

## What it does

Drop a file (or paste a URL) and get clean Markdown back in seconds. Useful for feeding documents into LLMs, writing pipelines, or just extracting text from messy formats.

**Supported formats:** PDF, Word (.docx), Excel (.xlsx), PowerPoint (.pptx), HTML, CSV, JSON, XML, PNG/JPG, ZIP, EPUB, MSG, WAV, MP3 and more.

## Features

- **Drag & drop or browse** — pick any supported file
- **URL conversion** — paste a public URL, get Markdown
- **Batch mode** — select multiple files, converted one by one
- **Download as .md** — saves with the original filename
- **Token estimate** — approximate LLM token count shown alongside char/line counts
- **50 MB limit** — checked client-side before upload
- **No storage** — files are deleted immediately after conversion

## Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) + [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- **Frontend:** Vanilla HTML/CSS/JS — zero dependencies

## Run locally

```bash
git clone https://github.com/your-username/markitdown-tool.git
cd markitdown-tool

python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt

uvicorn main:app --reload --port 8000
```

Then open [http://localhost:8000](http://localhost:8000).

## Deploy to Railway

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com)

1. Fork this repo
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Select your fork — Railway auto-detects the config and deploys

## Project structure

```
.
├── main.py              # FastAPI app — /convert and /convert-url endpoints
├── requirements.txt
├── railway.toml         # Railway deploy config
├── static/
│   ├── landing.html     # Marketing landing page (served at /)
│   └── index.html       # Conversion tool (served at /app)
└── start.sh / start.bat # Local quick-start scripts
```

## License

MIT
