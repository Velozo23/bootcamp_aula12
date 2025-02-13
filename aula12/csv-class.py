import pandas as pd

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        
    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)
        return self.df
    
    def filtra_por(self, coluna, atributo):
        return self.df[self.df[coluna] == atributo]   
    


arquivo_csv = './exemplo2.csv'
filtro = 'estado'
limite = 'SP'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()

print(arquivo_CSV.filtra_por(filtro, limite))

