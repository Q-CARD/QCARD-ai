import os
import shutil

from fastapi import FastAPI, Depends, Header, UploadFile
from starlette.middleware.cors import CORSMiddleware
import database
from scheme import InterviewStartReq
from sqlalchemy.orm import Session
from util import jwt_util, gpt_util, whisper_util
import crud

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "/tmp"


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/model")
async def root():
    return {"message": "Hello World"}


@app.post("/interview/start")
async def start_interview(req: InterviewStartReq, Authorization: str | None = Header(default=None),
                          db: Session = Depends(get_db)):
    account = crud.find_account_by_email(db=db, email=jwt_util.decode_jwt(access_token=Authorization))
    questions = []
    if len(req.categories) < 1:
        questions = crud.find_all_question(db=db)
    else:
        questions = crud.find_question_by_categories(db=db, categories=req.categories)
    interview, interview_question = crud.create_interview(db=db, account=account, questions=questions,
                                                          categories=req.categories)
    return {
        "interview_id": interview.id,
        "account": {
            "id": account.id,
            "name": account.name,
            "email": account.email
        },
        "question": crud.find_interview_questions(db=db, interview_questions=interview_question)
    }


@app.put("/interview/answer/{question_id}")
async def answer_interview(question_id: int, file: UploadFile, Authorization: str | None = Header(default=None),
                           db: Session = Depends(get_db)):
    # 계정 유효성 검증
    account = crud.find_account_by_email(db=db, email=jwt_util.decode_jwt(access_token=Authorization))

    # 파일 업로드
    filename = file.filename
    file_obj = file.file
    upload_name = os.path.join(UPLOAD_DIR, filename)
    upload_file = open(upload_name, 'wb+')
    shutil.copyfileobj(file_obj, upload_file)
    upload_file.close()

    # Whisper-api 호출
    answer = whisper_util.translate_answer_audio(file=upload_name)


    return account


@app.get("/interview/{interview_id}")
async def get_interview_result():
    return ""
