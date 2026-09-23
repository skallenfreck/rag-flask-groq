# Academic AI - RAG Flask + Groq

Aplicación web de consulta académica basada en RAG (Retrieval-Augmented Generation).

El sistema permite realizar preguntas sobre documentos PDF y generar respuestas utilizando búsqueda semántica con ChromaDB, embeddings con Sentence Transformers y un modelo de lenguaje de Groq.

## Tecnologías

- Python 3.13
- Flask
- LangChain
- ChromaDB
- Sentence Transformers
- Groq
- PyPDF
- HTML
- CSS
- JavaScript

---

# Instalación y ejecución

## 1. Clonar el repositorio

Abrir una terminal y ejecutar:

https://github.com/skallenfreck/rag-flask-groq.git

Entrar al proyecto:

cd rag-flask-groq

---

## 2. Verificar Python

El proyecto utiliza Python 3.13.

En Windows:

py --version

Si Python 3.13 está instalado, debe aparecer algo similar a:

Python 3.13.x

---

## 3. Crear el entorno virtual

Desde la carpeta del proyecto ejecutar:

py -3.13 -m venv .venv

Esto crea un entorno virtual independiente para el proyecto.

---

## 4. Activar el entorno virtual

En PowerShell:

.venv\Scripts\Activate.ps1

En CMD:

.venv\Scripts\activate

Cuando se active correctamente aparecerá (.venv) al inicio de la terminal.

---

## 5. Instalar las dependencias

Con el entorno virtual activado:

pip install -r requirements.txt

Esto instala todas las librerías necesarias para ejecutar el proyecto.

---

## 6. Configurar la API Key de Groq

En la raíz del proyecto crear un archivo llamado:

.env

El archivo debe estar al mismo nivel que run.py.

Agregar:

GROQ_API_KEY=TU_API_KEY

Reemplazar TU_API_KEY por una API Key válida de Groq.

No compartir la API Key ni subir el archivo .env a GitHub.

---

## 7. Ejecutar la aplicación

Con el entorno virtual activado:

python run.py

Si todo funciona correctamente, Flask mostrará:

Running on http://127.0.0.1:5000

Abrir el navegador y entrar a:

http://127.0.0.1:5000

La aplicación mostrará la interfaz de Academic AI.

---

# Documentos

Los documentos utilizados por el sistema se encuentran en:

data/documents/

Actualmente el proyecto incluye el Reglamento Académico Institucional.

Para agregar nuevos documentos, colocar los archivos PDF dentro de esta carpeta.

Cuando no existe una base vectorial previamente creada, el sistema:

1. Carga los documentos PDF.
2. Divide los documentos en fragmentos.
3. Genera los embeddings.
4. Crea la base vectorial.
5. Indexa los fragmentos.
6. Permite realizar consultas sobre los documentos.

La base vectorial se almacena localmente en:

storage/chroma/

Esta carpeta se genera automáticamente.

---

# Funcionamiento del RAG

El flujo principal del sistema es:

Documento PDF
      ↓
Carga del documento
      ↓
División en fragmentos
      ↓
Embeddings
      ↓
ChromaDB
      ↓
Pregunta del usuario
      ↓
Recuperación de fragmentos relevantes
      ↓
Prompt
      ↓
Groq
      ↓
Respuesta
      ↓
Fuentes utilizadas

La aplicación muestra la respuesta generada junto con las páginas del documento utilizadas como fuente.

---

# Estructura del proyecto

rag-flask-groq/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   ├── splitter.py
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   ├── prompt.py
│   │   ├── llm.py
│   │   └── pipeline.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       ├── css/
│       │   └── style.css
│       │
│       └── js/
│           └── app.js
│
├── data/
│   └── documents/
│       └── Acuerdo-No.-01-de-2025-Reglamento-Academico-Institucional.pdf
│
├── storage/
│   └── chroma/
│
├── .env
├── .env.example
├── .gitignore
├── config.py
├── requirements.txt
├── run.py
├── test_rag.py
└── README.md

---

# Prueba del RAG

El proyecto incluye test_rag.py, que permite probar directamente el pipeline RAG sin utilizar la interfaz web.

Con el entorno virtual activado ejecutar:

python test_rag.py

El sistema realizará una consulta y mostrará la respuesta junto con las fuentes recuperadas.

---

# Git

Para clonar el proyecto:

git clone URL_DEL_REPOSITORIO
cd rag-flask-groq

Para obtener los últimos cambios:

git pull origin main

Para guardar cambios:

git add .
git commit -m "Descripción del cambio"
git push origin main

---

# Notas importantes

- Se requiere Python 3.13.
- Se requiere una API Key válida de Groq.
- El archivo .env no debe subirse al repositorio.
- El entorno virtual .venv no debe subirse al repositorio.
- La base vectorial de ChromaDB se genera localmente.
- Los documentos PDF utilizados por el RAG se encuentran en data/documents/.
