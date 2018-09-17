motos = ["honda", "yamaha", "suzuki"]
print(motos)

ultima_moto_comprada = motos.pop()
print(motos)
print("A última moto que eu comprei foi uma " + ultima_moto_comprada.title() + " GSX 750R.")
# o método pop() permite que se remova o últimmo item de uma lista (Suzuki), mas permite que você trabalhe com esse item depois da remoção, podendo até adicionar a outra lista.



carros = ["ford", "chevrolet", "ferrari", "fiat", "hyundai", "kia", "renault", "mercedes"]
ultimo_carro_comprado = carros.pop(2)
print(carros)
print("\nO último carro que eu comprei foi um " + ultimo_carro_comprado.title() + " F50.")
# Ao adicionar um valor ao pop(X), é possível escolher qual item você irá remover.
