import random
from random import uniform as uf
r = 0.5
caiu_dentro = 0
caiu_fora = 0
picalculado = float()
piReal = 3.141
testes = 50000

for x in range(0,testes):
    xAleatorio = uf(-0.5, 0.5)
    yAleatorio = uf(-0.5, 0.5)

    soma = (xAleatorio**2 + yAleatorio**2)**0.5

    if soma <= r:
        caiu_dentro += 1

    else:
        caiu_fora += 1
print('\n')
print('The point was within the circle '+ str(caiu_dentro) +' times.')
print('The point was outside the circle '+ str(caiu_fora) +' times.')


picalculado = caiu_dentro * 4 / testes

print('\n')
print('The estimated pi was ' + str(picalculado))
print('\n')
print('And that corresponds to an error of ' + str(picalculado-piReal))

