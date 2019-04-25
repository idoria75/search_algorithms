class Node:
    def __init__(self, nome="", custo=0, vizinhos=[]):
        self.nome = nome
        self.custo = custo
        self.vizinhos = vizinhos

    def print(self):
        print(self.custo)


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

print(NodoA.vizinhos)
NodoA.vizinhos.append(NodoC)
NodoA.vizinhos.append(NodoB)
print(NodoA.vizinhos[0].nome)
print(NodoA.vizinhos[0].custo)
