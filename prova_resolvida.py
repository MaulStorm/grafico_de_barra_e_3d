import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'c:\Users\Gamer\OneDrive\Documentos\EBAC\CURSO ANALISTA DE DADOS\PYTHON\6-Visualização de Dados\PROVA\ecommerce_estatistica.csv')
print(df.head().to_string())

# Histograma: 
plt.hist(df['Preço'])
plt.show()

# Histograma - Parâmetros: 
plt.figure(figsize=(10, 6)) # Tamanho da imagem (caixa) será 10 por 6. 
plt.hist(df['Preço'], bins=150, color='green', alpha=0.8)
# Os 'bins' são as divisões das colunas (formando os quadrados no gráfico). 
# O 'alpha' é a transparência do gráfico. 
plt.title('Histograma - Distribuição de Preços') # Define o título do gráfico, 
# que fica no canto superior. 
plt.xlabel('Preço') # Define o título do eixo X. 
plt.xticks(ticks=range(0, int(df['Preço'].max())+10, 10)) # Define os intervalos 
# dos valores a serem mostrados no gráfico; no caso, de 2mil em 2mil no eixo X. 
plt.ylabel('Frequência') # Define o título do eixo Y. 
plt.grid(True) # Habilita as linhas de grade. 
plt.show()

# Gráfico de Dispersão (hexbin): 
# (Lembre-se: dispersão e correlação são a mesma coisa!)
plt.hexbin(df['Desconto_MinMax'], df['Qtd_Vendidos_Cod'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Desconto_MinMax')
plt.ylabel('Qtd_Vendidos_Cod')
plt.title('Dispersão de Desconto_MinMax e Qtd_Vendidos_Cod')
plt.show()

df_corr = df[['N_Avaliações_MinMax', 'Qtd_Vendidos_Cod']].corr()
# Heatmap de Correlação: 
# (Aplicar mapas de calor para identificar rapidamente correlações fortes ou fracas entre várias variáveis.) 
plt.figure(figsize=(10,8))
sns.heatmap(df_corr, annot=True, fmt=".2f")
plt.title('Mapa de Calor da Correlação entre Variáveis')
plt.show()

# Gráfico de barras: 
plt.figure(figsize=(10,4))
df['Gênero'].value_counts().plot(kind='bar', color='#90ee70')
plt.title('Divisão por gênero - 1')
plt.xlabel('Gênero')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

x = df['Gênero'].value_counts().index
y = df['Gênero'].value_counts().values

# Gráfico de Pizza (pie): 
plt.figure(figsize=(10,6))
plt.pie(y, labels= x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição por Gênero - 2')
plt.show()

# Gráfico de Densidade: 
# (Parecido com o do Histograma mas com a curva mais suave/arredondada. Gráficos 
# de densidade suavizam a distribuição dos dados, mas podem potencialmente esconder 
# picos acentuados que seriam visíveis em um histograma tradicional.) 
plt.figure(figsize=(10,6))
sns.kdeplot(df['Desconto'], fill=True, color='#863e9c')
plt.title('Densidade de produtos com Desconto')
plt.xlabel('Descontos')
plt.show()

# Gráfico de Regressão: 
# (Calcula a linha entre dois campos (colunas). Gráficos de regressão NÃO devem ser utilizados para prever 
# tendências futuras, pois eles são apenas para visualização de dados históricos. Gráficos de regressão são 
# usados para visualizar relações e não são indicados para previsões de tendências futuras, 
# embora possam sugerir padrões históricos.) 
sns.regplot(x='Desconto_MinMax', y='Qtd_Vendidos_Cod', data=df, color='#278f65', scatter_kws={'alpha':0.5, 'color': '#34c289'})
# O primeiro 'color' é a cor da linha e a segunda é a cor dos pontos (bolhas). O 'alpha' é 
# referente à transparência dos pontos. 
plt.title('Regressão de Desconto por Vendas')
plt.xlabel('Desconto')
plt.ylabel('Vendas')
plt.show()
