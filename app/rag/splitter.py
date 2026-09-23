from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents: list) -> list:
    """
    Divide los documentos cargados en fragmentos pequeños
    para posteriormente generar embeddings.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", " "]
    )

    chunks = text_splitter.split_documents(documents)

    print(f"[OK] Documentos originales: {len(documents)}")
    print(f"[OK] Fragmentos generados: {len(chunks)}")

    return chunks