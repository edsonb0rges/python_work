motos = ["honda", "yamaha", "suzuki"]
print(motos)

del motos[0]
print(motos)
# remove o primeiro item da lista (Honda). Sabendo a posição de um elemento de uma lista, é possível excluir esse elementos com o comando del variavel[X]


ultima_moto_comprada = motos.pop()
print(motos)
print("A última moto que eu comprei foi uma " + ultima_moto_comprada.title() + " GSX 750R.")
# o método pop() permite que se remova o últimmo item de uma lista (Suzuki), mas permite que você trabalhe com esse item depois da remoção, podendo até adicionar a outra lista.


carros = ["ford", "chevrolet", "ferrari", "fiat", "hyundai", "kia", "renault", "mercedes"]
ultimo_carro_comprado = carros.pop(2)
print(carros)
print("O último carro que eu comprei foi um " + ultimo_carro_comprado.title() + " F50.")
# Ao adicionar um valor ao pop(X), é possível escolher qual item você irá remover.


carros.remove("fiat")
print(carros)
# Quando você não souber a ordem de um elemento de uma lista, você pode utilizar o método remove("elemento") para removê-lo


carro_muito_caro = "mercedes"
carros.remove(carro_muito_caro)
print(carros)
print("\nA " + carro_muito_caro.title() + " é muito cara pra mim.")
# Aqui nós usamos uma variável para identificar um carro caro e que não queremos ele na nossa lista
