valor_em_real = float(input('Quantos reais voce quer converter pra dolar? '))

valor_em_dolar = valor_em_real /6.11
valor_euro = valor_em_real /6.25
valor_iene = valor_em_real /0.04

print(f'O valor R${valor_em_real} equivale a \n ',
        f'US$ {valor_em_dolar:.2f} \n EUR {valor_euro:.2f} \n  JPY {valor_em_real:.2f} e')