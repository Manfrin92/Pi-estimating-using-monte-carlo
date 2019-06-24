import random
from random import uniform as uf
r = 0.5
caiu_dentro = 0
caiu_fora = 0
picalculado = float()
piReal = 3.141
testes = 500000

for x in range(0,testes):
    xAleatorio = uf(-0.5, 0.5)
    yAleatorio = uf(-0.5, 0.5)

    soma = (xAleatorio**2 + yAleatorio**2)**0.5

    if soma <= r:
        caiu_dentro += 1

    else:
        caiu_fora += 1
print('\n')
print('Caiu dentro '+ str(caiu_dentro) +' vezes')
print('Caiu fora '+ str(caiu_fora) +' vezes')


picalculado = caiu_dentro * 4 / testes

print('\n')
print('pi calculado foi ' + str(picalculado))
print('\n')
print('erro de ' + str(picalculado-piReal))

print(testes)
print(caiu_dentro+caiu_fora)
