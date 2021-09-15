n = int(input('Digite um valor: '))
d = n * 2
t = n * 3
rq = n ** (1/2)
print(f' O dobro de {n} é igual a {d} \n o triplo é igual a {t} \n a raíz quadrada é {rq:.2f}')

no1 = float(input('1º nota do aluno: '))
no2 = float(input('2º nota do aluno: '))
m = (no1 + no2) * 0.5
print(f' A média do aluno será {m}')

metro = float(input('Uma distância em metros: '))
cm = metro * 100
mm = metro * 1000
hm = metro / 100
km = metro / 1000
print(f'A medida {metro} metros em centímetros é {cm} e em milímetros {mm}\nem hectômetro é {hm} e em quilômetros é igual a {km}')

nt = int(input('Digite um número para ver sua tabuada: '))
nt1 = nt * 1
nt2 = nt * 2
nt3 = nt * 3
nt4 = nt * 4
nt5 = nt * 5
nt6 = nt * 6
nt7 = nt * 7
nt8 = nt * 8
nt9 = nt * 9
nt10 = nt * 10
print(f'{nt} x  1 = {nt1}')
print(f'{nt} x  2 = {nt2}')
print(f'{nt} x  3 = {nt3}')
print(f'{nt} x  4 = {nt4}')
print(f'{nt} x  5 = {nt5}')
print(f'{nt} x  6 = {nt6}')
print(f'{nt} x  7 = {nt7}')
print(f'{nt} x  8 = {nt8}')
print(f'{nt} x  9 = {nt9}')
print(f'{nt} x 10 = {nt10}\n')



dc = float(input('Quanto dinheiro você tem na carteira? R$'))
dol = dc / 5.25
eur = dc / 6.17
lib = dc / 7.10
pa = dc * 18.55
print(f'Com R${dc} você tem US${dol:.2f}, £{lib:.2f}, €{eur:.2f} e ${pa:.2f}')

larg = float(input("Largura da parede: "))
alt = float(input("ALtura da parede: "))
area = larg * alt
print(f"Sua parede tem a dimensão de {larg}x{alt} e sua área é {area}m2")
tinta = area / 2
print(f"Para pintar a parede, será necessário {tinta}l de tinta")