def soma(valor_1: float, valor_2: float = 10) -> float:
    """
    Uma função simples que retorna a soma dos valor de tipo float.
    """
    valor_3 = valor_1 * valor_2    
    return valor_3



try:
    valor_1 = input("Digite o valor 1 a ser somado: ")
    valor_2 = input("Digite o valor 1 a ser somado: ")

    valor_1 = float(valor_1)
    valor_2 = float(valor_2)

    resultado = soma(valor_1, valor_2)
    print(resultado)

except ValueError as e:
    print(e)