from csv_class import CsvProcessor

arquivo_csv = './exemplo2.csv'
filtro = 'estado'
limite = 'SP'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()

print(arquivo_CSV.filtra_por(['estado', 'preco'], ['SP', '10,50']))
#print(arquivo_CSV.sub_filtro('preco', '10,50'))

