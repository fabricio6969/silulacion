import random
import matplotlib.pyplot as plt
import numpy as np
def dado(n):
    i = 1
    dos =0
    tres =0
    cuatro =0
    cinco=0
    seis =0
    siete=0
    ocho=0
    nueve=0
    diez=0
    once=0
    doce=0
    cont = [0,0,0,0,0,0,0,0,0,0,0]
    while i <= n:
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        #print("Resultado del primer dado es: ",r1)
        #print("Resultado del segundo dado es: ",r2)
        suma = r1 +r2
       # print("Sumatoria de dados ------->",suma)
        for j in range(2, 13):
                if suma == j:
                    cont[j-2] = cont[j-2] + 1
        i += 1
        dividendo =1
        if suma == 2:
            dividendo=1
            dos +=1
        elif suma ==3:
            dividendo=2
            tres +=1
        elif suma ==4:
            dividendo=3
            cuatro +=1
        elif suma ==5:
           dividendo=4
           cinco +=1
        elif suma ==6:
            dividendo=5
            seis +=1
        elif suma ==7:
            dividendo=6
            siete +=1
        elif suma ==8:
            dividendo=5
            ocho +=1
        elif suma ==9:
            dividendo=4
            nueve +=1
        elif suma ==10:
            dividendo=3
            diez +=1
        elif suma ==11:
            dividendo=2
            once +=1
        elif suma ==12:
            dividendo=1
            doce +=1
        frecuencia = dividendo/36
       # print("La frecuencia es : ", frecuencia)
       
    print("la suma de dos se repitio",dos)
    print("la suma de tres se repitio",tres)
    print("la suma de cuatro se repitio",cuatro)
    print("la suma de cinco se repitio",cinco)
    print("la suma de seis se repitio",seis)
    print("la suma de siete se repitio",siete)
    print("la suma de ocho se repitio",ocho)
    print("la suma de nueve se repitio",nueve)
    print("la suma de diez se repitio",diez)
    print("la suma de once se repitio",once)
    print("la suma de doce repitio",doce)
    print("fin")
    etiqueta = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    plt.xticks(range(len(cont)), etiqueta)
    plt.xlabel('Sumas')
    plt.ylabel('Probabilidad')
    plt.title('Simulación suma Dados')
    plt.bar(range(len(cont)), cont) 
    plt.show()
    
    
dado(100)
dado(1000)
dado(10000)


