from fastapi import FastAPI, Depends, Body, status, Header
from starlette.middleware.cors import CORSMiddleware
import database
from scheme import InterviewStartReq
from sqlalchemy.orm import Session
from util import jwt_util
import crud
import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
async def start_interview(Authorization: str | None = Header(default=None), db: Session = Depends(get_db)):
    email = jwt_util.decode_jwt(access_token=Authorization)
    account = crud.find_account_by_email(db=db, email=email)
    return ""


# , req: InterviewStartReq, db: Session = Depends(get_db)

@app.post("/interview/answer")
async def answer_interview():
    return ""


@app.get("/interview/{interview_id}")
async def get_interview_result():
    return ""
