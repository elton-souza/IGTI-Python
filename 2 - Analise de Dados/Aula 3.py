import numpy as np
'''
                         #Operações aritméticas
#Criação de dois arrays
x = np.ones((2,2)) #Podendo criar um array com apenas um numero multiplicando pelo numero que desejado
y = np.eye(2)
print("x:\n", x)
print("y:\n", y)
print("20*=")

#Soma
print("A soma de dois arrays:\n",x + y)
#Soma(Broadcasting)
print("A soma do array x:\n", x + 2)
print("A soma do array y:\n", y + 2)
print("20*=")

#Subtração
print("A subtração dos arrays:\n", x - y)
#Subtração(Broadcasting)
print("A subtração do array x:\n", x - 2)
print("A subtração do array y:\n", y - 2)

#E assim sucessivamente...

#Momentos em que o Broadcasting não funciona:
    #Quando os arrays não sao consistentes

#Combinando operações
print("Combinando as operações:\n", (x+y)/(x-2))


#Operações matriciais
x = np.ones((2,2))
x *=2
y = np.eye(2)
print("x:\n", x)
print("y:\n", y)

print(20*"=")

print("Multiplicação matricial(np.dot):\n", np.dot(x,y))
print("Multiplicação matricial(@):\n", x @ y)
print("Multiplicação matricial(.dot):\n", x.dot(y))
'''
A = np.array([[1,2],[3,-2]])
c = np.array([[7],[-11]])
print("A:\n",A)
print("c:\n",c)

#Resolução
x = np.dot(np.linalg.inv(A),c)
print("(a,b):",x.ravel())
