from pydantic import BaseModel
from datetime import datetime

from typing import List


class InterviewStartReq(BaseModel):
    categories: List[str] = []


class AdditionalInterviewReq(BaseModel):
    sequence: int  # 1, 2, 3
    question_id: int
    answer: str
