import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# configuração inicial da página
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

st.title("Dashboard de Vendas")

# upload do arquivo csv
arquivo = st.file_uploader("Envie seu arquivo CSV", type=["csv"])

if arquivo:
    # lendo o csv (usei sep=";" porque excel no brasil geralmente salva assim)
    df = pd.read_csv(arquivo, sep=";")
    
    # padronizando os nomes das colunas (tira espaço e deixa primeira letra maiúscula)
    df.columns = df.columns.str.capitalize().str.strip()

    # colunas mínimas que o sistema precisa pra funcionar
    colunas_obrigatorias = {"Data", "Produto", "Valor"}

    # verifica se o csv tem o que precisa
    if not colunas_obrigatorias.issubset(df.columns):
        st.error("O CSV precisa conter as colunas: data, produto e valor")
        st.stop()  # para execução se não tiver as colunas certas

    st.subheader("Dados Brutos")
    st.dataframe(df)

    # convertendo a coluna Data para formato de data
    # criei uma coluna nova 'data' só pra garantir que está no formato certo
    df["data"] = pd.to_datetime(df["Data"])

    # calculando métricas principais
    faturamento_total = df["Valor"].sum()
    ticket_medio = df["Valor"].mean()
    produto_mais_vendido = df["Produto"].value_counts().idxmax()

    # criando 3 colunas pra organizar as métricas lado a lado
    col1, col2, col3 = st.columns(3)

    col1.metric("Faturamento Total", f"R$ {faturamento_total:,.2f}")
    col2.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}")
    col3.metric("Produto Mais Vendido", produto_mais_vendido)

# seção dos gráficos
st.subheader("Gráficos")

# criando duas colunas pra deixar os gráficos lado a lado
col1, col2 = st.columns(2)

with col1:
    st.markdown("Vendas por Dia")
    
    # agrupando por data e somando os valores
    vendas_dia = df.groupby("Data")["Valor"].sum()
    
    # criando figura menor pra não ficar gigante na tela
    fig1, ax1 = plt.subplots(figsize=(5,4))
    vendas_dia.plot(ax=ax1)
    
    ax1.set_xlabel("")
    ax1.set_ylabel("Valor")
    
    # rotacionando datas pra não ficar sobreposto
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    st.pyplot(fig1)

with col2:
    st.markdown("Vendas por Produto")
    
    # agrupando por produto
    vendas_produto = df.groupby("Produto")["Valor"].sum()
    
    fig2, ax2 = plt.subplots(figsize=(5,4))
    vendas_produto.plot(kind="bar", ax=ax2)
    
    ax2.set_xlabel("")
    ax2.set_ylabel("Valor")
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    st.pyplot(fig2)