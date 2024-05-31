from math import sqrt

print('Vamos a resolver una ecuación de segundo grado')
print(' ax^2 + bx + c = 0 \n')

a = float(input('Ingrese el coeficiente a: '))
b = float(input('Ingrese el coeficiente b: '))
c = float(input('Ingrese el coeficiente c: '))

discriminante = b ** 2 - 4 * a * c

if discriminante < 0:
    print('La ecuación no tiene soluciones reales.')
else:
    raiz = sqrt(discriminante)
    x_1 = (-b + raiz) / (2 * a)
    if discriminante != 0:
        x_2 = (-b - raiz) / (2 * a)
        print(f'Las soluciones son {x_1} y {x_2}')
    else:
        print(f'La solución es {x_1}')
