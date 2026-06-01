# pip install -r requirements.txt
# uvicorn main:app --reload --port 8000
# Then open http://localhost:8000

import os
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from markitdown import MarkItDown

app = FastAPI(title="MarkItDown Tool")

STATIC_DIR = Path(__file__).parent / "static"


@app.get("/")
async def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/convert")
async def convert(file: UploadFile = File(...)):
    suffix = Path(file.filename).suffix if file.filename else ""
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp_path = tmp.name
            content = await file.read()
            tmp.write(content)

        md = MarkItDown()
        result = md.convert(tmp_path)
        markdown_text = result.text_content or ""

        return JSONResponse({
            "markdown": markdown_text,
            "filename": file.filename or "unknown",
            "token_estimate": len(markdown_text) // 4,
            "char_count": len(markdown_text),
        })
    except Exception as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.unlink(tmp_path)
