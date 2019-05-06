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

    def getNomeVizinhos(self):
        nomes = []
        for i in self._vizinhos:
            nomes = nomes+[i.getNome()]
        return nomes

# Funcao para energizar um do sistema
# Parametros:
#   Nodo: Nodo do sistema a ser energizado
#   custoAtual: Custo energético atual do sistema
#   estadoAtual: Lista de strings com os estados atualmente ligados
#   listaDeVizinhosDisponiveis: Lista de strings com o nome dos vizinhos disponiveis


def energizar(nodo, custoAtual, estadoAtual, listaDeVizinhosDisponiveis):
    if(not(nodo.getNome() in estadoAtual)):
        estadoAtual = estadoAtual + [(nodo.getNome())]
        custoAtual = nodo.getCusto() + custoAtual
        listaDeNovosVizinhos = nodo.getNomeVizinhos()
        for i in listaDeNovosVizinhos:
            if(not(i in listaDeVizinhosDisponiveis) and not(i in estadoAtual)):
                listaDeVizinhosDisponiveis = listaDeVizinhosDisponiveis + [i]
        for i in listaDeVizinhosDisponiveis:
            if(i == nodo.getNome()):
                listaDeVizinhosDisponiveis.remove(nodo.getNome())
    return estadoAtual, listaDeVizinhosDisponiveis


# Configura Nodos
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

# Adiciona vizinhos
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
