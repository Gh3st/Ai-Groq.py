from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Pega a chave da variável de ambiente
api_key = os.getenv("GROQ_API_KEY")

# Usa a chave no client
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key
)

response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {"role": "user", "content": "Me explique o que é o buraco negro."}
    ]
)

print(response.choices[0].message.content)
