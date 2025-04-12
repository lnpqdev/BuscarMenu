from utils.exportador_sql import export_to_sql_file
import pandas as pd

def ler_excel(caminho_arquivo):
    try:
        df = pd.read_excel(caminho_arquivo)
        if 'Fluxos' not in df.columns:
            raise ValueError("A coluna 'NomeDaColuna' não foi encontrada no arquivo Excel.")
        return df['Fluxos'].dropna().tolist()
    except Exception as erro:
        print(f"Erro ao ler o arquivo Excel: {erro}")
        return []

def gerar_query_insert(fluxos, table_name):
    print(f"Quantidade total de fluxos: {len(fluxos)}")
    sem_duplicatas = set(fluxos)
    print(f"Quantidade de fluxos duplicados removidos: {len(fluxos) - len(sem_duplicatas)}")
    values = ",\n".join([f"('{fluxo}')" for fluxo in sem_duplicatas])
    query = f"insert into {table_name} (valor) values\n{values};"
    return query, len(sem_duplicatas)

def processar_fluxos():
    excel_file = "fluxos_tratados.xlsx"
    table_name = "testefluxos"
    arquivo_saida = "fluxos_inseridos.sql"

    fluxos = ler_excel(excel_file)
    if not fluxos:
        print("Nenhum fluxo encontrado no arquivo Excel.")
        return
    
    query, total_inserido = gerar_query_insert(fluxos, table_name)
    
    export_to_sql_file(query, arquivo_saida)

    print(f"Total de fluxos inseridos na query: {total_inserido}")