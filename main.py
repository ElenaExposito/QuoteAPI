from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

from ollama import ChatResponse, chat

def obtener_cita(sentimiento: str) -> str:
    """
    Consulta a Ollama para obtener una cita basada en un sentimiento.
    Parámetros:
        sentimiento (str): Una palabra que describe cómo te sientes.
    Retorna:
        str: Una cita con su autor, o un mensaje de error si algo falla.
    """
    response: ChatResponse = chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': f"Dame solo una cita relacionada con sentirse {sentimiento} en el formato: 'Cita' - Autor. No añadas ningún otro texto."
        },
    ])
    return response.message.content

app = FastAPI()

@app.get("/quote")
def get_quote(feeling: str = Query(..., description="El sentimiento para buscar una cita")):
    try:
        cita = obtener_cita(feeling)
        return JSONResponse(content={"feeling": feeling, "quote": cita})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)