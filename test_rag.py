from app.rag.pipeline import RAGPipeline


rag = RAGPipeline()

question = "¿Cuál es el objetivo del Reglamento Académico Institucional?"

result = rag.ask(question)

print("\n" + "=" * 60)
print("RESPUESTA")
print("=" * 60)

print(result["answer"])

print("\n" + "=" * 60)
print("FUENTES")
print("=" * 60)

for source in result["sources"]:
    print(
        f"- {source['source']} "
        f"(Página {source['page']})"
    )