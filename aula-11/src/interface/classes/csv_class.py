import pandas as pd

class CsvProcessor:
    """
        Classe para instanciar files CSV's.
    """
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None

    def carregar_csv(self) -> None:
        """
            Metodo que atribui o dataFrame para a instancia.
        """
        self.df = pd.read_csv(self.file_path)

    def filtrar_por(self, colunas: list, atributos: list) -> pd.DataFrame:
        """
            Metodo que recebe um dataFrame e
            retorna o dataFrame filtrado por de acordo com 
            um ou mais atributos de uma ou mais colunas.
        """
        if len(colunas) != len(atributos):
            raise ValueError("Não tem o mesmo número de colunas e atributos.")
        
        if len(colunas) == 0:
            return self.df
        
        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

        
        self.df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]

        if len(colunas) == 1:
            print('###############')
            print(f'coluna filtrada: {coluna_atual}, atributo utilizado: {atributo_atual}')
            return self.df_filtrado
        else:
            print('###############')
            print(f'coluna filtrada: {coluna_atual}, atributo utilizado: {atributo_atual}')
            print(self.df_filtrado)
            return self.filtrar_por(colunas[1:], atributos[1:])    