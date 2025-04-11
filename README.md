# Menu Fetcher

## Visão Geral
Menu Fetcher é uma aplicação Python que recupera menus de um endpoint de API especificado com base em um código de canal e exporta os resultados para um arquivo Excel. Este projeto foi projetado para ser executado localmente e requer um token de API válido para autenticação.

## Estrutura do Projeto
```
menu-fetcher
├── src
│   ├── main.py               # Ponto de entrada da aplicação
│   ├── api
│   │   ├── fake_endpoint.py   # Simula o endpoint da API
│   │   └── client.py          # Gerencia as requisições para a API
│   ├── utils
│   │   └── excel_exporter.py   # Exporta dados para Excel
│   └── config
│       └── settings.py        # Configurações do projeto
├── requirements.txt           # Dependências do projeto
└── README.md                  # Documentação do projeto
```

## Instalação
1. Clone o repositório:
   ```
   git clone <repository-url>
   cd menu-fetcher
   ```

2. Instale as dependências necessárias:
   ```
   pip install -r requirements.txt
   ```

## Configuração
- Abra o arquivo `src/config/settings.py` e substitua os valores de exemplo pelos valores reais da URL do endpoint da API e do token.

## Uso
1. Execute a aplicação:
   ```
   python src/main.py
   ```

2. A aplicação solicitará que você insira um código de canal. Após inserir o código, ela buscará os menus e os exportará para um arquivo Excel.