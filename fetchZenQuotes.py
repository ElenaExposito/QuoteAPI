import requests

# URL de la API de ZenQuotes
API_URL = "https://zenquotes.io/api/random"

def fetch_quote():
    try:
        # Realiza la solicitud GET a la API
        response = requests.get(API_URL)
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

# Ejecuta la función principal
if __name__ == "__main__":
    print("Inspirational Quotes (powered by ZenQuotes)")
    while True:
        fetch_quote()
        # Pregunta al usuario si quiere otra cita
        more = input("¿Quieres otra cita? (s/n): ").strip().lower()
        if more != 's':
            break
    print("¡Gracias por usar el programa!")
