#PANDAS
import pandas as pd
#Leitura de dados

#CSV
df = pd.read_csv("C:/Users/Elton/Downloads/temperature.csv") #ou o caminho do arquivo na maquina local

#==================================================================================

#EXCEL
#2 abas(worksheets)
#leitura do arquivo odo
ex = pd.ExcelFile("C:/Users/Elton/Downloads/temperature.xlsx")  #ou o caminho do arquivo na maquina local

#==================================================================================
print('Leitura da primeira aba (sheet1)')

#Dados numéricos com separador decimal = "."
df2 = pd.read_excel(ex, sheet_name = "Sheet1", )
print(df2)
print(50*"=")

#==================================================================================
print('Leitura da segunda aba (Sheet2)')

#Dados numericos com separador decimal = ","
df3 = pd.read_excel(ex, sheet_name = "Sheet2")#, decimal=",")
print(df3)
#print(df3.dtypes)
print(50*"=")

#==================================================================================
print('Visualizar linhas do dataframe')

n = 3
print(df.head(n)) #N primeiras linhas
print("")
print(df.tail(n)) #N ultimas linhas
print("")
# print(df.dtypes)  #Visualizar os tipos de dados do dataframe
#print(50*"=")
print(df.describe()) # Estatiscas basicas de todos os atributos numéricos
print("")
print(df.info()) # Especificações dos dados
print(50*"=")

#====================================================================================
print('Visualizar colunas')

print(df.head())
print("")
print(df['date']) #Ira mostrar a coluna especificada
print("")
print(df[['date','temperatura']]) # ira mostrar uma lista de colunas
print("")
print(df.columns) # Verifica o nome as colunas
#df.columns = ['col1','col2','col3'] # Renomear o nome das colunas
#print(df.columns)


print(50*"=")
#====================================================================================
print('Indexação')

print(df[['temperatura']]) # Irá indexar a coluna temperatura
print("")
print(df[['temperatura','classification']]) #Irá indexar uma lista de colunas
print(50*"=")

#====================================================================================
print('Método iloc')

print(df.iloc[1,2]) #Irá mostrar um dado especifico atraves do indice e da coluna
print("")
print(df.iloc[1:4,0:2]) #Mostrar mais de um elemento simultaneamente
print("")
print(df.iloc[:,1]) #Todas as linhas da coluna tal
print(50*"=")

#====================================================================================
print('Método loc')

print(df.loc[5,'temperatura']) #Mostra um dado especifico atraves do nome da linha e da coluna
print("")
print(df.loc[:,'temperatura':  ])
print(50*"=")

#====================================================================================
print('Indexação Booleana')

print(df[df['classification'] == 'quente'])
print("")
print(df.loc[df['classification']=='quente','temperatura'])
print("")
print(df.dtypes)
df['date'] = pd.to_datetime(df['date']) #Transformando a coluna date(object) para datetime
print(df.dtypes)
print("")
df = df.set_index('date')#Transformar a coluna 'date' em um indice
print(df.head())
print("")

#Selecionar exemplos acima de 25 graus
print(df[df['temperatura']>=25])

#Selecionar entradas até Março de 2020
print(df[df.index <= '2020-03-01']) # é valido apenas para datetime, se estiver em object não funciona

#Selecionar entradas até Março de 2020. Slicing na coluna classification
print(df.loc[df.index <= '2020-03-01',['classification']])
#ou
print(df.iloc[df.index <= '2020-03-02', [-1]])

#====================================================================================

print("Ordenação")
help(df.sort_values)

#Ordenação crescente por uma coluna
print(df.sort_values(by='temperatura'))
print("")
print(df.sort_values(by='classification'))
print('')
#Ordenação por mais de uma coluna
print(df.sort_values(by=['classification','temperatura']))
print(50*"=")
#Ordenação decrescente por uma coluna
print(df.sort_values(by='classification',ascending=False))
print(50*"=")
#Ordenação crescente pelo indice
print(df.sort_index())
print(50*"=")
#Ordenação decrescente pelo indice
print(df.sort_index(ascending=False))
#====================================================================================

#Visualização de dados
print(df.plot) #Plot de linhas
print(50*"=")
#Plot de linhas(Tamanho)
print(df.plot(figsize=(10,10)))
print(50*"=")
#Plot de linhas: grid - Referencia de valores
print(df.plot(figsize=(10,10), grid=True))
print(50*"=")
#Plot de linhas: Style
print(df.plot(style='-o',figsize=(10,5),grid=True)) #Visualização com ponto e traçado
#print(df.plot(style='-',figsize=(10,5),grid=True))
#print(df.plot(style='-.',figsize=(10,5),grid=True))
print(50*"=")

#Plot de linhas: linewidth - Aumenta o tamanho do tracejado
print(df.plot(style = 'o',linewidth = 2.5, figsize=(10,5),grid =True))
print(50*"=")
#Plot de linhas: Cor
print(df.plot(style = 'o',linewidth = 2.5,color ='red',figsize =(10,5),grid=True))
print(50*"=")
#Plot de barras
df['classification'].value_counts().plot.bar(figsize=(10,5),rot=0) #Retorna a quantidade de ocorrencias em tal coluna - Será mostrado em forma de barras
print(50*"=")
print(df.plot(kind = 'bar',figsize=(10,5),rot=30))
#====================================================================================

#Método groupby - ultilizado para fazer agrupamento de valores unicos de uma ou mais colunas
print(df.groupby(by='classification'))
print(50*"=")
print(df.groupby(by='classification').mean()) #Tirar média de uma coluna agrupada
print(50*"=")
print(df.groupby(by='classification').sum()) #Somar
print(50*"=")

#Remoção de uma coluna:
print(df.drop('temperatura',axis=1)) #Deletar a coluna temperatura ao longo do eixo 1
print(50*"=")

# Copia de um dataframe:evita compartilhamento de memoria
#sem copy(), operações inplace de df2 tambem alteram df
df2 = df.copy()
print(df2.head()) #Faz uma copia para outro dataframe
print(50*"=")
df3 = df2.drop('temperatura',axis=1)#inplace substitui o objeto que esta sendo chamado e sobrescreve
print(df3.head())
f3 = df2.drop('temperatura',axis=1,inplace=True) #inplace substitui o objeto que esta sendo chamado e sobrescreve
print(df2.head())
print(df.head()) # Não é alterados