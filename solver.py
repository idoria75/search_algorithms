from definicoes import *

custoAtual = 0
custoMaximo = 70
vizinhosDisponiveis = ['A']
energizados = []


def solver(listaDePrioridades, beta):  # , vizinhosDisponiveis):
    global vizinhosDisponiveis
    global energizados
    global custoAtual
    for i in listaDePrioridades:
        if((i.getNome() in vizinhosDisponiveis) and (i.getCusto()+custoAtual < beta)):
            energizados, vizinhosDisponiveis = energizar(
                i, custoAtual, energizados, vizinhosDisponiveis)
            custoAtual = custoAtual + i.getCusto()
    print("Resultado: " + str(energizados))
    print("Custo Total:" + str(custoAtual))
