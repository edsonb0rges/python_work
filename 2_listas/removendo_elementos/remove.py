carros = ["ford", "chevrolet", "ferrari", "fiat", "hyundai", "kia", "renault", "mercedes"]
print(carros)

carros.remove("fiat")
print(carros)
# Quando você não souber a ordem de um elemento de uma lista, você pode utilizar o método remove("elemento") para removê-lo


carro_muito_caro = "mercedes"
carros.remove(carro_muito_caro)
print(carros)
print("\nA " + carro_muito_caro.title() + " é muito cara pra mim.")
# Aqui nós usamos uma variável para identificar um carro caro e que não queremos ele na nossa lista
