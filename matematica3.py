import math
n = float(input('Digite um número: '))
print(f'O número {n} tem a parte inteira {math.trunc(n)}\n')

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')

co1 = float(input('Comprimento do cateto oposto: '))
ca1 = float(input('Comprimento do cateto adjacente: '))
hi1 = math.hypot(co1, ca1)
print(f'A hipotenusa vai medir {hi1:.2f}\n')

a = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tang = math.tan(math.radians(a))
print(f'O ângulo {a} tem o SENO de {sen:.2f}, o COSSENO de {cos:.2f} e a TANGENTE de {tang:.2f}\n')

import random
al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')
lista = [al1, al2, al3, al4]
as1 = random.choice(lista)
print(f'O aluno sorteado foi {as1}\n')

all1 = input('Primeira aluna: ')
all2 = input('Segunda aluna: ')
all3 = input('Terceira aluna: ')
all4 = input('Quarta aluna: ')
lista1 = [all1, all2, all3, all4]
random.shuffle(lista1)
print(f'A aluna sorteada será \n')
print(lista1)

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('fox.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
