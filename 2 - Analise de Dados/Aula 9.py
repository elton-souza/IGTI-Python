#Regressão linear pt2 SCIKIT LEARN
from matplotlib import pyplot as plt
import numpy as np


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

#Transformando em numpy array
x,y = np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1)

#Modelo
from sklearn.linear_model import LinearRegression

#Treinando o modelo: y = a*x + b, valores reais (a,b) = (2,1)
reg = LinearRegression()
reg.fit(x,y)

#Coeficientes a,b estimados
#Valores estimados usando numpy diretamente...

print("A estimado:",reg.coef_.ravel()[0])
print('B estimado: ',reg.intercept_[0]) #modelo independente

#Predição do modelo
y_pred = reg.predict(x)

#Score do modelo
#Caracteriza se o modelo foi bom ou ruim para a base de dados
# quanto mais proximo de 1 é melhor, quanto mais perto 0 pior.
score = reg.score(x, y)
print("Score: ",score)

#Plot de dados
plt.figure(figsize=(10, 5))
plt.plot(x, y, '*', label = 'Dados originais')
plt.plot(x, y_pred, label = 'Regressao linear (R2: {:.3f})'.format(score))
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title = 'Regressão Linear'
plt.grid()
plt.show()
print(80*'=')

#Parte 2

plt.figure(figsize=(10, 5))
plt.plot(x, y, '*', label = 'Dados originais')
plt.plot(x, y_pred, label = 'Regressao linear (R2: {:.3f})'.format(score))
plt.hlines(y=y.mean(), xmin = x.min(),xmax=x.max(),linestyles='dashed',
           label='Modelo de referencia $R^2$')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title = 'Regressão Linear'
plt.grid()
plt.show()

#Função para o calculo do MSE
def mse(y_true, y_pred, is_ref = False):
    #MSE modelo
    if is_ref:
        mse = ((y_true - y_true.mean())**2).mean()
    else:
        mse = ((y_true - y_pred)**2).mean()
    return mse
#Função para o calculo do coeficiente de determinação R2
def r2(mse_reg,mse_ref):
    return 1 - mse_reg/mse_ref

#Visualizando y e y pred
print('y_true: ',y.ravel())
print('y_pred: ',y_pred.ravel())

#Calculando o mse dos modelos
mse_reg = mse(y_true=y,y_pred=y_pred)
print('MSE do modelo de regeressao: ', mse_reg)
mse_ref = mse(y_true=y, y_pred=y_pred, is_ref=True)
print('MSE dos modelo de referencia: ', mse_ref)

#Calculando o R2 score
r2_score = r2(mse_reg=mse_reg,mse_ref=mse_ref)
print('Coeficiente R2 do modelo implementado(calculado): ',r2_score)

#Score retornado pelo scikit lean
r2_score_skl = reg.score(x, y)
print('Coeficiente R2 do modelo implementado(Scikit Learn): ',r2_score_skl)


