import streamlit as st
import pandas as pd

st.title("Taxas Solicitadas*")

# Dados fixos
dados = {
    "Bandeira": [
        "Visa", "Visa", "Visa", "Visa",
        "MasterCard", "MasterCard", "MasterCard", "MasterCard",
        "Elo", "Elo", "Elo", "Elo",
        "Amex", "Amex", "Amex", "Amex"
    ],
    "Plano de venda": [
        "Débito", "Crédito", "Parcelado 2 a 6", "Parcelado 7 a 12",
        "Débito", "Crédito", "Parcelado 2 a 6", "Parcelado 7 a 12",
        "Débito", "Crédito", "Parcelado 2 a 6", "Parcelado 7 a 12",
        "Débito", "Crédito", "Parcelado 2 a 6", "Parcelado 7 a 12"
    ],
    "Margem (%)": [0.00] * 16
}

df = pd.DataFrame(dados)

# Editor de dados
edited_df = st.data_editor(
    df,
    num_rows="fixed",
    column_config={
        "Margem (%)": st.column_config.NumberColumn(
            "Margem (%)",
            min_value=0.0,
            max_value=100.0,
            step=0.01,
            format="%.2f"
        )
    },
    use_container_width=True
)

# Exibir resultado final
st.subheader("Tabela Atualizada")
st.dataframe(edited_df, use_container_width=True)
