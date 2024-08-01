import csv

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Função que lê um arquivo csv e retorna uma lista de funcionarios
    """
    
    with open(nome_do_arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        lista = []
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)

    return lista

def calcular_vendas_categoria(lista: list[dict]) -> list[dict]:
    """
    Função que calcula quantidade de vendas por categoria
    """

    categoria = {}
    for produto in lista:
        if produto['Categoria'] in categoria:
            valor = int(produto['Venda']) * int(produto['Quantidade'])
            categoria[produto['Categoria']] = categoria[produto['Categoria']] + valor
        else:
            valor = int(produto['Venda']) * int(produto['Quantidade'])
            categoria[produto['Categoria']] = valor

    return categoria

def main():
    """
    Função que integra as funções
    """

    path_arquivo = "vendas.csv"
    lista: list[dict] = ler_csv(path_arquivo)
    resultado: dict = calcular_vendas_categoria(lista)
    for categoria in resultado:
        print(f"{categoria} total de vendas: $ {resultado[categoria]:.2f} reais")

if __name__ == '__main__':
     main()