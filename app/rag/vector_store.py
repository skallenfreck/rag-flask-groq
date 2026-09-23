from pathlib import Path

from langchain_chroma import Chroma


COLLECTION_NAME = "reglamento_academico"


def create_vector_store(documents: list, embeddings, persist_directory: str):
    """
    Genera y almacena los embeddings de los documentos en ChromaDB.
    """

    Path(persist_directory).mkdir(parents=True, exist_ok=True)

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=persist_directory,
        collection_name=COLLECTION_NAME,
        collection_metadata={"hnsw:space": "cosine"}
    )

    print(f"[OK] ChromaDB creada en: {persist_directory}")
    print(f"[OK] Fragmentos indexados: {len(documents)}")

    return vector_store


def load_vector_store(embeddings, persist_directory: str):
    """
    Carga una base vectorial Chroma existente.
    """

    return Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings,
        collection_name=COLLECTION_NAME
    )