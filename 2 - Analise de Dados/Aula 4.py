import numpy as np
'''
#Comparações
x = np.array([[1,2],[3,4]])
y = np.array([1.5,3.5])
print("x:\n",x)
print("y:\n",y)

print("Comparação de um array com um escalar (>):\n",x > 2)
print("Comparação de um array com escalar (>=):\n",x >= 2)
print("Comparação de um array com escalar (<):\n",x < 2)
print("Comparação de um array com escalar (<=):\n", x <= 2)
print("Comparação entre arrays(==):\n", x == x)
print("Comparação entre arrays(>):\n", x > x)
print("Comparação entre arrays(<):\n", x < x)
print("Comparação entre arrays(>):\n",x > y)
'''

#Indexação booleana
x = np.array([[1,3,7],[4,11,21],[42,8,9]])
print("x:\n",x)
k = 10
cond = x > k
print("Condição:\n",cond)
print(f"Elementos maiores que {k}: ",x[cond])
print(f"Numero de elementos maiores que {k}: ",len(x[cond]))

#Indexação de numeros pares
cond = x % 2 == 0
print("Condição:\n",cond)
print("Numeros pares:",x[cond])
