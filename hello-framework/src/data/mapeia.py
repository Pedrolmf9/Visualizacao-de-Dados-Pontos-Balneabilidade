import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('HIST_Pontos_de_Balneabilidade.csv')

# Função para mapear nome da praia e tipo
def map_praia_tipo(codptcoleta):
    if codptcoleta.startswith('GR000'):
        return 'Gragoatá', 'Baía de Guanabara'
    elif codptcoleta.startswith('BV001'):
        return 'Boa Viagem', 'Baía de Guanabara'
    elif codptcoleta.startswith('FC001') or codptcoleta.startswith('FC000'):
        return 'Praia das Flechas', 'Baía de Guanabara'
    elif codptcoleta.startswith('IC'):
        return 'Praia de Icaraí', 'Baía de Guanabara'
    elif codptcoleta.startswith('SF'):
        return 'Praia de São Francisco', 'Baía de Guanabara'
    elif codptcoleta.startswith('CH'):
        return 'Charitas', 'Baía de Guanabara'
    elif codptcoleta.startswith('JR'):
        return 'Jurujuba', 'Baía de Guanabara'
    elif codptcoleta.startswith('AD000') or codptcoleta.startswith('EA000'):
        return 'Praia da Fortaleza', 'Baía de Guanabara'
    elif codptcoleta.startswith('PR'):
        return 'Piratininga', 'Oceânicas'
    elif codptcoleta.startswith('SG000'):
        return 'Praia do Sossego', 'Oceânicas'
    elif codptcoleta.startswith('CM'):
        return 'Camboinhas', 'Oceânicas'
    elif codptcoleta.startswith('II'):
        return 'Itaipu', 'Oceânicas'
    elif codptcoleta.startswith('IA'):
        return 'Itacoatiara', 'Oceânicas'
    else:
        return 'Desconhecido', 'Desconhecido'

# Aplicar a função ao DataFrame
df[['nomePraia', 'tipo']] = df['tx_codptcoleta'].apply(map_praia_tipo).apply(pd.Series)

# Salvar o novo CSV
df.to_csv('mapBairros.csv', index=False)

print("Novo CSV salvo com sucesso!")
