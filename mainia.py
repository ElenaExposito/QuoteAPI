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

# Ejemplo de uso
sentimiento = "feliz"
resultado = obtener_cita(sentimiento)
print(resultado)
