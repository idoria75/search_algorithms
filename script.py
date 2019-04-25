class Node:
    def __init__(self, nome="", custo=0, vizinhos=[]):
        self.nome = nome
        self.custo = custo
        self.vizinhos = vizinhos

    def print(self):
        print(self.custo)


NodoA = Node("A", 5)
NodoC = Node("C", 5)
NodoG = Node("G", 5)
NodoL = Node("L", 5)
NodoO = Node("O", 5)
NodoP = Node("P", 5)
NodoF = Node("F", 5)
NodoB = Node("B", 5)
NodoM = Node("M", 5)
NodoN = Node("N", 5)

prioridades = ["A", "C", "G", "L", "O", "P", "F", "B", "M", "N"]

print(NodoA.vizinhos)
NodoA.vizinhos.append(NodoC)
NodoA.vizinhos.append(NodoB)
print(NodoA.vizinhos[0].nome)
