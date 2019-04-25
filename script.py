class Node:
    def __init__(self, nome="", custo=0, vizinhos=[]):
        self.nome = nome
        self.custo = custo
        self.vizinhos = vizinhos

    def print(self):
        print(self.custo)
        print(self.vizinhos[0].nome)
        print(self.vizinhos[1].nome)
        print(self.vizinhos[2].nome)
        # print(self.vizinhos[0].custo)


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

NodoA.vizinhos.append(NodoB)
NodoA.vizinhos.append(NodoC)

# NodoB.vizinhos.append(NodoA)
NodoB.vizinhos.append(NodoP)
# NodoB.vizinhos.append(NodoG)

# NodoP.vizinhos.append(NodoB)

# NodoC.vizinhos.append(NodoA)
# NodoC.vizinhos.append(NodoO)
# NodoC.vizinhos.append(NodoF)

# NodoO.vizinhos.append(NodoC)
# NodoO.vizinhos.append(NodoG)

# NodoG.vizinhos.append(NodoB)
# NodoG.vizinhos.append(NodoN)
# NodoG.vizinhos.append(NodoL)
# NodoG.vizinhos.append(NodoO)

# NodoF.vizinhos.append(NodoC)
# NodoF.vizinhos.append(NodoM)

# Falta:
# NodoN, NodoL, NodoM

NodoA.print()
