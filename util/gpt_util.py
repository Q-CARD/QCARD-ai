import openai
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, "../.env"))
openai.api_key = os.environ.get("GPT_KEY")


def get_gpt_answer(question, prompt, model="gpt-3.5-turbo-0613"):
    content = "나는 " + question + "이라는 질문에 대해 나는 " + prompt + " 라고 답변했어." + "이 질문에 대한 답변과, 내가 한 답변에 대한 내용적인 첨삭을 받고 싶어. " \
                                                                           "나는 면접 준비중이야."
    messages = [{"role": "assistant", "content": content}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message["content"]


def get_gpt_questions(question, answer, model="gpt-3.5-turbo-0613"):
    content = "나는 " + question + "이라는 질문에 대해 나는 " + answer + " 라고 답변했어." \
              + "네가 면접관이라면, 나에게 할 추가 질문을 3개 줘." \
            + "json 형식으로, {'question_1':"", 'question_2':"", 'question_3':""}로 응답해줘."
    messages = [{"role": "assistant", "content": content}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message["content"]
