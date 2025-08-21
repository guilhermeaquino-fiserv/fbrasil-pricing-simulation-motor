
import streamlit as st

# Título do app
st.title("Multiplicador de X e Y")



x = st.number_input("CNPJ", value=0)
y = st.number_input("CNAE", value=0)

# Layout em colunas
col1, col2 = st.columns(2)

with col1:
    debit = st.number_input("Digite o valor de debit", value=0.0)
    cred = st.number_input("Digite o valor de cred", value=0.0)

with col2:    
    parc6 = st.number_input("Digite o valor de parc6", value=0.0)
    parc12 = st.number_input("Digite o valor de parc12", value=0.0)
    



# Botão para calcular
if st.button("Multiplicar"):
    resultado = x * y
    st.success(f"{resultado}")
