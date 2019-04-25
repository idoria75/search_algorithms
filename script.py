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


prioridades = ['A', "C", "G", "L", "O", "P", "F", "B", "M", "N"]
custoAtual = 0
# Adiciona nome do nodo quando a linha for energizada
estados = []

# Energiza o nodo se não energizado antes


def energizar(nodo):
    global custoAtual, estados
    print("Nome do novo nodo:")
    print(nodo.getNome())
    print("Novo nodo em estados:")
    print(nodo.getNome() in estados)
    if(not(nodo.getNome() in estados)):
        estados = estados + [(nodo.getNome())]
        custoAtual = nodo._custo + custoAtual
    print("Custo atual:")
    print(custoAtual)
    print("Estados:")
    print(estados)


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

energizar(NodoA)
energizar(NodoB)
energizar(NodoC)
energizar(NodoG)
energizar(NodoL)
energizar(NodoP)

# print("NodoA:")
# NodoA.print()
# print("NodoB:")
# NodoB.print()
# print("NodoC:")
# NodoC.print()
# print("NodoP:")
# NodoP.print()
# print("NodoG:")
# NodoG.print()
# print("NodoO:")
# NodoO.print()
# print("NodoN:")
# NodoN.print()
# print("NodoM:")
# NodoM.print()
# print("NodoL:")
# NodoL.print()
# print("NodoF:")
# NodoF.print()
