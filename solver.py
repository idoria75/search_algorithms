from definicoes import *


def solver(listaDePrioridades, beta):
    global vizinhosDisponiveis
    global energizados
    global custoAtual
    # print(vizinhosDisponiveis)
    for i in listaDePrioridades:
        # print([i.getNome()])
        if((i.getNome() in vizinhosDisponiveis) and (i.getCusto()+custoAtual < beta)):
            energizados, vizinhosDisponiveis = energizar(
                i, custoAtual, energizados, vizinhosDisponiveis)
            custoAtual = custoAtual + i.getCusto()
            # break

    # print("Energizados:")
    # print(energizados)
    # print("Vizinhos disponiveis:")
    # print(vizinhosDisponiveis)
    # print("Custo atual:")
    # print(custoAtual)


solver(prioridades, 70)
