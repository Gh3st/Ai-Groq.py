import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Verifica se a chave está presente
if not api_key:
    st.error("A chave da API da Groq não foi encontrada no arquivo .env")
    st.stop()

# Inicializa o cliente da Groq
client = Groq(api_key=api_key)

# Configuração da página
st.set_page_config(page_title="Chat com Groq", page_icon="🤖")
st.title("🤖 Chat com Groq AI")

# Inicializa o histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Caixa de entrada do usuário
prompt = st.chat_input("Digite sua pergunta:")

if prompt:
    # Adiciona mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Exibe mensagem do usuário
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Gera resposta da IA
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                # Prepara mensagens para a API
                messages_for_api = []
                for msg in st.session_state.messages:
                    messages_for_api.append({"role": msg["role"], "content": msg["content"]})
                
                # Chama a API da Groq com modelo FUNCIONANDO
                chat_completion = client.chat.completions.create(
                    messages=messages_for_api,
                    model="llama3-8b-8192",  # MODELO QUE FUNCIONA!
                    temperature=0.7,
                    max_tokens=1024
                )
                
                # Extrai a resposta
                resposta = chat_completion.choices[0].message.content
                
                # Exibe a resposta
                st.markdown(resposta)
                
                # Adiciona resposta ao histórico
                st.session_state.messages.append({"role": "assistant", "content": resposta})
                
            except Exception as e:
                st.error(f"Erro ao conectar com a API: {e}")

# Sidebar com informações
with st.sidebar:
    st.subheader("ℹ️ Informações")
    st.write(f"Total de mensagens: {len(st.session_state.messages)}")
    
    if st.button("🗑️ Limpar Conversa"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("**Modelo:** Llama 3 8B")
    st.markdown("**Provider:** Groq")
    st.success("✅ Usando modelo atualizado!")