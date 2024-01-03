# QCARD-ai

### 실행 명령어
```bash
uvicorn main:app --reload
```

```bash
gunicorn main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --access-logfile ./log.log
```ㄹ