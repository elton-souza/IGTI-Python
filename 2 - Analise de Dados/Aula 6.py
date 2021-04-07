#Regressão linear numpy

#Visualização de dados
from matplotlib import pyplot as plt

#dados
x = [1, 2 ,3 ,4 , 5, 6]
y = [10, 50 , 100, 150, 200, 250]

#plot dos dados
plt.figure(figsize=(10,5))
plt.plot(x,y,'o',label = 'Dados originais')
plt.legend()
plt.xlabel("x")
plt.ylabel("Y")
plt.grid()
plt.show()

'''
Iremos estimar uma funçao do tipo : y = ax+b, ou seja
devemos achar quais valores de a e b que melhor representa os dados

Os valores reais de a e b são (2,1)
'''
#Trnsformando para numy e vetor coluna
x, y = np.array(x).reshape(-1,1), np.array(y).reshape(-1,1)

#Adicioanando bias: para estimar o termo b:
X = np.hstack((x,np.ones(x.shape))) #np.hstack - concatena dois arrays horinzontalmente

#Estimando a e b
beta = np.linalg.pinv(x).dot(y)
print("a estimado: ",beta[0][1])
print("b estimado: ",beta[0][1])

#plot de dados
plt.figure(figsize=(10,5))
plt.plot(x,y,'o',label="Dados originais")
plt.plot(x,X.dot(beta),label="Regressao linear")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regressão linear com numpy")
plt.grid()
plt.show()
