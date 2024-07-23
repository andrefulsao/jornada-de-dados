CONSTANTE_BONUS = 1000
nome = input("Digite nome do funcionario: ")
salario = float(input("Digite salario do funcionario: "))
bonus = float(input("Digite bonus do funcionario: "))
result_final = CONSTANTE_BONUS + (salario * bonus)

print(result_final)

print(f"Nome do funcionario: {nome} \nSalario do funcionario: R${salario} \nBonus aplicado: {bonus}% \nResultado Final: R${result_final}")