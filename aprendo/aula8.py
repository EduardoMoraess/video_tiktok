largura_parede = float(input('digite a altura da parede:=>'))
altura_parede = float(input('Digite a altura da parede:=>'))

area = largura_parede * altura_parede

print(f'Sua parede tem dimensão de {largura_parede}x{altura_parede} e sua area é de {area:.1f}m².')
lata_tinta = area /2

print('='*58)
print(f'Para pintar essa parede, voce precisara de {lata_tinta}l de tinta')