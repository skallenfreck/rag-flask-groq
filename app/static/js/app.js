const form = document.getElementById("question-form");
const input = document.getElementById("question");
const messages = document.getElementById("messages");
const sendButton = document.getElementById("send-button");


/*
 * Convierte Markdown básico en HTML.
 *
 * Actualmente soportamos:
 * **texto**  → negrita
 * saltos de línea
 */
function formatAnswer(text) {

    /*
     * Escapamos HTML para evitar que el contenido
     * generado por el modelo pueda interpretarse
     * como código HTML.
     */
    const escaped = text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");


    /*
     * Convertir **texto** en negrita.
     */
    const boldText = escaped.replace(
        /\*\*(.*?)\*\*/g,
        "<strong>$1</strong>"
    );


    /*
     * Mantener los saltos de línea.
     */
    return boldText.replace(/\n/g, "<br>");
}


/*
 * Agrega un mensaje al chat.
 */
function addMessage(type, content, sources = []) {

    const message = document.createElement("div");

    message.className = `message ${type}`;


    const avatar = document.createElement("div");

    avatar.className = "avatar";

    avatar.textContent =
        type === "user" ? "TÚ" : "AI";


    const body = document.createElement("div");

    body.className = "message-body";


    const name = document.createElement("div");

    name.className = "message-name";

    name.textContent =
        type === "user"
            ? "Tú"
            : "Academic AI";


    const messageContent = document.createElement("div");

    messageContent.className = "message-content";


    /*
     * Las preguntas del usuario se muestran
     * como texto normal.
     */
    if (type === "user") {

        messageContent.textContent = content;

    }

    /*
     * Las respuestas del RAG pueden contener
     * Markdown básico.
     */
    else {

        messageContent.innerHTML =
            formatAnswer(content);

    }


    body.appendChild(name);

    body.appendChild(messageContent);


    /*
     * Eliminar fuentes duplicadas.
     */
    const uniqueSources = [];

    const sourceKeys = new Set();


    sources.forEach(source => {

        const key =
            `${source.source}-${source.page}`;

        if (!sourceKeys.has(key)) {

            sourceKeys.add(key);

            uniqueSources.push(source);

        }

    });


    /*
     * Mostrar fuentes.
     */
    if (uniqueSources.length > 0) {

        const sourcesTitle =
            document.createElement("div");

        sourcesTitle.className =
            "sources-title";

        sourcesTitle.textContent =
            "Fuentes consultadas";


        const sourcesContainer =
            document.createElement("div");

        sourcesContainer.className =
            "sources";


        uniqueSources.forEach(source => {

            const sourceElement =
                document.createElement("div");

            sourceElement.className =
                "source";


            const shortName =
                source.source
                    .replace(".pdf", "")
                    .replace(
                        "Acuerdo-No.-01-de-2025-Reglamento-Academico-Institucional",
                        "Reglamento Académico"
                    );


            sourceElement.innerHTML = `
                <span class="source-icon">📄</span>

                <span>${shortName}</span>

                <span class="source-page">
                    Página ${source.page}
                </span>
            `;

            sourcesContainer.appendChild(
                sourceElement
            );

        });


        body.appendChild(sourcesTitle);

        body.appendChild(sourcesContainer);

    }


    message.appendChild(avatar);

    message.appendChild(body);

    messages.appendChild(message);


    /*
     * Llevar el chat al último mensaje.
     */
    messages.scrollTop =
        messages.scrollHeight;
}


/*
 * Muestra el indicador de carga.
 */
function showLoading() {

    const loading =
        document.createElement("div");

    loading.className =
        "message assistant";

    loading.id =
        "loading-message";


    loading.innerHTML = `
        <div class="avatar">AI</div>

        <div class="message-body">

            <div class="message-name">
                Academic AI
            </div>

            <div class="message-content loading-content">
                <span class="loading-dot"></span>
                <span class="loading-dot"></span>
                <span class="loading-dot"></span>

                <span class="loading-text">
                    Consultando el reglamento...
                </span>
            </div>

        </div>
    `;


    messages.appendChild(loading);

    messages.scrollTop =
        messages.scrollHeight;
}


/*
 * Elimina el indicador de carga.
 */
function hideLoading() {

    const loading =
        document.getElementById(
            "loading-message"
        );

    if (loading) {

        loading.remove();

    }
}


/*
 * Enviar pregunta.
 */
form.addEventListener(
    "submit",
    async (event) => {

        event.preventDefault();


        const question =
            input.value.trim();


        if (!question) {

            return;

        }


        /*
         * Mostrar pregunta.
         */
        addMessage(
            "user",
            question
        );


        /*
         * Limpiar campo.
         */
        input.value = "";


        /*
         * Bloquear formulario durante
         * la consulta.
         */
        sendButton.disabled = true;

        input.disabled = true;


        showLoading();


        try {

            /*
             * Enviar pregunta a Flask.
             */
            const response =
                await fetch("/ask", {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        question: question
                    })

                });


            const data =
                await response.json();


            hideLoading();


            /*
             * Error del servidor.
             */
            if (!response.ok) {

                addMessage(
                    "assistant",
                    data.error ||
                    "Ocurrió un error al procesar la pregunta."
                );

                return;

            }


            /*
             * Mostrar respuesta.
             */
            addMessage(
                "assistant",
                data.answer,
                data.sources || []
            );


        }

        catch (error) {

            hideLoading();


            addMessage(
                "assistant",
                "No fue posible comunicarse con el servidor."
            );


            console.error(error);

        }

        finally {

            /*
             * Reactivar formulario.
             */
            sendButton.disabled = false;

            input.disabled = false;

            input.focus();

        }

    }
);