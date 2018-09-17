quadrados = []
for valor in range(1,11):
    quadrado = valor**2
    quadrados.append(quadrado)
print(quadrados)
# Começamos com uma lista vazia chamada "quadrados".
# Depois dizemos a Python para percorrer cada valor de 1 a 10 usando a função range().
# No loop, o valor atual é elevado ao quadrado e armazenado na variável "quadrado"
# Após, cada novo valor de "quadrado" é concatenado à lista "quadrados".
# Por fim, quando o loop acaba de executar, a lista de quadrados é exibida

#Podemos simplificar esse código da seguinte forma:
quadrados = []
for valor in range(1,11):
    quadrados.append(valor**2)
print(quadrados)
