import requests
from utils.excel_exporter import export_to_excel
from config.settings import CANAIS_ENDPOINT, MENUS_ENDPOINT

def obter_token():

    return input("Insira o token de autenticação: ").strip()

def buscar_canais(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(CANAIS_ENDPOINT, headers=headers, verify=False)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar canais: {response.status_code} - {response.text}")
        return []

def buscar_menus_por_canal(token, canal_id):
    url = MENUS_ENDPOINT.replace("{canal_id}", str(canal_id))
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers, verify=False)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar menus para o canal {canal_id}: {response.status_code} - {response.text}")
        return []

def main():
    token = obter_token()
    canais = buscar_canais(token)
    
    if not canais:
        print("Não existem canais disponíveis.")
        return

    todos_menus = []

    for canal in canais:
        menus = buscar_menus_por_canal(token, canal['id'])
        print(f"Buscando menus do canal: {canal['name']} (ID: {canal['id']}) - Quantidade de menus encontrados: {len(menus) if menus else 0}")
        if menus:
            for menu in menus:
                menu['channel_name'] = canal['name']
            todos_menus.extend(menus)
        else:
            print(f"Nenhum menu encontrado para o canal: {canal['name']}")

    if todos_menus:
        export_to_excel(todos_menus)
        print("Menus exportados com sucesso.")
    else:
        print("Nenhum menu encontrado.")

if __name__ == "__main__":
    main()