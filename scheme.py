from pydantic import BaseModel
from datetime import datetime

from pydantic.decorator import List


class InterviewStartReq(BaseModel):
    categories: List[str] = []
