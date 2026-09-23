import time

import streamlit as st

from taximetro import calcular_importe

st.title("🚕 Taxímetro")

st.markdown(
    """
    <style>
    div.stButton > button {
        height: 5em;
        font-size: 1.3em !important;
        font-weight: bold;
        color: black !important;
        white-space: normal;
    }
    div.stButton > button p {
        font-size: 1.3em !important;
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
    st.session_state.marca_tiempo = None

st.divider()

icono_estado = "🚕💨" if st.session_state.estado == "movimiento" else "🚕"
st.markdown(
    f"""
    <div style="text-align: center;">
        <div style="font-size: 1.5em; color: #FFC107;">ESTADO</div>
        <div style="font-size: 2.5em; font-weight: bold;">{icono_estado} {st.session_state.estado.upper()}</div>
        <div style="font-size: 1.5em; color: #FFC107; margin-top: 0.5em;">TOTAL A PAGAR</div>
        <div style="font-size: 3.5em; font-weight: bold; color: #FFC107;">{st.session_state.total:.2f}€</div>
    </div>
    """,
    unsafe_allow_html=True,
)
