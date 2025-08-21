
import streamlit as st
import pandas as pd

st.title("Taxas Solicitadas")

# Dados fixos
bandeiras = ["Visa", "MasterCard", "Elo", "Amex"]
planos = ["Débito", "Crédito", "Parcelado 2 a 6", "Parcelado 7 a 12"]

# Criar estrutura da tabela
dados = []
for bandeira in bandeiras:
    for plano in planos:
        dados.append({"Bandeira": bandeira, "Plano de venda": plano, "Margem (%)": 0.00})

df = pd.DataFrame(dados)

# Interface para preenchimento
st.write("Preencha as margens abaixo:")

# Criar inputs dinâmicos
for i in range(len(df)):
    margem_input = st.number_input(
        label=f"{df.loc[i, 'Bandeira']} - {df.loc[i, 'Plano de venda']}",
        min_value=0.0,
        max_value=100.0,
        value=df.loc[i, "Margem (%)"],
        step=0.01,
        key=f"margem_{i}"
    )
    df.loc[i, "Margem (%)"] = margem_input

# Exibir tabela atualizada
st.subheader("Tabela Atualizada")
st.dataframe(df)
