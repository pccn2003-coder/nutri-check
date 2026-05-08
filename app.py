import streamlit as st
from datetime import datetime

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Nutri Check",
    page_icon="🥗",
    layout="centered"
)

# TÍTULO
st.title("🥗 Check-in Intestinal")

st.write("Responda rapidamente as perguntas do dia.")

st.divider()

# PERGUNTA 1
banheiro = st.radio(
    "Quantas vezes você foi ao banheiro hoje?",
    ["0", "1", "2", "3", "4 ou mais"]
)

st.divider()

# PERGUNTA 2
boiavam = st.radio(
    "As fezes boiavam?",
    ["Sim", "Não", "Não me lembro"]
)

st.divider()

# 🆕 PERGUNTA 3 - OBSERVAÇÕES
st.write("Observações do dia (opcional)")

observacoes = st.text_area(
    "Escreva aqui",
    max_chars=120,
    placeholder="Ex: Dor leve abdominal, alimentação normal..."
)

st.caption(f"{len(observacoes)}/120 caracteres")

st.divider()

# BOTÃO
if st.button("Salvar respostas"):

    dados = {
        "data": str(datetime.now()),
        "banheiro": banheiro,
        "boiavam": boiavam,
        "observacoes": observacoes
    }

    st.success("✅ Respostas salvas com sucesso!")

    st.write("Resumo do dia:")
    st.json(dados)