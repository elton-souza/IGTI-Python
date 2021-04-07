#Funções
''''
===========================================

def equacao_reta(x):
    y_x = 2 * x + 1
    return y_x
x = float(input("Entre com o valor a ser calculado para y(x) = 2x+1: "))
resultado = equacao_reta(x)
print("O resultado encontrado foi Y = %.0f" %resultado)

============================================
'''
def equacao_reta(X):
    y_x = 2 * X + 1
    return y_x

lista_x = [1,2,3,4,5,6]
lista_y = []
for valor_x in lista_x:
    lista_y.append(equacao_reta(valor_x))
    
for valor_x,valor_y in zip(lista_x,lista_y):
    print("O valor de y(%0.1f) = %0.1f"%(valor_x,valor_y))