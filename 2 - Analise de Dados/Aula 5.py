#Outras operacoes com NUMPY
import numpy as np
x = np.array([[1,3,7],
              [4,11,21],
              [42,8,9]])
print("X:\n",x)
print(20*"=")
print("Transformacao de um array:\n",x.reshape(1,9)) #Refaz o array nessa condicao (9 linhas e 1 coluna)
print(20*"=")
#Transposicao de matriz(linha em coluna e coluna em linhas) .T
print("X transporta: \n",x.T)
print(20*"=")
#.num em um tal eixo
print("A soma de todos os elememtos de x:",np.sum(x))
print("A soma de x ao longo das linhas:",np.sum(x, axis=0))
print("A soma de x ao longo das coluanas:",np.sum(x,axis=1))
print(20*"=")
#.mean e a media dada em um eixo
print("A media total do eixo x:",np.mean(x))
print("A media total de x ao longo das linhas:",np.mean(x, axis=0))
print("A media total de x ao longo das colunas:",np.mean(x,axis=1))
#np.median - retorna a mediana ao longo de um eixo
print(20*"=")
#np.where, identificacao dos indices onde uma dada condicao e atendida. Uso conjunto com indexacao booleana. tbm acessa os indicies das linhas e colunas
cond = x % 2 == 0
print("Condicao: \n",cond)
i,j = np.where(cond)
print("Indice i (linhas):",i)
print("Indice j (Colunas):",j)
print(20*"=")

#Indexaçao booleana e slicing: selecionar as linhas de x que possuem algum numero par
print("x:\n",x)
cond = x % 2 == 0
print("Condicao:\n",cond)
i_row = np.where(np.sum(cond, axis=1)) [0] #So retorna as linhas
print("Indicies das linhas  que possuem numeros pares:",i_row)
print("linhas que possuem numeros pares:\n",x[i_row, :])
