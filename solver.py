from definicoes import *

caminhoBusca = []
listaDeRespostas = []
listaDeCustos = []


def depthSearch(meta, caminho, betaDisponivel, vizinhosDisponiveis):
    # print("Vizinhos disponiveis: ")
    # prettyPrintNodos(vizinhosDisponiveis)
    global caminhoBusca, listaDeRespostas, listaDeCustos
    for i in vizinhosDisponiveis:
        if(i == meta):
            # print("Meta "+i.getNome()+" atingida!")
            # print("Caminho: ")
            # prettyPrintNodos(caminho)
            listaDeRespostas = listaDeRespostas + [caminho]
            custo = 0
            for i in caminho:
                custo = custo+i.getCusto()
            listaDeCustos = listaDeCustos + [custo]
            caminhoBusca = caminho
        else:
            if(i.getVizinhos() != []):
                novoEstadoVizinhos = i.getVizinhos()
                novoBeta = betaDisponivel - i.getCusto()
                novoCaminho = caminho+[i]
                depthSearch(meta, novoCaminho, novoBeta, novoEstadoVizinhos)
    return listaDeRespostas, listaDeCustos


def solve_priority_problem(listaDePrioridades, betaMaximo, listaDeVizinhos):
    betaAcumulado = 0
    cont = 0
    prioridadesAtualizada = listaDePrioridades
    flagStop = 0
    nodosLigados = []
    nodosDisponiveis = []

    # Liga NodoA se possivel:
    if(betaMaximo - betaAcumulado > listaDePrioridades[0].getCusto()):
        nodosLigados, nodosDisponiveis, betaAcumulado = energizar(
            NodoA, betaAcumulado, [], listaDeVizinhos)

    else:
        return False
    prettyPrintNodos(nodosLigados)
    prettyPrintNodos(nodosDisponiveis)
    print(betaAcumulado)
    print("Nova lista de prioridades:")
    prioridadesAtualizada = subtractLista(prioridadesAtualizada, nodosLigados)
    prettyPrintNodos(prioridadesAtualizada)
    print("----------------------------------------")

    # Flag que controla se programa continua executando
    while(flagStop == 0):
        # Verificar necessidade
        betaIteracao = betaAcumulado
        for nodo in prioridadesAtualizada:
            print("Meta: "+str(nodo.getNome()))
            if(betaMaximo - betaAcumulado > nodo.getCusto()):
                print(betaMaximo - betaAcumulado)
                # print("Nodos disponiveis *")
                # prettyPrintNodos(nodosDisponiveis)

                depthSearch(nodo, [], betaMaximo -
                            betaAcumulado, nodosDisponiveis)
                print(listaDeCustos)
                if(listaDeRespostas == [[]]):
                    # No caso do nodo ja ser vizinho
                    print("Nodo ja eh vizinho")
                    nodosLigados, nodosDisponiveis, betaAcumulado = energizar(
                        nodo, betaAcumulado, nodosLigados, nodosDisponiveis)
                    # print("Nova lista de prioridades:")
                    print("Nodos disponiveis: ***")
                    prettyPrintNodos(nodosDisponiveis)
                    print("Nodos ligados: ***")
                    prettyPrintNodos(nodosLigados)
                    prioridadesAtualizada = subtractLista(
                        prioridadesAtualizada, nodosLigados)
                    print("Nova lista de prioridades: ")
                    prettyPrintNodos(prioridadesAtualizada)

                else:
                    # Caso nao seja vizinho
                    # Verificar se Custo da solucao + custo do nodo esta disponivel
                    print("Nao eh vizinho!")
                    if(len(listaDeCustos) > 0):
                        if(min(listaDeCustos) + nodo.getCusto() < betaMaximo - betaAcumulado):
                            print("Eh possivel ligar nodo "+str(nodo.getNome()))
                            melhorResposta = listaDeRespostas[listaDeCustos.index(
                                min(listaDeCustos))]
                            for auxNodo in melhorResposta:
                                print(auxNodo.getNome())
                                nodosLigados, nodosDisponiveis, betaAcumulado = energizar(
                                    auxNodo, betaAcumulado, nodosLigados, nodosDisponiveis)
                            nodosLigados, nodosDisponiveis, betaAcumulado = energizar(
                                nodo, betaAcumulado, nodosLigados, nodosDisponiveis)
                del listaDeRespostas[:]
                del listaDeCustos[:]
                print("----------------------------------------")
        if(betaAcumulado == betaIteracao):
            print("PAROU")
            flagStop = 1
        prettyPrintNodos(nodosLigados)
        print(str(betaAcumulado)+"/"+str(betaMaximo))
    return

prioridades = [NodoA, NodoC, NodoG, NodoL,
               NodoO, NodoP, NodoF, NodoB, NodoM, NodoN]
prioridadesSemA = [NodoA, NodoC, NodoG, NodoL,
                   NodoO, NodoP, NodoF, NodoB, NodoM, NodoN]
beta = 90
vizinhos = [NodoA]

print(solve_priority_problem(prioridades, beta, vizinhos))
