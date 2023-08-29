from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/interview/start")
async def start_interview():
    return ""


@app.post("/interview/answer")
async def answer_interview():
    return ""


@app.get("/interview/{interview_id}")
async def get_interview_result():
    return ""
