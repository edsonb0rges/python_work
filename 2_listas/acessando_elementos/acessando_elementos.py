bicicletas = ["trek", "cannondale", "caloi", "monark", "specialize", "sundown"]
print(bicicletas[2])
# Para acessar um elemento de uma lista, basta informar ao interpretador qual é elemento da ordem que se pretende acessar entre colchetes [0, 1, 2.....].


print(bicicletas[3].title())
# Observe que também foi utilizada o método .title para deixar a inicial maiúscula


print(bicicletas[-1])
# O [-1] devolve o último item da lista


print(bicicletas[-4])
# O [-4] devolve o 4º item a partir do final, e assim sucessivamente [-5], [-6]....


message ="Minha primeira bicicleta foi uma " + bicicletas[5].title() + "."
print(message)
# Podemos usar concatenação para criar uma mensagem com base em um valor de uma lista
