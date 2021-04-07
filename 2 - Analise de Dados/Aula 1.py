#Importar biblioteca numpy
import numpy as np

print('Array 1D')
l = [1,2,3]  # dtype = (int,float,..) forca o tipo de dado
x = np.array(l)
print("x:", x)
print("shape:", x.shape)

# print(type(x))
print('')

print('Array 2D')
ls = [[1,2],[3,4]]
z = np.array(ls)
print("z:\n",z)
print("Shape:",z.shape)

print('')

print('Array contendo apenas Zeros: ')
dim = (2, 2) # Linhas , colunas
a = np.zeros(dim)
print('a:\n', a)
print('Shape:', a.shape)

print('')

print('Array contendo apenas numero um: ')
size = (2, 2) #Recebe tuplas
e = np.ones(size)
print('e:\n', e)
print('Shape: ',e.shape)

print('')

print('Criacao de valores dentro de um intervalo ')
# Valores uniformes entre 5 e 15
c_min,c_max = 5, 15
c = np.linspace(start=c_min,stop=c_max, num=6)#num define a quantidade de numeros que devem ser mostrado em tal intervalo
print('c: ', c)
print('Shape: ', c.shape)

print('Criacao de matriz identidade:')
v = 2
b = np.eye(v)
print('b: \n',b)
print('Shape: ',b.shape)

print('')

print('Criacao de valores aleatorios: ')
#np.random.seed(10) -
h = np.random.random(size=(2,3)) # Valores aleatorios entre 0 e 1(floats) em um array de 2x3.
print('h:\n',h)
print('Shape: ',h.shape)