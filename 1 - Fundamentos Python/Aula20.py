# Construtores
'''
class carro:
    def __init__(self,portas,preço,):
        self.numero_portas = portas
        self.preço = preço

        print("Objeto instanciado com sucesso")
    def get_numero_portas(self):
        return self.numero_portas

carro1 = carro(6,50000,)
portas_carro1 = carro1.get_numero_portas()
print("Meu carro possui %d portas" %portas_carro1)
print(20*"=")
carro2 = carro(2,70000)
portas_carro2 = carro2.get_numero_portas()
print("Meu carro possuí %d portas" %portas_carro2)
================================================
#Métodos acessores
import array as a
meu_array = a.array('i',[1,2,3,4,5,2])
print(meu_array)
print(meu_array.index(2)) #Acessa o indice com valor igual a 2
print(meu_array.count(2)) #Retorna a quantiade que o numero aparece
'''
#Criando uma classe Carro
class carro:
    def __init__(self,portas,valor):
        self.numero_portas = portas
        self.valor = valor
        print("Objeto criado com sucesso ")
    def get_numero_portas(self):
        return self.numero_portas
    def set_numero_portas(self,novo_numero_portas):
        self.numero_portas = novo_numero_portas

carro1 = carro(2,60000)
print("Numero de portas é ", carro1.get_numero_portas())
carro1.set_numero_portas(5) # Modifica o numero de portas
print("O novo numero de portas é", carro1.get_numero_portas())

