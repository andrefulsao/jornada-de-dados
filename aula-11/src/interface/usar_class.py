from classes.csv_class import CsvProcessor

arquivo_csv = '../exemplo.csv'
coluna = 'estado'
atributo = 'SP'
coluna2 = 'data'
atributo2 = '20/01/2024'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtrar_por([coluna, coluna2], [atributo, atributo2]))