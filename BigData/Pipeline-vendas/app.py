import time
import streamlit as st
from pymongo import MongoClient
import pandas as pd
import plotly.express as px

# Conectar ao MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["sales_db"]
collection = db["raw_sales_data"]

# Título do Dashboard
st.title("Dashboard de Vendas - Atualização em Tempo Real")

# Espaço reservado para o gráfico
placeholder = st.empty()

# Função para consultar dados do MongoDB
def get_data():
    """Consulta os dados do MongoDB e converte para um DataFrame."""
    data = list(collection.find())
    if not data:
        return pd.DataFrame()  # Retorna um DataFrame vazio se não houver dados
    df = pd.DataFrame(data)
    # Conversão de tipos para garantir compatibilidade
    df['Quantidade Vendida'] = df['Quantidade Vendida'].astype(int)
    df['Preço Unitário (R$)'] = df['Preço Unitário (R$)'].astype(float)
    df['Total de Vendas (R$)'] = df['Total de Vendas (R$)'].astype(float)
    return df

# Loop para atualizar o gráfico
while True:
    df = get_data()  # Consulta os dados mais recentes

    with placeholder.container():
        if not df.empty:
            # Calcula o total de vendas por categoria
            total_sales_by_category = df.groupby("Categoria")["Total de Vendas (R$)"].sum().reset_index()

            # Cria o gráfico interativo com Plotly
            fig = px.bar(
                total_sales_by_category,
                x="Categoria",
                y="Total de Vendas (R$)",
                title="Total de Vendas por Categoria",
                labels={"Total de Vendas (R$)": "Total de Vendas (R$)"},
            )

            # Atualiza o gráfico no mesmo espaço reservado
            placeholder.plotly_chart(fig, use_container_width=True, key=f"plotly_chart_{int(time.time())}")
        else:
            placeholder.write("Nenhum dado disponível no momento. O gráfico será exibido assim que os dados estiverem disponíveis.")

    # Aguarda 10 segundos antes de atualizar novamente
    time.sleep(10)

