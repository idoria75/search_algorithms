class Node:
    def __init__(self, nome="", custo=0):
        self._nome = nome
        self._custo = custo
        self._vizinhos = []

    def print(self):
        print(self._custo)
        print(self._vizinhos[0]._nome)
        # print(self._vizinhos[1]._nome)
        # print(self._vizinhos[2]._nome)
        # print(self.vizinhos[0]._custo)

    def appendVizinho(self, novoVizinho):
        self._vizinhos.append(novoVizinho)


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

prioridades = ["A", "C", "G", "L", "O", "P", "F", "B", "M", "N"]

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
