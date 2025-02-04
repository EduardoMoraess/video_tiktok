#Escreva um programa que pergunte a quantidade de Km percorridos
# por um carr0 alugado e a quantiadade de dias pelos quais ele foi alugado
#Calcule o preço a pagar, sabenndo que o carro custa R$60 por dia e R$0,15 por km  rodado

dias  = int(input('Dias alugados?:=>'))
km = float(input('Quantos Km rodados?:=>'))

pago = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de {pago:.2f}')