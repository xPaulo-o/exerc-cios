import math

def bhaskara(a, b, c):
    delta = (b**2) - 4*a*c
    delta =  delta ** (1/2)
    x1 = (-b + delta) / 2
    x2 = (-b - delta) / 2
    dic = {'x1': x1, 'x2': x2}
    return dic

try:
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    raizes = bhaskara(a, b, c)
    print("As raízes da equação são: ",raizes)

except ValueError:
    print("Por favor, insira valores numéricos válidos.")