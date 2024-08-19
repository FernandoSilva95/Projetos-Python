
# bibliotecas importadas: Pandas, openpyxl, plotly, nbformat

import pandas as pd
import plotly.express as px

dados = pd.read_excel("vendas.xlsx")

# criação de gráficos, através dos dados da tabela e apresentar em html

lista_colunas = ["loja", "cidade", "estado", "tamanho", "local_consumo"]

for coluna in lista_colunas:
    grafico = px.histogram(dados, x=coluna, 
                    y="preco", 
                    text_auto=True,
                    title="Faturamento",
                    color="forma_pagamento")
    grafico.show()

    # salver o gráfico como html
    grafico.write_html(f"Faturamento-{coluna}.html")
