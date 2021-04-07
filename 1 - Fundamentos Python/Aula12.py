#Função do operador IN
'''
lista = ['Sabao','Pao','Cafe', 'Leite']
produto = input("Entre com um produto: ")
if produto not in lista:
    print(f"{produto} não está na lista")
#    nlista= input("Gostaria de adicionar a lista? ")
#    if nlista == "sim" :
#      lista.append(produto)
else:
    print("Não esqueça de comprar")
print(lista)
======================================================================
#Encontrar valores comuns em duas listas(usando for)
x = ['1','2','3','5']
y = ['2','3','4']
print(x,y)
for numeros in x:
    if numeros in y:
        print("{} é comum nas duas listas".format(numeros))
    else:
        print("{} não é comum nas duas listas".format(numeros))
======================================================================
#Outros identificadores
x = 'Cinco'
if (type(x) is int):
    print("Verdadeiro")
else:
    print("Falso")
----------------------------------
x = 'Cinco'
if (type(x) is not int):
    print("Verdadeiro")
else:
    print("Falso")
=======================================================================
#Acumuladores
lista =input("Entre com uma lista de inteiro: ")
lista_inteiro = lista.split()
contador = 0
for inteiro in lista_inteiro:
    contador += 1
print(f"Existem {contador} inteiros na lista")
======================================================================
#Calculando o fatorial (!) de um numero
n = int(input("Digite um numero nao negativo: "))
fatorial = 1
for i in range(1,n+1):
    fatorial *= i
print("{}!= {}".format(n,fatorial))
===============================================================
#Condição de parada
condicao = 10
soma = 1
while soma <= condicao:
    print("está é a {} vez no loop".format(soma))
    soma +=1
'''
    
