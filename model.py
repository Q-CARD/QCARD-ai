from sqlalchemy import Boolean, Column, ForeignKey, Date, DateTime, String, BigInteger
from sqlalchemy.orm import relationship

from database import Base


class Account(Base):
    __tablename__ = "account"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    email = Column(String)
    name = Column(String)


class Question(Base):
    __tablename__ = "question"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    category = Column(String)


class Answer(Base):
    __tablename__ = "answer"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    question = Column(BigInteger, ForeignKey("question.id"))
    content = Column(String)
    type = Column(String)


class Inteverview(Base):
    __tablename__ = "interview"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    account = Column(BigInteger, ForeignKey("account.id"))
    created_at = Column(DateTime)
    category_1 = Column(String)
    category_2 = Column(String)
    category_3 = Column(String)
    interview_account = relationship("Account", backref="interview_account")


class InterviewQuestion(Base):
    __tablename__ = "interview_question"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    interview = Column(BigInteger, ForeignKey("interview.id"))
    question = Column(BigInteger, ForeignKey("question.id"))
    answer = Column(String)
    gpt_answer = Column(String)
    additional_question_1 = Column(String)
    additional_answer_1 = Column(String)
    additional_question_2 = Column(String)
    additional_answer_2 = Column(String)
    additional_question_3 = Column(String)
    additional_answer_3 = Column(String)
    # interview_model = relationship("Interview", backref="interviewquestion_interview")
    question_model = relationship("Question", backref="question_model")
