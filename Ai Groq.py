from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",  # Endpoint da Groq
    api_key="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"            # Substitua pela sua chave
)

response = client.chat.completions.create(
    model="llama3-8b-8192",  # Pode usar também llama3-70b-8192
    messages=[
        {"role": "user", "content": "Me explique o que é buraco negro."}
    ]
)

print(response.choices[0].message.content)
