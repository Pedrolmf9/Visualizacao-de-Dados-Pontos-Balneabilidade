import pandas as pd

# Carregar os dados do CSV para um DataFrame do Pandas
df = pd.read_csv('mapBairros.csv')

# Converter a coluna dt_atualizacao para datetime
df['dt_atualizacao'] = pd.to_datetime(df['dt_atualizacao'])

# Extrair o ano da coluna dt_atualizacao
df['ano'] = df['dt_atualizacao'].dt.year

# Filtrar os dados para o intervalo de anos entre 2019 e 2023 e incluir a coluna tipo
df_filtrado = df[(df['ano'] >= 2019) & (df['ano'] <= 2023)]

# Contagem de ocorrências por ano, tipo, nome da praia e status
contagem = df_filtrado.groupby(['ano', 'tipo', 'nomePraia', 'tx_status']).size().reset_index(name='quantidade')

# Salvar o resultado em um arquivo CSV
contagem.to_csv('ocorrAno.csv', index=False)

print("Contagem salva em 'ocorrAno.csv'")
