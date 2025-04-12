import unittest
from unittest.mock import patch, mock_open
from src.services.leitor_excel_service import ler_excel, gerar_query_insert, processar_fluxos
import pandas as pd

class TestLeitorExcelService(unittest.TestCase):

    @patch("pandas.read_excel")
    def test_ler_excel(self, mock_read_excel):
        # Mock do DataFrame retornado pelo pandas
        mock_df = pd.DataFrame({"Fluxos": ["Menu 1", "Menu 2", None, "Menu 1"]})
        mock_read_excel.return_value = mock_df

        # Testa a função ler_excel
        resultado = ler_excel("mocked_file.xlsx")
        self.assertEqual(resultado, ["Menu 1", "Menu 2", "Menu 1"])  # Verifica se valores nulos foram removidos

    def test_gerar_query_insert(self):
        # Dados de entrada
        fluxos = ["Menu 1", "Menu 2", "Menu 1", "Menu 3"]
        table_name = "testefluxos"

        # Testa a função gerar_query_insert
        query, total_inserido = gerar_query_insert(fluxos, table_name)

        # Verifica a query gerada
        query_esperada = (
            "insert into testefluxos (valor) values\n"
            "('Menu 1'),\n"
            "('Menu 2'),\n"
            "('Menu 3');"
        )
        self.assertEqual(query, query_esperada)

        # Verifica o total de valores únicos inseridos
        self.assertEqual(total_inserido, 3)

    @patch("builtins.open", new_callable=mock_open)
    @patch("src.services.leitor_excel_service.ler_excel")
    @patch("src.services.leitor_excel_service.gerar_query_insert")
    def test_processar_fluxos(self, mock_gerar_query_insert, mock_ler_excel, mock_open_file):
        # Mock dos fluxos retornados por ler_excel
        mock_ler_excel.return_value = ["Menu 1", "Menu 2", "Menu 1"]

        # Mock da query gerada
        mock_gerar_query_insert.return_value = (
            "insert into testefluxos (valor) values\n('Menu 1'),\n('Menu 2');",
            2,
        )

        # Testa a função processar_fluxos
        processar_fluxos()

        # Verifica se ler_excel foi chamado corretamente
        mock_ler_excel.assert_called_once_with("fluxos_tratados.xlsx")

        # Verifica se gerar_query_insert foi chamado corretamente
        mock_gerar_query_insert.assert_called_once_with(
            ["Menu 1", "Menu 2", "Menu 1"], "testefluxos"
        )

        # Verifica se o arquivo foi escrito corretamente
        mock_open_file.assert_called_once_with("fluxos_inseridos.sql", "w", encoding="utf-8")
        mock_open_file().write.assert_called_once_with(
            "insert into testefluxos (valor) values\n('Menu 1'),\n('Menu 2');"
        )