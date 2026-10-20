
import requests

URL = "http://192.168.168.34:8080/api/chat/completions"
MODEL = "google/gemma-4-E4B-it"

API_KEY = "sk-cbc81e8c928647b3ba6f220695c0dbcf"

PROMPT = """
És a inteligência artificial de um robô de assistência.
Responde em inglês, de forma simples, clara e breve.
O utilizador comunica contigo por voz.
"""

with open("transcription.txt", "r", encoding="utf-8") as file:
    texto = file.read().strip()

if not texto:
    print("Nenhum texto reconhecido.")
    raise SystemExit

resposta = requests.post(URL, headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": MODEL,
        "messages": [
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": texto}
        ],
        "temperature": 0
    },
    timeout=120
)

resposta.raise_for_status()
print(resposta.json()["choices"][0]["message"]["content"])