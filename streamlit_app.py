
import streamlit as st

# Título do app
st.title("Multiplicador de X e Y")

# Campos de entrada
x = st.number_input("Digite o valor de X", value=0.0)
y = st.number_input("Digite o valor de Y", value=0.0)

# Botão para calcular
if st.button("Multiplicar"):
    resultado = x * y
    st.success(f"O resultado de {x} × {y} é {resultado}")
