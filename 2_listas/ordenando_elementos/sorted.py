carros = ["bmw", "audi", "toyota", "subaru", "honda"]
print(sorted(carros))
# A função sorted() permite exibir sua list em uma ordem em particular, mas não afeta a ordem original propriamente dita da lista.
# Ela apenas retorna (imprime) uma ordem da lista.


ordem_inversa = sorted(carros, reverse=True)
print(ordem_inversa)
# Retorna (imprime) uma ordem inversa da lista, sem alterar a ordem original.
