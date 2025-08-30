import streamlit as st
import requests
import json

API_URL = "https://SEU-SERVICO.onrender.com/odds"  # troque pela URL do Render

st.set_page_config(page_title="Comparador de Odds – Escanteios", layout="wide")

st.title("Comparador de Odds – Escanteios (API)")
st.caption("Cole as URLs do MESMO jogo nas 3 casas e clique em Atualizar")

col1, col2, col3 = st.columns(3)
with col1:
    betano = st.text_input("URL Betano", placeholder="https://www.betano.bet.br/live/...")
with col2:
    bet365 = st.text_input("URL Bet365", placeholder="https://www.bet365.bet.br/#/IP/EV...")
with col3:
    kto = st.text_input("URL KTO", placeholder="https://www.kto.bet.br/esportes-ao-vivo/...")

market = st.selectbox("Mercado", ["9.5", "8.5", "10.5", "11.5"], index=0)

if st.button("Atualizar Odds"):
    payload = {
        "market": market,
        "betano": betano.strip(),
        "bet365": bet365.strip(),
        "kto": kto.strip()
    }
    try:
        r = requests.post(API_URL, headers={"Content-Type":"application/json"}, data=json.dumps(payload), timeout=60)
        r.raise_for_status()
        data = r.json()
        st.json(data)
    except requests.RequestException as e:
        st.error(f"Erro ao consultar a API: {e}")
