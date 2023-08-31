import datetime
import json

from sqlalchemy import or_

import scheme
from sqlalchemy.orm import Session, joinedload
from model import Account, Question, InterviewQuestion, Inteverview
import random


# account
def find_account_by_email(db: Session, email):
    db_account = db.query(Account).filter(email == Account.email)
    if db_account:
        for acc in db_account:
            return acc


# question
def find_all_question(db: Session):
    db_questions = db.query(Question).all()
    return random.sample(db_questions, 10)


def find_question_by_id(db: Session, question_id: int):
    return db.query(Question).get(question_id)


def find_question_by_categories(db: Session, categories: list):
    if len(categories) == 1:
        categories.append(None)
        categories.append(None)
    elif len(categories) == 2:
        categories.append(None)

    db_questions = db.query(Question).filter(or_(
        categories[0] == Question.category, categories[1] == Question.category, categories[2] == Question.category))
    return random.sample(list(db_questions), 10)


# interview
def create_interview(db: Session, categories: list, account: Account, questions: list):
    while len(categories) < 3:
        categories.append("")
    db_interview = Inteverview(
        account=account.id,
        created_at=datetime.datetime.now(),
        category_1=categories[0],
        category_2=categories[1],
        category_3=categories[2]
    )
    db.add(db_interview)
    db.commit()
    db.refresh(db_interview)

    db_interview_questions = []
    for i in range(len(questions)):
        db_interview_questions.append(InterviewQuestion(
            interview=db_interview.id,
            question=questions[i].id
        ))
    db.add_all(db_interview_questions)
    db.commit()
    for i in range(len(db_interview_questions)):
        db.refresh(db_interview_questions[i])
    return db_interview, db_interview_questions


def find_interview_questions(db: Session, interview_questions: list):
    res = []
    for i in range(len(interview_questions)):
        db_interview_question = db.query(InterviewQuestion).options(
            joinedload(InterviewQuestion.question_model)).filter(
            InterviewQuestion.question == interview_questions[i].question)
        res.append(list(db_interview_question)[0])
    return res


def find_question_by_interview_question(db: Session, interview_question_id: int):
    db_iq = db.query(InterviewQuestion).options(
        joinedload(InterviewQuestion.question_model)).filter(InterviewQuestion.id == interview_question_id)
    print(db_iq)
    iq = list(db_iq)[0]
    print(iq)
    print(iq.question_model.title)
    return iq.question_model.title


def update_interview_question(db: Session, iq_id: int, answer: str, gpt_answer: str, gpt_additional: str):
    gpt_additional = json.loads(gpt_additional.replace("'", "\""))
    db.query(InterviewQuestion).filter_by(id=iq_id).update({
        "answer": answer,
        "gpt_answer": gpt_answer,
        "additional_question_1": gpt_additional['question_1'],
        "additional_question_2": gpt_additional['question_2'],
        "additional_question_3": gpt_additional['question_3']
    })
    db.commit()


def find_interview(db: Session, interview_id: int):
    return db.query(InterviewQuestion).options(
        joinedload(InterviewQuestion.question_model)).filter(
        InterviewQuestion.interview == interview_id)


def update_interview_question_additional_answer(db: Session, sequence: int, question_id: int, answer: str):
    target = ""
    if sequence == 1:
        target = "additional_answer_1"
    elif sequence == 2:
        target = "additional_answer_2"
    elif sequence == 3:
        target = "additional_answer_3"
    db.query(InterviewQuestion).filter_by(id=question_id).update({
        target: answer
    })
    db.commit()


def find_interview_question_by_pk(db, iq_id: int):
    return list(db.query(InterviewQuestion).options(
        joinedload(InterviewQuestion.question_model)).filter(InterviewQuestion.id == iq_id))[0]
