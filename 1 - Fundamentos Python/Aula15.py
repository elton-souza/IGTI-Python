#Stack (Pilha)
def inverte_string(valor_string):
    resultado = ""
    for caracter in valor_string:
        resultado = caracter + resultado
    return resultado

string = input("Entre com uma string:  ")
while string.strip() != "":
    print("O inverso de {} é {}.".format(string,inverte_string(string)))
    string=input("Entre com um uma string ou aperte ENTER para sair: ")

''''
def verifica_div(x,y):

     return x % y == 0

x = int(input("Digite um numero: "))
y = int(input("Digite outro numero: "))

if (verifica_div(x,y)):
    print(x, "é divisivel por ",y)
else:
    print(x ,"não é divisivel por", y)
'''