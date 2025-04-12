def export_to_sql_file(query, arquivo_saida):
    try:
        with open(arquivo_saida, 'w', encoding='ascii', errors='ignore') as arquivo:
            arquivo.write(query)
        print(f"Arquivo SQL exportado com sucesso: {arquivo_saida}")
    except Exception as e:
        print(f"Erro ao exportar o arquivo SQL: {e}")