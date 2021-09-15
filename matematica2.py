pp = float(input('Qual é o preço do produto? R$'))
desc = pp - (pp * 8/100)
print(f'O produto custava R${pp:.2f}, na promoção com desconto de 8% vai custar R${desc:.2f}.\n')

s = float(input('Qual é o seu salário? R$'))
sa = s + (s * 15/100)
print(f'Com 15% de aumento, seu salário ficará R${sa:.2f}\n')

pp1 = float(input('Qual o valor do produto? R$'))
pd = pp1 - (pp1 * 5/100)

pa = pp1 + (pp1 * 8/100)
print(f'O produto com valor R${pp1:.2f}, com pagamento à vista irá custar R${pd:.2f}, com pagamento parcelado será R${pa:.2f}\n')

c = float(input('Informa a temperatura em ºC:'))
f = 9 * c / 5 + 32
print(f'A temperatura {c}ºC corresponde a {f}ºF\n')

km1 = float(input('Quantos Km o carro percorreu? '))
d1 = int(input('Quantos dias o carro ficou alugado? '))
km = 0.15
d = 60
km2 = km1 * km
d2 = d1 * d
print(f'Alugando o carro por {d1} dias e percorrendo {km1:.1f}Km, o total a ser pago será R${km2 + d2:.2f}')
