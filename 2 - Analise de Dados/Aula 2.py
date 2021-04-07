#Acessar elementos
import numpy as np

x = np.linspace(start = 10, stop = 100, num = 10)
print("x: ", x)
print("Shape: ",x.shape)
print('''
Primeiro numero é: {}
Segundo numero é: {}
Terceiro numero é: {}
Ultimo numero é: {}
'''.format(x[0],x[1],x[2],x[9]))

#Slicing
print("x: ",x)
print("Os cincos primeiros mumeros: ", x[0:5])
print("Os dois primeiros numeros: ", x[:2])
print("Os dois ultimos numeros: ", x[-2: ])

print('')

#Acessando elementos D2
x = x.reshape(2, 5) # reshape(remodelar) de x para 2 linhas e 5 colunas
print("x:\n ", x) 
print(f'''
Primeira linha, segunda coluna: {x[0,1]}
Segunda lina, penultima coluna: {x[1,-2]}
Ultima linha, ultima coluna: {x[1,-4]}
Ultima linha, ultima coluna: {x[-1, -1]}
''')

#Slicing
print("x:\n",x)
print(f'''
Primeira linha inteira: {x[0,:]}
Primeira linha, segunda ate a quarta coluna: {x[0,1:4]}
Ultima coluna inteira:\n {x[:,[-1]]}
''')

#Compartilhamento de memoria
a = np.array([1,2,3,4])
print("A:", a)
z = a[0:4].copy()
z[0] = -90
print("Z:",z)
print("A:",a)
 #Se não for usado o metodo copy(), o array principal(a) será alterado.

 
