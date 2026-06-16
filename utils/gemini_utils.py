import google.generativeai as genai
from dotenv import load_dotenv
import os


def configure_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.5-flash")



def generate_notes(model,text):

    prompt = f"""
    Create professional study notes from the transcript.

    Include:
    1. Title
    2. Key Concepts
    3. Important Points
    4. Summary
    5. Exam Notes

    Transcript:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text


def generate_quiz(model,text, quiz_questions):

    prompt = f"""
    Create EXACTLY {quiz_questions} MCQs.

    Rules:
    -The total number of questions must be {quiz_questions}.
    -Do not stop early.
    -Do not generate more than {quiz_questions}.
    - Generate exactly {quiz_questions} questions.
    - Put every option on a NEW LINE.
    - Use format:

    Q1. Question

    A) Option A
    B) Option B
    C) Option C
    D) Option D

    Correct Answer: A

    Transcript:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text


def generate_flashcards(model,text,flashcard_count):

    prompt = f"""
    Create EXACTLY {flashcard_count} flashcards.
    The total number of flashcards must be {flashcard_count}.
    Do not stop early.
    Do not generate more than {flashcard_count}.

    Format:

    Flashcard 1
    Q: Question
    A: Answer

    Flashcard 2
    Q: Question
    A: Answer

    Transcript:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text


def ask_question(model,transcript, question):

    prompt = f"""
    Answer ONLY using the lecture transcript.

    If the answer is not present, reply:
    'The information is not available in the lecture.'

    Transcript:
    {transcript}

    Question:
    {question}
    """

    response = model.generate_content(prompt)
    return response.text
