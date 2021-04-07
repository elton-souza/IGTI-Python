'''
#Adicionando arquivos no google colab
from google.colab import files
uploaded = files.upload()
'''
#Lê o arquivo
nome_do_arquivo = input("Digite o nome do arquivo: ")
arquivo=open(nome_do_arquivo,"r")
for linhas in arquivo:
    print(linhas)
arquivo.close()
