archivo = open("texto.txt", mode='r', encoding='UTF-8')
texto = archivo.read()

arregloLetras = []

for letra in texto:
    arregloLetras.append(letra)

diccionarioLetras = {}

for caracter in arregloLetras:
    if caracter in diccionarioLetras:
        diccionarioLetras[caracter] += 1
    else:
        diccionarioLetras[caracter] = 1

diccionario_ordenado = sorted(diccionarioLetras.items(),key=lambda item: item[1])

print(diccionario_ordenado)