from langchain_huggingface import HuggingFaceEmbeddings


EMBEDDING_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"


def get_embeddings():
    """
    Crea el modelo de embeddings que se ejecuta localmente.
    """

    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )