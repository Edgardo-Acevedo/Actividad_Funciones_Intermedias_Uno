import random
arr = []
MaximoPorDefecto = 100
MinimoPorDefecto = 0
def randInt(Minimo = MinimoPorDefecto, Maximo = MaximoPorDefecto):
    if(type(Minimo) == int and type(Maximo) == int and Minimo < Maximo):
        print(f'El Mínimo es {Minimo} y el Máximo es {Maximo}')
        for a in range(Minimo, Maximo, 1):
            arr.append(a)    
            numero = arr
            numero = random.random()*100
            redondeo = round(numero, 0)
        print(f'Su número aleatorio es {redondeo}')
    if(type(Minimo) != int and type(Maximo) != int):
        print("Estos no son números, así que serán devueltos los números aleatorios pór defecto.")
        for a in range(MinimoPorDefecto,MaximoPorDefecto,1):
            arr.append(a)    
            numero = arr
            numero = random.random()*100
            redondeo = round(numero, 0)
        print(f'Su número aleatorio es {redondeo}')
    if(type(Minimo) == int and type(Maximo) != int):
        print("Solo hay un valor Mínimo")
        for a in range(Minimo,MaximoPorDefecto,1):
            arr.append(a)
            numero = arr
            numero = random.random()*100
            redondeo = round(numero, 0)
        print(f'Su número aleatorio es {redondeo}')
    if(type(Minimo) != int and type(Maximo) == int):
        print("Solo hay un valor Mínimo")
        for a in range(MinimoPorDefecto,Maximo,1):
            arr.append(a)
            numero = arr
            numero = random.random()*100
            redondeo = round(numero, 0)
        print(f'Su número aleatorio es {redondeo}')
randInt(Minimo = 2, Maximo = 5)
randInt(Minimo = '', Maximo = 10)
randInt(Minimo = 2, Maximo = '')
randInt(Minimo = '', Maximo = '')
