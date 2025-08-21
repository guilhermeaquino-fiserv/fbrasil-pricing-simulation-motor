import streamlit as st

# Menu lateral
pagina = st.sidebar.selectbox("Selecione a página", ["P&L", "Consulta Politica"])

# Página 1
if pagina == "P&L":
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

    import pandas as pd
    df = pd.DataFrame(dados)

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


# Página 2
elif pagina == "Consulta Politica":
    st.title("Politica BAU")
    
    # Campos de entrada
    nome = st.text_input("Nome")
    fat_ano = st.number_input("Faturamento Anual", value=0.0)
    cnae = st.number_input("CNAE")
    
    # Botão para calcular
    if st.button("Consultar"):
       st.success(f"mostra tabela com condições")

