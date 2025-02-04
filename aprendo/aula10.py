salario = float(input('Digite seu salario:=>'))

novo_salario = salario + (salario * 15 /100)

print(f'O funcionaario que ganhava R${salario:.2f} com 15% de aumento, '
      f' passa a ganhar {novo_salario:.2f}')