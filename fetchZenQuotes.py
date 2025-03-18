import requests
import time
from codecarbon import EmissionsTracker

# URL de la API de ZenQuotes
ZEN_QUOTES_API_URL = "https://zenquotes.io/api/random"

# URL de la aplicación FastAPI
FASTAPI_URL = "http://127.0.0.1:8000/quote"

# Lista de sentimientos para enviar en las peticiones
sentimientos = ["feliz", "triste", "enojado", "ansioso", "emocionado"]

def fetch_quote():
    try:
        # Realiza la solicitud GET a la API de ZenQuotes
        response = requests.get(ZEN_QUOTES_API_URL)
        response.raise_for_status()  # Lanza una excepción si ocurre un error
        data = response.json()

        # Extrae la cita y el autor del JSON devuelto
        quote = data[0]["q"]
        author = data[0]["a"]

        # Muestra la cita
        print(f"\n\"{quote}\"")
        print(f"- {author}\n")

    except requests.exceptions.RequestException as e:
        print("Error al obtener la cita:", e)

def simulate_requests():
    # Duración de la simulación en segundos
    duracion = 60
    # Intervalo entre peticiones en segundos
    intervalo = 0.1

    # Tiempo de inicio
    start_time = time.time()

    while time.time() - start_time < duracion:
        for sentimiento in sentimientos:
            try:
                response = requests.get(FASTAPI_URL, params={"feeling": sentimiento})
                print(f"Sentimiento: {sentimiento}, Respuesta: {response.json()}")
            except Exception as e:
                print(f"Error al enviar la petición: {e}")
            time.sleep(intervalo)

# Ejecuta la función principal
if __name__ == "__main__":
    print("Inspirational Quotes (powered by ZenQuotes)")
    tracker = EmissionsTracker()
    tracker.start()
    try:
        while True:
            fetch_quote()
            # Pregunta al usuario si quiere otra cita
            more = input("¿Quieres otra cita? (s/n): ").strip().lower()
            if more != 's':
                break
        print("¡Gracias por usar el programa!")

        # Simula el envío de peticiones a la aplicación FastAPI
        print("Simulando el envío de peticiones a la aplicación FastAPI...")
        simulate_requests()
        print("Simulación completada.")
    finally:
        tracker.stop()
