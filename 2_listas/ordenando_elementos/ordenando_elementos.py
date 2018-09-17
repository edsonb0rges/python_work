carros = ["bmw", "audi", "toyota", "subaru"]
carros.sort()
print(carros)
# o método sort() altera a ordem dos elementos de uma lista em ordem alfabética


carros.sort(reverse=True)
print(carros)
# o método sort(reverse=True) altera a ordem dos elementos de uma lista em ordem alfabética inversa. Cuidado!!! O True deve ser escrito com inicial maiúscula


print(sorted(carros))
# A função sorted() permite exibir sua list em uma ordem em particular, mas não afeta a ordem propriamente dita da lista. Ela apenas retorna uma ordem da lista.


carros.reverse()
print(carros)
# O método reverse() inverte a ordem original de uma lista. Lembre-se que como a variável foi alterada pelo método sort(reverse=True), então o reverse() apenas voltou variável para o status anterior


carros = ["bmw", "audi", "toyota", "subaru"]
len(carros)
print(len(carros))
# A função len() informa a quantidade de elementos dentro de uma lista
