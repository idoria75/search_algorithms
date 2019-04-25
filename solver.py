from definicoes import *

prioridades = [NodoA, NodoC, NodoG, NodoL,
               NodoO, NodoP, NodoF, NodoB, NodoM, NodoN]
custoMaximo = 70


def solver(listaDePrioridades, beta):
    custoAtual = 0
    for i in listaDePrioridades:
        print(i.getNome())
