salario_base = float(input())

contribuicao1 = (salario_base * 0.08)
contribuicao2 = (salario_base * 0.09)
contribuicao3 = (salario_base * 0.11)


if salario_base <= 1751.81:
    print("Desconto do INSS:R${:.2f}".format(contribuicao1))
elif salario_base <= 2919.72:
    print("Desconto do INSS:R${:.2f}".format(contribuicao2))
elif salario_base <= 5839.45:
    print("Desconto do INSS:R${:.2f}".format(contribuicao3))
else:
    print("Desconto do INSS:R$ 642.34")
