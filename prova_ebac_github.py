import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv('ecommerce_estatistica.csv')

lista_temporada = df['Temporada'].unique()
options = [{'label': temp, 'value': temp} for temp in lista_temporada]

def cria_graficos(selecao_genero):
    # Gráfico de Barra: 
    filtro_df = df[df['Temporada'].isin(selecao_genero)]

    fig1 = px.bar(filtro_df, x='Marca', y='Gênero', color='Gênero', barmode='group', color_discrete_sequence=px.colors.sequential.RdBu)
    fig1.update_layout(
        title='Vendas das Marcas por Gênero',
        xaxis_title='Gênero',
        yaxis_title='Qtd_Vendidos',
        legend_title='Vendas na Temporada',
        plot_bgcolor='rgba(222,255,253,1)',
        paper_bgcolor='rgba(186,245,241,1)'
    )
    fig2 = px.scatter_3d(filtro_df, x='Gênero', y='Qtd_Vendidos', z='Temporada', color='Gênero')
    fig2.update_layout(
        title='Quantidade de Vendas na Temporada por Gênero',
        scene=dict(
            xaxis_title='Gênero',
            yaxis_title='Vendas',
            zaxis_title='Temporada'
        )
    )
    return fig1, fig2

def cria_app():
    app = Dash(__name__)
    
    app.layout = html.Div([
        # O 'Div' é parágrafo. 
        html.H1("Dashboard Interativo"),
        # O 'H1' é o título da página. 
        html.Div('''
        Interatividade entre os Dados
        '''),
        html.Br(), # O 'Br' serve para pular uma linha. 
        html.H2("Gráfico de Marcas mais Vendidas por Gênero"),
        # O 'H2' é um cabeçalho. Menor que o título ('H1'). 
        dcc.Checklist(
            id='id_selecao_temporada',
            options=options,
            value=[lista_temporada[0]] # Define um valor padrão. 
        ),
        dcc.Graph(id='id_grafico_barra'),
        dcc.Graph(id='id_grafico_3d')          
    ])
    return app

# Execução do app: 
if __name__ == '__main__':
    app = cria_app()
    
    @app.callback(
        [Output('id_grafico_barra', 'figure'),
        Output('id_grafico_3d', 'figure')
        ],
        [Input('id_selecao_temporada', 'value')]
    )
    def atualiza_grafico(selecao_genero):
        fig1, fig2 = cria_graficos(selecao_genero)
        return [fig1, fig2]
    app.run(debug=True, port=8050) # Default 8050. 
