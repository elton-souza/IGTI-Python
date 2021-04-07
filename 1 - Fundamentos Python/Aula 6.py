# if condicional or
#altura = int(input("Digite sua altura em centimetros: "))
#if (altura < 150) or (altura > 180):
#    print('Voce nao pode brincar')
#else:
#    print("Voce pode brincar!")

#Adivinhando resultado da divisao
#numerador = float(input("Digite o valor do numerador: "))
#denominador = float(input("Digite o valor do denominaodr: "))
#resultado = numerador / denominador

#chute = float(input("Qual seu chute para o resultado da divisao? "))
#maior = abs(resultado)

#if abs((chute - resultado)/maior) <=0.1:
#    print("Voce acertou! Parabens")
#else:
#    print("Voce errou, o resultado era {}".format(resultado))

# if aninhado
# i = int(input("Digite um valor: "))
# if(i == 10):
#    if(i < 16):
#        print("i é menor que 16")
#    if(i < 12):
#        print("i é menor que 13 tambem")
#else:
#    print("i é maior que 10")

# x = float(input("Entre com o primeiro numero: "))
# y = float(input("Entre com o segundo numero: "))

# print("{1} - Somar")
# print("{2} - Subtrair ")
# print("{3} - Dividir")
# print("{4} - Multiplicar")

# escolha = int(input("Digite o numero da operação desejada: "))
# print("o resultado é: ",end=" " )
# if(escolha == 1):
#    resultado = x + y
#    print(resultado)
#elif(escolha == 2):
#  print(resultado)
#elif(escolha == 3):
#    resultado = x / y
#    print(resultado)
#elif(escolha == 4):
#    resultado = x * y
#    print(resultado)
#else:
#    print("Opçao invalida")
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))
z = int(input("Digite o valor de Z: "))

if (x > y) and (x > z):
    print("O valor {} é maior " .format(x))
elif (y > x) and (y > z):
    print("O valor {} é maior " .format(y))
else:
    print("O valor {} é maior " .format(z))


