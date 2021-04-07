# try - exception
#numerador = int(input("Entre com o numerador: "))
#denominador = int(input("Entre com o denominador: "))
#if numerador % denominador == 0:
#    print("O numerador é divisivel pelo denominaodor")
#else:
#    print("A divisão não é inteira ")

# try:
#    numerador = int(input("Digite o numerador: "))
#except ValueError:
#    print("O valor não é inteiro")
#    exit(0)
#try:
#    denominador = int(input("Digite o denominador: "))
#except ValueError:
#    print("O valor não é inteiro ")
#    exit(0)
#try:
#    if numerador % denominador == 0:
#        print("O numerador é divisil pelo denominador")
#else:
#        print("A divisao não é inteira ")
#except ZeroDivisionError:
#    print("Denominador não pode ser zero")
# ===================================================
#idades = {'Tulio' : 18, 'Maria': 30, 'Bryan' : 7 }
#pessoa = input("Qual pessoa voce quer saber a idade?")
#idade = idades.get(pessoa)

# if idade:
#    print(f'{pessoa} tem {idade} anos de idade')
# else:
#    print("Idade desconhecida0")
# Com excessão
idades = {'Tulio': 18,'Bryan': 7,'Maria':30}
pessoa =input("Qual pessoa voce quer saber a idade?")
idade = idades.get(pessoa)
try:
    print(f"{pessoa} tem {idades[pessoa]} anos de idade")
except KeyError:
    print(f"{pessoa} Idade desconhecida")