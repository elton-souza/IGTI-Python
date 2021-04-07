# Argumentos em python
'''
def concatena_nome_mensagem(nome,mensagem): #A função possui dois parametros
    print("Olá,"+nome+"! "+mensagem)
a = input("Digite seu nome: ")
b = input("Digite seu nome: ")
concatena_nome_mensagem(a,"Bom dia")
concatena_nome_mensagem(b, "BOM DIA")

=====================================================
# 3 FORMAS DISTINTAS DE ARGUMENTOS
 #Default
def concatena_nome_mensagem(nome,mensagem="Bom dia"): # A função possui dois parametros e um deles já tem um valor de inicio(Padrão)
    print("Olá,"+nome+"! "+mensagem)

concatena_nome_mensagem("Elton")

 #Posição
def concatena_nome_mensagem(nome,mensagem): # A função possui dois parametros e um deles já tem um valor de inicio(Padrão)
    print("Olá,"+nome+"! "+mensagem)

concatena_nome_mensagem("Bom dia","Elton")

 #Argumentos arbitrários
def print_nomes_dos_usuarios(*nomes): #a função possui n parametros
    for nome in nomes:
        print("Olá,"+nome+"! Bom dia")
print_nomes_dos_usuarios('Elton','Sandro','Pedro')

def minha_funcao(**var):
    print(str(var))
minha_funcao(a = 12, b = 13, c ='ABC')
'''
