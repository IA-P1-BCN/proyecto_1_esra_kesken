import time

import streamlit as st

from taximetro import calcular_importe

st.title("🚕 Taxímetro")

if "total" not in st.session_state:
    st.session_state.total = 0.0
    st.session_state.estado = "parado"
    st.session_state.marca_tiempo = None

col1, col2, col3, col4 = st.columns(4)

if col1.button("Iniciar"):
    st.session_state.marca_tiempo = time.time()
    st.session_state.estado = "parado"
    st.session_state.total = 0.0

if col2.button("Movimiento") and st.session_state.marca_tiempo is not None:
    tiempo_transcurrido = time.time() - st.session_state.marca_tiempo
    st.session_state.total += calcular_importe(st.session_state.estado, tiempo_transcurrido)
    st.session_state.estado = "movimiento"
    st.session_state.marca_tiempo = time.time()

if col3.button("Parado") and st.session_state.marca_tiempo is not None:
    tiempo_transcurrido = time.time() - st.session_state.marca_tiempo
    st.session_state.total += calcular_importe(st.session_state.estado, tiempo_transcurrido)
    st.session_state.estado = "parado"
    st.session_state.marca_tiempo = time.time()

if col4.button("Finalizar") and st.session_state.marca_tiempo is not None:
    tiempo_transcurrido = time.time() - st.session_state.marca_tiempo
    st.session_state.total += calcular_importe(st.session_state.estado, tiempo_transcurrido)
    st.session_state.marca_tiempo = None

st.metric("Estado", st.session_state.estado)
st.metric("Total", f"{st.session_state.total:.2f}€")
