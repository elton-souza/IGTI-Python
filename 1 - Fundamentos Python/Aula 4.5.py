# Metodo SET

# conjunto1 = set('Elton')
# print(conjunto1)

# conjunto1 = set(['Elton', 'Pedro', 'Elton'])
# print(conjunto1)

# conjunto1 = set([1,2,3,4,'Elton',9,6,7,"Elton"])
# print(conjunto1)

# conjunto1 = set(['ELTON' , 'Sandro', 1])
# for i in conjunto1:
#    print(i, end = " ")
# print("Elton" in conjunto1)

# conjunto1 = set([1,2,3,4,5])
# print(conjunto1)
# conjunto1.add(6)
# conjunto1.update([6,7,8,9,10])
# conjunto1.remove(1)
# conjunto1.discard(4)
# conjunto1.pop()
# conjunto1.clear()
# print(conjunto1)

# Operações:
conjuntoA = set([1,2,3])
conjuntoB = set([4,5,1])
# União:
uniao = conjuntoA.union(conjuntoB)
print('Conjunto AB: ', uniao)
# Diferença
dif = conjuntoA.difference(conjuntoB)
print("Diferença AB: ",dif)
# interseção
inter = conjuntoA.intersection(conjuntoB)
print("Interseçao AB: ",inter)
# Diferença Simetrica
difsim = conjuntoA.symmetric_difference(conjuntoB)
print("A diferença simetrica AB: ",difsim)