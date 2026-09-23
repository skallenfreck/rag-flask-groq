from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


def load_documents(documents_path: str) -> list:
    """
    Carga todos los archivos PDF de una carpeta.

    Cada página del PDF se convierte en un objeto Document
    que contiene el texto y sus metadatos.
    """

    documents = []
    pdf_path = Path(documents_path)

    for file in sorted(pdf_path.glob("*.pdf")):
        loader = PyPDFLoader(str(file))
        pages = loader.load()

        documents.extend(pages)

        print(f"[OK] {file.name}: {len(pages)} páginas cargadas")

    print(f"[OK] Total de páginas cargadas: {len(documents)}")

    return documents