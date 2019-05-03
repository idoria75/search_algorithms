class Node:
    # Variaveis com "_" sao privadas
    def __init__(self, nome="", custo=0):
        self._nome = nome
        self._custo = custo
        self._vizinhos = []

    def print(self):
        print(self._custo)
        print(self._vizinhos[0]._nome)

    def appendVizinho(self, novoVizinho):
        self._vizinhos.append(novoVizinho)

    def getCusto(self):
        return self._custo

    def getNome(self):
        return self._nome

    def getVizinhos(self):
        return self._vizinhos

# Qual a funcao disso?
# Reprojetar!


def getNomeVizinhos(listaDeNodos):
    nomes = []
    print(listaDeNodos)
    for i in listaDeNodos:
        print("GET_NOME()")
        print(i.getNome())
        nomes = nomes + [i.getNome()]
    return nomes

# Energiza o nodo se não energizado antes


def energizar(nodo, custoAtual, estadoAtual, listaDeVizinhosDisponiveis):
    print("Nome do novo nodo:")
    print(nodo.getNome())
    print("Novo nodo em estados:")
    print(nodo.getNome() in estadoAtual)
    # print("PRINT NODOS:")
    # print(getNomeVizinhos(estadoAtual))
    if(not(nodo.getNome() in estadoAtual)):
        estadoAtual = estadoAtual + [(nodo.getNome())]
        custoAtual = nodo.getCusto() + custoAtual
        # print("Lista Vizinhos anterior:")
        # print(listaDeVizinhosDisponiveis)
        listaDeVizinhosDisponiveis = listaDeVizinhosDisponiveis + \
            getNomeVizinhos(nodo)

        # print("Lista Vizinhos atual:")
        # print(listaDeVizinhosDisponiveis)

        print("Custo atual:")
        print(custoAtual)
        print("Estados:")
        print(estadoAtual)

    return estadoAtual


NodoA = Node("A", 5)
NodoC = Node("C", 10)
NodoG = Node("G", 20)
NodoL = Node("L", 13)
NodoO = Node("O", 40)
NodoP = Node("P", 10)
NodoF = Node("F", 50)
NodoB = Node("B", 5)
NodoM = Node("M", 13)
NodoN = Node("N", 13)

NodoA.appendVizinho(NodoB)
NodoA.appendVizinho(NodoC)

NodoB.appendVizinho(NodoP)
NodoB.appendVizinho(NodoA)
NodoB.appendVizinho(NodoG)

NodoP.appendVizinho(NodoB)

NodoC.appendVizinho(NodoA)
NodoC.appendVizinho(NodoO)
NodoC.appendVizinho(NodoF)

NodoO.appendVizinho(NodoC)
NodoO.appendVizinho(NodoG)

NodoG.appendVizinho(NodoB)
NodoG.appendVizinho(NodoN)
NodoG.appendVizinho(NodoL)
NodoG.appendVizinho(NodoO)

NodoF.appendVizinho(NodoC)
NodoF.appendVizinho(NodoM)

NodoN.appendVizinho(NodoG)

NodoL.appendVizinho(NodoG)

NodoM.appendVizinho(NodoF)

prioridades = [NodoA, NodoC, NodoG, NodoL,
               NodoO, NodoP, NodoF, NodoB, NodoM, NodoN]
custoAtual = 0
custoMaximo = 70
vizinhosDisponiveis = []
energizados = []
