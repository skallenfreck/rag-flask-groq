from pathlib import Path

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.embeddings import get_embeddings
from app.rag.vector_store import (
    create_vector_store,
    load_vector_store
)
from app.rag.retriever import get_retriever
from app.rag.prompt import get_prompt
from app.rag.llm import get_llm


DOCUMENTS_PATH = "data/documents"
CHROMA_PATH = "storage/chroma"


class RAGPipeline:
    def __init__(self):
        self.embeddings = get_embeddings()
        self.prompt = get_prompt()
        self.llm = get_llm()

        if Path(CHROMA_PATH).exists() and any(Path(CHROMA_PATH).iterdir()):
            print("[INFO] Cargando ChromaDB existente...")
            self.vector_store = load_vector_store(
                self.embeddings,
                CHROMA_PATH
            )
        else:
            print("[INFO] Creando ChromaDB...")

            documents = load_documents(DOCUMENTS_PATH)
            chunks = split_documents(documents)

            self.vector_store = create_vector_store(
                chunks,
                self.embeddings,
                CHROMA_PATH
            )

        self.retriever = get_retriever(
            self.vector_store,
            k=5
        )

        print("[OK] RAG Pipeline listo")

    def ask(self, question: str) -> dict:
        """
        Ejecuta el flujo completo:
        pregunta → retrieval → contexto → prompt → LLM.
        """

        documents = self.retriever.invoke(question)

        context = "\n\n---\n\n".join(
            f"[Fuente: {Path(doc.metadata.get('source', '?')).name} "
            f"— Página: {doc.metadata.get('page', '?') + 1}]\n"
            f"{doc.page_content}"
            for doc in documents
        )

        prompt = self.prompt.invoke({
            "context": context,
            "question": question
        })

        response = self.llm.invoke(prompt)

        sources = [
            {
                "source": Path(
                    doc.metadata.get("source", "?")
                ).name,
                "page": doc.metadata.get("page", 0) + 1
            }
            for doc in documents
        ]

        return {
            "question": question,
            "answer": response.content,
            "sources": sources
        }