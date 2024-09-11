from random import randint
from time import sleep

print('=*='*19)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('=*='*19)
reps = 's'

while reps == 's':
    resp = randint(0,5)
    n = int(input('Em que numero pensei? '))
    print('PROCESSANDO...')
    sleep(3)# Deixa o computador "pensando"/ da um tempinho de intervalo
    

    if n == resp:
        print('PARABENS! Você conseguiu me vencer!')
        reps = input('Deseja tentar mais uma vez?[S/N] ').lower()
        print('=*='*19)
    else:
        print('GANHEI! Eu pensei no numero {} e nao no {}'.format(resp, n))
        reps = input('Deseja tentar mais uma vez?[S/N] ').lower()
        print('=*='*19)