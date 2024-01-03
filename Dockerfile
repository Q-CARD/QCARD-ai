FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

# 파일 복사
COPY . .

# 파이썬 라이브러리 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
