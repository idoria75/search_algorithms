from definicoes import *

custoAtual = 0
custoMaximo = 70
vizinhosDisponiveis = ['A']
energizados = []
flag = False


def solver(listaDePrioridades, beta):  # , vizinhosDisponiveis):
    global vizinhosDisponiveis, energizados, custoAtual, flag
    temp_flag = 0
    while(flag != True):
        temp_flag = 0
        for i in listaDePrioridades:
            if((i.getNome() in vizinhosDisponiveis) and (i.getCusto()+custoAtual < beta) and temp_flag == 0):
                energizados, vizinhosDisponiveis = energizar(
                    i, custoAtual, energizados, vizinhosDisponiveis)
                custoAtual = custoAtual + i.getCusto()
                temp_flag = 1
            if(i.getNome() == 'N' and temp_flag == 0):
                flag = True
    print("Resultado: " + str(energizados))
    print("Custo Total:" + str(custoAtual))
