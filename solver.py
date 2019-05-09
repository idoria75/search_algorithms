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
        prettyPrintNodos(nodosLigados)
        prettyPrintNodos(nodosDisponiveis)
        print(betaAcumulado)
    else:
        return False

    # print("Nova lista de prioridades:")
    prioridadesAtualizada = subtractLista(prioridadesAtualizada, nodosLigados)
    # prettyPrintNodos(prioridadesAtualizada)
    print("----------------------------------------")

    # Flag que controla se programa continua executando
    while(flagStop == 0):
        betaIteracao = betaAcumulado
        for nodo in prioridadesAtualizada:
            print("Meta: "+str(nodo.getNome()))
            if(betaMaximo - betaAcumulado > nodo.getCusto()):
                print(betaMaximo - betaAcumulado)
                print("Nodos disponiveis *")
                prettyPrintNodos(nodosDisponiveis)
                depthSearch(nodo, [], betaMaximo -
                            betaAcumulado, nodosDisponiveis)
                print(listaDeCustos)
                if(listaDeRespostas == [[]]):
                    # No caso do nodo ja ser vizinho
                    print("Nodo ja eh vizinho")
                    nodosLigados, nodosDisponiveis, betaAcumulado = energizar(
                        nodo, betaAcumulado, nodosLigados, listaDeVizinhos)
                    print("Nova lista de prioridades:")
                    prioridadesAtualizada = subtractLista(
                        prioridadesAtualizada, nodosLigados)
                    print("Nodos disponiveis: ***")
                    prettyPrintNodos(nodosDisponiveis)
                    print("Nodos ligados: ***")
                    prettyPrintNodos(nodosLigados)
                    prettyPrintNodos(prioridadesAtualizada)
                else:
                    # Caso nao seja vizinho
                    # Verificar se Custo da solucao + custo do nodo esta disponivel
                    print("Nao eh vizinho!")
                    if(min(listaDeCustos) + nodo.getCusto() < betaMaximo - betaAcumulado):
                        print("Eh possivel ligar nodo "+str(nodo.getNome()))
                        for aux in range(len(listaDeRespostas)):
                            prettyPrintNodos(listaDeRespostas[aux])
                        print(listaDeCustos)
                del listaDeRespostas[:]
                del listaDeCustos[:]
        if(betaAcumulado == betaIteracao):
            flagStop = 1
        return

    # for nodo in nodosDisponiveis:
    #     print(nodo.getNome())
    #     # print(betaMaximo)
    #     # print(betaAcumulado)
    #     # print(betaMaximo - betaAcumulado)
    #     if(betaMaximo - betaAcumulado > listaDePrioridades[0].getCusto()):
    #         print(nodo.getNome())

    # depthSearch(listaDePrioridades[cont], [],
    #             betaMaximo-betaAcumulado, listaDeVizinhos)

    # print("Caminho Busca: ")
    # prettyPrintNodos(caminhoBusca)
    # print("Respostas: ")
    # for i in listaDeRespostas:
    #     prettyPrintNodos(i)
    # print(listaDeCustos)
    # del listaDeRespostas[:]
    # del listaDeCustos[:]
    # cont = cont+1

    # depthSearch(listaDePrioridades[cont], [],
    #             betaMaximo-betaAcumulado, listaDeVizinhos)
    # print("Caminho Busca: ")
    # prettyPrintNodos(caminhoBusca)
    # print("Respostas: ")
    # for j in listaDeRespostas:
    #     prettyPrintNodos(j)
    # print(listaDeCustos)
    # print(betaAcumulado)
    # del listaDeRespostas[:]
    # del listaDeCustos[:]

    # cont = 7
    # depthSearch(listaDePrioridades[cont], [],
    #             betaMaximo-betaAcumulado, listaDeVizinhos)
    # print("Caminho Busca: ")
    # prettyPrintNodos(caminhoBusca)
    # print("Respostas: ")
    # for k in listaDeRespostas:
    #     prettyPrintNodos(k)
    # print(listaDeCustos)
    # print(betaAcumulado)
    # del listaDeRespostas[:]
    # del listaDeCustos[:]


prioridades = [NodoA, NodoC, NodoG, NodoL,
               NodoO, NodoP, NodoF, NodoB, NodoM, NodoN]
prioridadesSemA = [NodoA, NodoC, NodoG, NodoL,
                   NodoO, NodoP, NodoF, NodoB, NodoM, NodoN]
beta = 80
vizinhos = [NodoA]

print(solve_priority_problem(prioridades, beta, vizinhos))

print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-..-.-.-.-..")

# depthSearch(NodoC, [], 70, vizinhos)
# print("Caminho Busca: ")
# prettyPrintNodos(caminhoBusca)
# print("Respostas: ")
# for i in listaDeRespostas:
#     prettyPrintNodos(i)
# print(listaDeCustos)
