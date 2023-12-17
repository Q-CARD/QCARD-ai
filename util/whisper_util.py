import openai
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, "../.env"))
openai.api_key = os.environ.get("GPT_KEY")


def translate_answer_audio(file):
    audio_file = open(file, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    text = transcript['text']
    return text


def translate_answer_audio_socket(file):
    transcript = openai.Audio.transcribe("whisper-1", file)
    text = transcript['text']
    return text
