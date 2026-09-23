from langchain_groq import ChatGroq

from config import GROQ_API_KEY


GROQ_MODEL = "openai/gpt-oss-120b"


def get_llm():
    """
    Crea el modelo de lenguaje que generará
    la respuesta final del RAG.
    """

    return ChatGroq(
        model=GROQ_MODEL,
        temperature=0.0,
        api_key=GROQ_API_KEY
    )