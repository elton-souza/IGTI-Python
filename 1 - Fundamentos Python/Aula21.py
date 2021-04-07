#Classes
#class MinhaClasse:
#    ''' Corpo da classe'''
#    pass
# Help(MinhaClasse)
# ========================================================================================================
#class Carro:
#    ''' Corpo da Classe Carro '''
#    numero_de_portas = 5
#    def print_msg(self):
#        print("Carro criado")
#print(Carro.numero_de_portas)
#print(Carro.__doc__)  #__doc__ é a descriçao da classe
# Instanciando objeto
# carro1 = Carro() #Carro1 é uma instancia da classe Carro, e recebe todos os atributos da classe

# carro1.print_msg() #Necessario instanciar para poder ultilizar os obejtos dentro de uma classe
# =========================================================================================================
class carro:
    def __init__(self,cor = "Vermelho",n_portas=3):
        self.cor_do_carro = cor
        self.num_portas = n_portas
    def get_cor_carro(self):
        return self.cor_do_carro
    def get_number_portas(self):
        return self.num_portas

carro1 = carro(cor = "Azul", n_portas = 5 )
carro2 = carro()
carro3 = carro(cor = "Preto", n_portas = 6)

print("A cor do carro 1 é {} e com {} portas".format(carro1.get_cor_carro(),carro1.get_number_portas()))
print("A cor do carro 2 é {} e com {} portas".format(carro2.get_cor_carro(),carro2.get_number_portas()))
print("A cor do carro 3 é {} e com {} portas".format(carro3.get_cor_carro(),carro3.get_number_portas()))

print(5*"=" + " Novas Cores "+ 5* "=")
carro1.get_cor_carro = "Laranja"
carro2.get_cor_carro = "Preto"
carro3.get_cor_carro = "Rosa"
print(f"A nova cor do carro 1 é {carro1.get_cor_carro}, carro 2 é {carro2.get_cor_carro} e do carro 3 é {carro3.get_cor_carro}")


