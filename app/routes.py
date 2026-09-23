from flask import Blueprint, render_template, request, jsonify

from app.rag.pipeline import RAGPipeline


main = Blueprint("main", __name__)

# Inicializamos el RAG una sola vez
rag = RAGPipeline()


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    question = data.get("question", "").strip()

    if not question:
        return jsonify({
            "error": "La pregunta no puede estar vacía."
        }), 400

    try:
        result = rag.ask(question)

        return jsonify({
            "answer": result["answer"],
            "sources": result["sources"]
        })

    except Exception as e:
        return jsonify({
            "error": f"Ocurrió un error al procesar la pregunta: {str(e)}"
        }), 500