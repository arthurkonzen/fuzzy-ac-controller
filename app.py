import streamlit as st
from fuzzy_controller import compute_power

import csv
import os
from datetime import datetime
import pandas as pd


# ==========================
# FUNÇÃO DE LOG
# ==========================
def save_log(temp, hum, power):
    file_exists = os.path.isfile("logs.csv")

    with open("logs.csv", "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "temperatura", "umidade", "potencia"])

        writer.writerow([datetime.now(), temp, hum, power])


# ==========================
# CARREGAR LOGS
# ==========================
def load_logs():
    if os.path.isfile("logs.csv"):
        return pd.read_csv("logs.csv")
    return pd.DataFrame(columns=["timestamp", "temperatura", "umidade", "potencia"])


# ==========================
# CONFIG STREAMLIT
# ==========================
st.set_page_config(
    page_title="Controle Inteligente de Ar-Condicionado",
    layout="wide",
    page_icon="🌡️"
)

st.title("🌡️ Controle Inteligente de Ar-Condicionado (Lógica Fuzzy)")
st.write("Sistema inteligente que calcula automaticamente a potência ideal do ar-condicionado usando **Lógica Fuzzy**.")


# ==========================
# SLIDERS DE ENTRADA
# ==========================
col1, col2 = st.columns(2)

with col1:
    temp = st.slider("Temperatura (°C)", 10, 40, 25)

with col2:
    umid = st.slider("Umidade (%)", 0, 100, 50)


# ==========================
# CÁLCULO FUZZY
# ==========================
potencia = compute_power(temp, umid)

# SALVA LOG
save_log(temp, umid, potencia)


# ==========================
# PAINEL PRINCIPAL
# ==========================
st.markdown(f"## 💡 Potência recomendada: **{potencia:.1f}%**")

if potencia < 30:
    st.success("O ambiente está confortável. Potência baixa é suficiente. 😎")
elif potencia < 70:
    st.warning("Ambiente moderado. Ajustando potência para manter o conforto. 🟡")
else:
    st.error("Ambiente muito quente! Potência alta recomendada. 🔥")


# ==========================
# DASHBOARD
# ==========================
st.markdown("---")
st.header("📊 Dashboard do Sistema")

logs = load_logs()

colA, colB, colC = st.columns(3)

with colA:
    st.metric("Temperatura Atual", f"{temp} °C")

with colB:
    st.metric("Umidade Atual", f"{umid} %")

with colC:
    st.metric("Potência Atual", f"{potencia:.1f} %")


# ==========================
# GRÁFICO DE POTÊNCIA (Tempo Real)
# ==========================
st.subheader("📈 Histórico da Potência Recomendada")

if not logs.empty:
    st.line_chart(logs["potencia"])
else:
    st.info("O gráfico aparecerá depois das primeiras interações.")


# ==========================
# TABELA DE LOGS
# ==========================
st.subheader("📄 Dados coletados durante o uso")
st.dataframe(logs, use_container_width=True)


# ==========================
# MINI API (PASSO 4)
# ==========================
st.markdown("---")
st.header("🔗 API Integrada (Simples)")

st.code("""
Endpoint disponível:

/api/potencia?temp=30&umid=70

Retorno:
{
    "temperatura": 30,
    "umidade": 70,
    "potencia": 82.3
}
""", language="txt")

st.write("Como é apenas uma demonstração, a API funciona usando *query params* dentro do próprio Streamlit.")

# API SIMPLES VIA QUERY PARAMS
query = st.query_params  # ✔ novo método

if "temp" in query and "umid" in query:
    try:
        t = float(query["temp"])
        h = float(query["umid"])
        p = compute_power(t, h)

        st.json({
            "temperatura": t,
            "umidade": h,
            "potencia": round(p, 2)
        })

    except:
        st.error("Erro ao processar parâmetros da API.")