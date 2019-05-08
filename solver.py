from definicoes import *

custoAtual = 0
custoMaximo = 70
vizinhosDisponiveis = [NodoA]
energizados = []

resultadoBusca = []
custoBusca = 0

# Lista: Lista dos vizinhos disponiveis
# Resultado: Variavel que ira guardar o caminho ate o nodo
# Custo: Variavel que ira guardar custo ate o nodo
# Meta: Nodo meta
# Lista deve ser lista de strings e nao de nodos para funcionar


def depth_search(lista, resultado, custo, meta):
    print("Lista:" + str(lista))
    print(lista[0].getNome())
    print("Resultado:" + str(resultado))
    print("Custo:" + str(custo))
    print("Meta:" + str(meta))
    for i in lista:
        print(i.getNome())
        # if i.getNome() == meta.getNome():
        if(meta in lista):
            return True
        else:
            print("Nodo: "+i.getNome())
            print("Vizinhos: "+str(i.getNomeVizinhos()))
            print(energizar(i, custo, lista, i.getVizinhos())[1])
    return False


# print(depth_search(vizinhosDisponiveis, resultadoBusca, custoBusca, NodoB))
