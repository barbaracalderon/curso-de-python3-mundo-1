# Crie um módulo chamado moeda.py que tenham as funções incorporadas aumentar(), diminuir(),
# dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
num = float(input('Digite o preço: R$'))
print(f'Aumentando 25% de {moeda.formato(num)} temos o preço de {moeda.formato(moeda.aumentar(num))}')
print(f'Diminuindo 25% de {moeda.formato(num)} temos o preço de {moeda.formato(moeda.diminuir(num))}')
print(f'O dobro de {moeda.formato(num)} é {moeda.formato(moeda.dobro(num))}')
print(f'A metade de {moeda.formato(num)} é {moeda.formato(moeda.metade(num))}')
