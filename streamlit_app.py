import time
import datetime

import streamlit as st

from taximetro import calcular_importe

st.markdown(
    "<h1 style='text-align: center; font-size: 3.5em;'>🚕 Taxímetro</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    div.stButton > button {
        height: 5em;
        font-size: 1.3em !important;
        font-weight: 900 !important;
        color: black !important;
        white-space: normal;
    }
    div.stButton > button p {
        font-size: 1.3em !important;
        font-weight: 900 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "total" not in st.session_state:
    st.session_state.total = 0.0
    st.session_state.estado = "parado"
    st.session_state.marca_tiempo = None

col1, col2, col3, col4 = st.columns(4)

if col1.button("▶️ Iniciar", use_container_width=True, type="primary"):
    st.session_state.marca_tiempo = time.time()
    st.session_state.estado = "parado"
    st.session_state.total = 0.0

if col2.button("💨 Movimiento", use_container_width=True, type="primary") and st.session_state.marca_tiempo is not None:
    tiempo_transcurrido = time.time() - st.session_state.marca_tiempo
    st.session_state.total += calcular_importe(st.session_state.estado, tiempo_transcurrido)
    st.session_state.estado = "movimiento"
    st.session_state.marca_tiempo = time.time()

if col3.button("🛑 Parado", use_container_width=True, type="primary") and st.session_state.marca_tiempo is not None:
    tiempo_transcurrido = time.time() - st.session_state.marca_tiempo
    st.session_state.total += calcular_importe(st.session_state.estado, tiempo_transcurrido)
    st.session_state.estado = "parado"
    st.session_state.marca_tiempo = time.time()

if col4.button("🏁 Finalizar", use_container_width=True, type="primary") and st.session_state.marca_tiempo is not None:
    tiempo_transcurrido = time.time() - st.session_state.marca_tiempo
    st.session_state.total += calcular_importe(st.session_state.estado, tiempo_transcurrido)
    st.session_state.estado = "finalizado"
    st.session_state.marca_tiempo = None
    with open("logs/historial.txt", "a") as log:
        log.write(f"{datetime.datetime.now()} - Total: {st.session_state.total:.2f}€\n")

st.divider()

if st.session_state.estado == "movimiento":
    icono_estado, color_estado = "🚕💨", "#2ECC71"
elif st.session_state.estado == "finalizado":
    icono_estado, color_estado = "✅", "#3498DB"
else:
    icono_estado, color_estado = "🚕", "#E74C3C"

st.markdown(
    f"""
    <div style="text-align: center;">
        <div style="font-size: 2em; font-weight: bold; color: #FFC107; letter-spacing: 0.1em;">ESTADO</div>
        <div style="font-size: 2.5em; font-weight: bold; margin-top: 0.2em;">
            {icono_estado}
            <span style="background-color: {color_estado}; color: white; padding: 0.2em 0.6em; border-radius: 1em;">
                {st.session_state.estado.upper()}
            </span>
        </div>
        <div style="font-size: 2em; font-weight: bold; color: #FFC107; letter-spacing: 0.1em; margin-top: 1.5em;">TOTAL A PAGAR</div>
        <div style="margin-top: 0.3em;">
            <span style="background-color: {color_estado}; color: white; font-size: 2.5em; font-weight: bold; padding: 0.2em 0.6em; border-radius: 1em;">
                {st.session_state.total:.2f}€
            </span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
