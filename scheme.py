from pydantic import BaseModel
from datetime import datetime


class InterviewStartReq(BaseModel):
    categories: list
