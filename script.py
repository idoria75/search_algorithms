class Node:
    def __init__(self, custo=0, vizinhos=None):
        self.custo = custo
        self.filhos = vizinhos

    def print(self):
        print(self.custo)


Nodo1 = Node(3)
Nodo1.print()
Nodo2 = Node(5)
Nodo2.print()
