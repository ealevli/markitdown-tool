import os
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from markitdown import MarkItDown

app = FastAPI(title="DocToMark")

STATIC_DIR = Path(__file__).parent / "static"
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB


def _build_response(markdown_text: str, filename: str) -> dict:
    return {
        "markdown": markdown_text,
        "filename": filename,
        "token_estimate": len(markdown_text) // 4,
        "char_count": len(markdown_text),
    }


@app.get("/")
async def landing():
    return FileResponse(STATIC_DIR / "landing.html")


@app.get("/app")
async def app_page():
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/convert")
async def convert(file: UploadFile = File(...)):
    suffix = Path(file.filename).suffix if file.filename else ""
    tmp_path = None
    try:
        content = await file.read()
        if len(content) > MAX_FILE_SIZE:
            raise HTTPException(status_code=413, detail=f"File too large. Maximum allowed size is {MAX_FILE_SIZE // (1024*1024)} MB.")

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp_path = tmp.name
            tmp.write(content)

        md = MarkItDown()
        result = md.convert(tmp_path)
        return JSONResponse(_build_response(result.text_content or "", file.filename or "unknown"))
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.unlink(tmp_path)


@app.post("/convert-url")
async def convert_url(request: Request):
    body = await request.json()
    url = (body.get("url") or "").strip()
    if not url:
        raise HTTPException(status_code=400, detail="No URL provided.")
    if not url.startswith(("http://", "https://")):
        raise HTTPException(status_code=400, detail="URL must start with http:// or https://")

    try:
        md = MarkItDown()
        result = md.convert(url)
        filename = url.split("/")[-1].split("?")[0] or "page"
        if "." not in filename:
            filename = filename + ".html"
        return JSONResponse(_build_response(result.text_content or "", filename))
    except Exception as exc:
        raise HTTPException(status_code=422, detail=str(exc))
