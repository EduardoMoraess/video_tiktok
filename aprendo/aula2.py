n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('=' * 90)

print(f'A soma é {s}, o produto é {m} e a divisão é {d:.2f}', end='')
print(f'A divisão inteira é {di} e a potência é {e}')

print('='*90)