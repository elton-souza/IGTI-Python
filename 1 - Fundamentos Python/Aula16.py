# Desenvolvimento TOP_DOWN , BOTTOM_UP
#A linguagem python usa o desenvolvimento bottom_up
'''
===============================================================
#Exemplo TOP_DOWN
l = input("ENTRE COM UMA LISTA DE NUMEROS: ")
lista = []
for x in l.split():
    lista.append(int(x))
print(lista)
===============================================================
'''
#Exemplo Bottom_UP
def verifica_div(x,y):
    return int(y) % int(x) == 0

def elementos_div(x,lista):
    resultado = []
    for elemento in lista:
        if verifica_div(elemento,x):
            resultado.append(elemento)
    return resultado

def divisores_lista(lista):
    for elemento in lista:
        print(elemento, "é divisivel por ", end="")
        elementos = elementos_div(elemento, lista)
        for f in elementos:
            print(f, end=" ")
        print()

s = input("Entre com uma lista de valores: ")
lista_val = []
for x in s.split():
    lista_val.append(int(x))
divisores_lista(lista_val)

