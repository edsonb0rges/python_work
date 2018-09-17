motos = ["honda", "yamaha", "suzuki"]
print(motos)

motos[0] = "bmw"
print(motos)
# motos[0] = "bmw" mudou o nome do elemento "honda" para "bmw"

motos.append("ducati")
print(motos)
# acrescenta novo elemento ao final de uma lista

motos.insert(0, "mv agusta")
print(motos)
# acrescenta novo elemento à lista de acordo com a definição feita pelo programador em 0, 1, 2...
