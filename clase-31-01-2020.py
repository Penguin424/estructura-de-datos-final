def max(n1, n2):
    if n1 > n2:
        print('El numero {} es mayor que el numero {}'.format(n1, n2))

    elif n1 < n2:
         print('El numero {} es mayor es que el numero {}'.format(n2, n1))

    else: 
        print('Eso no es un numero amigo')

def max_de_tres(n1,n2,n3):

    if n1 > n2 and n1 > n3:
        print('El numero mas grande de los tres es {}'.format(n1))

    elif n2 > n1 and n2 > n3:
        print('El numero mas grande de los tres es {}'.format(n2))

    elif n3 > n1 and n3 > n2:
        print('El numero mas grande de los tres es {}'.format(n3))

    else:
        print('Eso no es un numero amigo')

def len_fake(pepsy):
    longitud = 0

    for i in pepsy:
        longitud += 1

    return  longitud

print(len_fake('Hola'))
    
max_de_tres(1,10,2)

max(1,5)

