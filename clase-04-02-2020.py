def cuenta_regresiva(pepsy):
    pepsy -= 1

    if pepsy > 0:
        print(pepsy)
        cuenta_regresiva(pepsy)
    else:
        print('Booooooooooooooom!')

    print('Fin de la funcion {}'.format(pepsy));


cuenta_regresiva(5)