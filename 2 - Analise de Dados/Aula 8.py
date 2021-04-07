import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


df = pd.read_csv("C:/Users/Elton/Downloads/temperature.csv")
print(df.head())

#Extração de X e Y
x,y = df[['temperatura']].values, df[['classification']].values
print('x:\n',x)
print('y:\n',y)

#Prós processamento
from sklearn.preprocessing import LabelEncoder #Codifica uma entrada como um valor numerico
#print((LabelEncoder))

#Conversao de y em valores numericos
le = LabelEncoder()
y = le.fit_transform(y.ravel())
print('y:\n',y)

#Modelo
from sklearn.linear_model import LogisticRegression

#Classificador
clf = LogisticRegression()
clf.fit(x,y)

#Gerando 100 valores de temperatura linearmente espaçados entre 0 e 45
x_test = np.linspace(start = 0,stop = 45, num = 100).reshape(-1,1)
#Predição desses valores
y_pred=clf.predict(x_test)
 #print(y_pred)
#Conversao de y pred para valores originais
y_pred = le.inverse_transform(y_pred)
#print(y_pred)
#print(x_test)

#output
output = {'new_temp': x_test.ravel(),
          'new_class': y_pred.ravel()}
output = pd.DataFrame(output)

#print(output.head())
#print(output.tail())

#Estatisticas
print(output.info)
print(output.describe())

#Contagem de valores gerados
output['new_class'].value_counts().plot.bar(figsize=(10,5),
                                            rot=0,
                                            title='#de novos valores gerados');

#Distribuição do output produzido
#Conseguimos inferir  a classificação novas temperaturas
#a partir  de um dataset com 6 exemplos
output.boxplot(by='new_class', figsize=(10, 5))
print(80*'=')
plt.show()
#Sistema automatico
def classify_temp():
    '''Classificaça o input do usuario'''
    ask = True
    while ask:
      #input de temperatura
        temp = input("Insira a temparatura(graus celsius): ")
      #Transformar para numpy array
        temp =  np.array(float(temp)).reshape(-1,1)
      #Realizar classificação
        class_temp = clf.predict(temp)
      #Transformação inversa  para retorna string original
        class_temp = le.inverse_transform(class_temp)
      #Classificação
        print(f'A classificação da temperatura {temp.ravel()[0]} é:', class_temp[0])
      #Perguntar
        ask = input('Nova classificação(y/n): ') == 'y'

classify_temp()


