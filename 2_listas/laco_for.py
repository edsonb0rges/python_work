magicos = ["alice", "david", "carolina", "zeruela"]
print(magicos)

for magico in magicos:
    print(magico)
# O laço "for" executa a mesma ação em todos os itens de uma lista. Observe que há uma diferença entre print(magicos) e print(magico)
# O laço "for" equivale a dizer: para todo mágico na lista de mágicos, exiba o nome do mágico
# Como a lista "magicos" foi armazenada como variável "magico", o interpretador irá repetir todo o loop mais de uma vez, até o último elemento da lista. Ao encerrar esse processo, o interpretador passa para o próximo passo do código.
# Tenha em mente que o conjunto de passos será repetido, uma vez para cada item da lista, não importa quantos itens haja na lista


    print(magico.title() + ", esse foi um ótimo truque.")
    # Cuidado! Para que os elementos da lista façam parte do laço "for", o comando "print" deve estar indentado!!!!!!

    print(magico.title() + ", esse foi um ótimo truque.")
    print("Eu não vejo a hora de ver um outro truque, " + magico.title() + ".\n")
    # Perceba que o laço "for" está retornando todo o comando e só depois que ele passa para o próximo item "mágico" da lista.

print("Obrigado, pessoal. Foi um grande show de mágica!")
