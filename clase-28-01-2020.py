def suma(n1,n2):
    return n1 + n2

def rest(n1,n2):
    return n1 - n2

def multi(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

def area(lado):
    return lado**2

def perimetro(lado):
    return lado*4

num1 = 5
num2 = 8

res0 = suma(num1, num2)
res1 = rest(num1, num2)
res2 = multi(num1, num2)
res3 = div(num1, num2)

print(res0)
print(res1)
print(res2)
print(res3)

print("\n")

lado = int(input("Ingresa el lado del cuadrado: "))

area_r = area(lado)
perimetro_r = perimetro(lado)

print("\nEl area del cuadrado es {} y el perimetro es {}".format(area_r, perimetro_r))