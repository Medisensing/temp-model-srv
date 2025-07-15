from fastapi import FastAPI, Query, Header, HTTPException
from fastapi.responses import PlainTextResponse
from pathlib import Path
import os, time, hmac, hashlib, base64
from fastapi.staticfiles import StaticFiles

# ───────── 내부 인증 값 (게이트웨이와 동일) ─────────

"""
    내부 네트워크 식별용 SECRET KEY 및 인증
    외부에서 모델관련 API 호출 시 차단.
"""
INTERNAL_SECRET = os.getenv("INTERNAL_SECRET", "dev_secret")

def verify_internal(auth: str | None):
    if not auth:
        raise HTTPException(403, "missing internal auth")
    try:
        ts_str, sig = auth.split(".")
        ts = int(ts_str)
        # 60초 유효
        if abs(time.time() - ts) > 60:
            raise ValueError
        expect = hmac.new(INTERNAL_SECRET.encode(), ts_str.encode(), hashlib.sha256).digest()
        if not hmac.compare_digest(expect, base64.urlsafe_b64decode(sig)):
            raise ValueError
    except Exception:
        raise HTTPException(403, "invalid internal auth")

# ───────── FastAPI 앱 ─────────
"""
    title 에 모델 이름을 설정합니다.
    API Document 의 위치와 파일명을 설정
"""
app = FastAPI(title="Template Model Service") 
DOC_PATH = Path(__file__).parent / "docs" / "api-docs.md"

# --------- Audio File Serve --------
"""
    Audio File을 Markdown 내 삽입하기위한 Route
"""
AUDIO_DIR = Path(__file__).parent / "static" / "audio"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/audio", StaticFiles(directory=AUDIO_DIR), name="audio")

# -------- DOCS Route Function --------
"""
    마크다운 서빙용 Route
    
    API DOCS 는 반드시 /app/docs/api-docs.md 에 위치.
    모델 사용 설명서 작성용 Route, 반드시 마크다운 형태로 작성해야 반영
    필요에 따라 HTML 태그 사용가능
"""
@app.get("/api-docs", response_class=PlainTextResponse)
def api_docs():
    """모델 사용 설명서(Markdown)"""
    return DOC_PATH.read_text(encoding="utf-8") if DOC_PATH.exists() else "SERVER_ERROR: api-docs.md not found"
