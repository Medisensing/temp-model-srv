FROM python:3.11-slim

# 비-root 유저 생성
RUN useradd -m appuser

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 설치 (root 권한)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 앱 복사 (root 권한으로 복사 후 권한 변경)
COPY app/ ./app

# appuser에게 소유권 부여
RUN chown -R appuser:appuser /app

# 포트 노출
EXPOSE 9000

# 권한 전환
USER appuser

# FastAPI 앱 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000"]
