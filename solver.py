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

# Funcao atual esta verificando se o nodo meta esta no parametro lista.
# Queremos que ele verifique se esta em um dos vizinhos dos nodos da lista


def solver_depth_search(lista, resultado, custo, meta):
    global resultadoBusca
    global vizinhosDisponiveis
    global custoBusca
    print("Lista:" + str(getNameListaNodos(lista)))
    # print("Resultado:" + str(getNameListaNodos(resultado)))
    # print("Custo:" + str(custo))
    print("Meta:" + meta.getNome())
    for i in lista:
        print("Nome: "+i.getNome())
        if(meta in lista):
            print("Nodo esta na lista")
            resultadoBusca, vizinhosDisponiveis, custoBusca = energizar(
                i, custoBusca, resultadoBusca, lista+i.getVizinhos())
            return True
        else:
            print("Meta nao encontrada")
            if(meta in i.getVizinhos()):
                print("Resposta eh um vizinho")
                # Energiza pai e filho
                resultadoBusca, vizinhosDisponiveis, custoBusca = energizar(
                    i, custoBusca, resultadoBusca, lista+i.getVizinhos())
                resultadoBusca, vizinhosDisponiveis, custoBusca = energizar(
                    meta, custoBusca, resultadoBusca, lista+i.getVizinhos())
                return True
            else:
                print("Meta nao esta nos vizinhos")

                if(normalizaLista(lista) == normalizaLista(lista+i.getVizinhos())):
                    return False
                # Caso lista de vizinhos mude ao dar um passo
                else:
                    print("Passo: "+i.getNome())
                    novaLista = normalizaLista(lista+i.getVizinhos())
                    novaLista.remove(i)
                    return solver_depth_search(novaLista, resultado, custo, meta)
                    # USAR DIFERENCA ENTRE OS VIZINHOS ANTIGOS E NOVOS!!!!!!

    return False


print(solver_depth_search(vizinhosDisponiveis, resultadoBusca, custoBusca, NodoM))
print("Resultado busca: ")
prettyPrintNodos(resultadoBusca)
print(custoBusca)
