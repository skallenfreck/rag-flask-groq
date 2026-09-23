def get_retriever(vector_store, k: int = 5):
    """
    Crea el recuperador que busca los fragmentos
    más relevantes para una pregunta.
    """

    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )