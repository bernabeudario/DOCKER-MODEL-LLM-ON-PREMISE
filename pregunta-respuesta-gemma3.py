import requests

response = requests.post(
    "http://localhost:12434/engines/llama.cpp/v1/chat/completions",
    json={
        "model": "ai/gemma3:4B-Q4_K_M",
        "messages": [
            {
                "role": "system",
                "content": "Eres un asistente útil, que responde en solo un párrafo y en español."
            },
            {
                "role": "user",
                "content": "Enumera con viñetas todos los países de America del Sur."   
            }
        ]
    }
)

if response.status_code == 200:
    print("Respuesta: ", response.json()["choices"][0]["message"]["content"])
else:
    print(f"Error en la solicitud: {response.status_code}, {response.text}")