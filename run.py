from solver import *

estadoBusca = []
vizinhosLigados = [NodoA]
custoBusca = 0
#energizar(nodo, custoAtual, estadoAtual, listaDeVizinhosDisponiveis)
estadoBusca, vizinhosLigados, custoBusca = energizar(
    NodoC, custoBusca, estadoBusca, vizinhosLigados)
