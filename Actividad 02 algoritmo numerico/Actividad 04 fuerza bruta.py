
mesa = {
    "costo" : "200",
    "peso"  : "5"
}

refri = {
    "costo" : "700",
    "peso"  : "50"
    } 

plato = {
    "costo" : "13",
    "peso"  : "0.01"
    }

cama = {
    "costo" : "500",
    "peso"  : "20"
    }

tv = {
    "costo" : "100",
    "peso"  : "13"
    }

bocina = {
    "costo" : "350",
    "peso"  : "0.5"
    }

silla = {
    "costo" : "150",
    "peso"  : "3"    
    }

taza = {
    "costo" : "20",
    "peso"  : "0.15"
    }

tanque = {
    "costo" : "700",
    "peso"  : "35"
    }

cafetera = {
    "costo" : "150",
    "peso"  : "1.5"
    }

misItems = {
    "mesa" : mesa,
    "refri" : refri,
    "plato" : plato,
    "cama"  : cama,
    "tv"    : tv,
    "bocina": bocina,
    "silla" : silla,
    "taza"  : taza,
    "tanque": tanque,
    "cafetera":cafetera
    }

CAPACIDAD=80

mochila=[]

itemsOrdenadosPrecio = sorted(misItems.items(),key = lambda y: float(y[1]['peso']))

for item in itemsOrdenadosPrecio:
    if CAPACIDAD - float(item[1]['peso']) > 0:
        mochila.append(item)
        CAPACIDAD-=float(item[1]['peso'])

for item in mochila:
    print(item[0])
    print(item[1])
    print("\n")
    

print('Espacio libre en la mochila: ',CAPACIDAD,' Kg.')



