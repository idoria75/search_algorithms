class Node:
    # Variaveis com "_" sao privadas
    def __init__(self, nome="", custo=0):
        self._nome = nome
        self._custo = custo
        self._vizinhos = []
        self._flagBusca = False

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

    def setFlagBusca(self, newState):
        self._flagBusca = newState

    def getFlagBusca(self):
        return self._flagBusca


class Resposta:
    def __init__(self, listaCaminhos=[], listaCustos=[]):
        self._listaCaminhos = listaCaminhos
        self._listaCustos = listaCustos

    def appendResposta(self, caminho, custo):
        self._listaCaminhos = self._listaCaminhos+caminho
        self._listaCustos = self._listaCustos+[custo]


def prettyPrintNodos(lista):
    temp = []
    for i in lista:
        temp = temp+[i.getNome()]
    print(temp)


def getNameListaNodos(lista):
    temp = []
    for i in lista:
        temp = temp+[i.getNome()]
    return temp


def normalizaLista(lista):
    return(list(dict.fromkeys(lista)))

# subtractLista: Retorna todos os itens que estao em X e nao em Y


def subtractLista(x, y):
    result = [item for item in x if item not in y]
    return result


def resetFlags(listaNodos):
    for i in listaNodos:
        i.setFlagBusca(False)

# Funcao para energizar um do sistema
# Parametros:
#   Nodo: Nodo do sistema a ser energizado
#   custoAtual: Custo energético atual do sistema
#   estadoAtual: Lista de strings com os estados atualmente ligados
#   listaDeVizinhosDisponiveis: Lista de strings com o nome dos vizinhos disponiveis


def energizar(nodo, custoAtual, estadoAtual, listaDeVizinhosDisponiveis):

    print("Energizar -> Estado atual: ")
    prettyPrintNodos(estadoAtual)
    prettyPrintNodos(listaDeVizinhosDisponiveis)
    if(not(nodo in estadoAtual)):
        estadoAtual = estadoAtual + [nodo]
        custoAtual = nodo.getCusto() + custoAtual
        listaDeNovosVizinhos = nodo.getVizinhos()
        for i in listaDeNovosVizinhos:
            if(not(i in listaDeVizinhosDisponiveis) and not(i in estadoAtual)):
                listaDeVizinhosDisponiveis = listaDeVizinhosDisponiveis + [i]
        for i in listaDeVizinhosDisponiveis:
            if(i == nodo.getNome()):
                listaDeVizinhosDisponiveis.remove(nodo)
    # prettyPrintNodos(estadoAtual)
    # prettyPrintNodos(listaDeVizinhosDisponiveis)
    # print(custoAtual)
    # print(listaDeVizinhosDisponiveis)
    # print(nodo)
    listaDeNovosVizinhos = subtractLista(
        listaDeVizinhosDisponiveis, [nodo])
    return estadoAtual, listaDeNovosVizinhos, custoAtual


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
NodoB.appendVizinho(NodoG)

NodoC.appendVizinho(NodoO)
NodoC.appendVizinho(NodoF)

NodoO.appendVizinho(NodoG)

NodoG.appendVizinho(NodoN)
NodoG.appendVizinho(NodoL)

NodoF.appendVizinho(NodoM)
