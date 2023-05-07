from Clases import ViajeroFrecuente

if __name__=='__main__':
    i = 0
    bul = False
    vf = []
    with open ('Viajeros frecuentes.txt') as archi:
        for line in archi:
            p, a, r, t, e = line.split(',')
            vf.append (ViajeroFrecuente(p, a, r, t, e))
            i = i + 1
    print ('Coloque:\na - Para consultar cantidad de millas\nb - Para acumular millas\nc - Para canjear millas')
    eleccion = input ('')
    NumViaj = input('Ingrese numero de viajero frecuente: ')
    if eleccion == 'a':
        j = 0
        while bul==False and j<i:
            bul = vf[j].buscar(NumViaj)
            j = j + 1
        if bul == False:
            print ('No se ha encontrado el numero de viajero buscado.\n')
        else:
            print ('Su cantidad de millas actuales son:', vf[j-1].cantidadTotalMillas(), '\n')
    elif eleccion == 'b':
        cantMoC = input ('Ingrese cantidad de millas: ')
        j = 0
        while bul==False and j<i:
            bul = vf[j].buscar(NumViaj)
            j = j + 1
        if bul == False:
            print ('No se ha encontrado el numero de viajero buscado.\n')
        else:
            print ('En nuevo total de millas acumuladas es: ', vf[j-1].acumularMillas(cantMoC), '\n')
    elif eleccion == 'c':
        cantMoC = input ('Ingrese cantidad de millas a canjear: ')
        j = 0
        while bul==False and j<i:
            bul = vf[j].buscar(NumViaj)
            j = j + 1
        if bul == True:
            marca = vf[j-1].canjearMillas (cantMoC)
            if marca != -1:
                print ('Canje realizado correctamente. Cantidad de millas acumuladas actualmente:', marca, '\n')
        else:
            print ('El numero de viajero ingresado no existe.\n')
    print ('\nFin del Programa...')