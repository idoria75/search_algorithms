from definicoes import *

betaMaximo = 50
metaFinal = NodoF
vizinhos = [NodoA]

caminhoBusca = []

listaDeRespostas = []
listaDeCustos = []

# Retorna caminho para ligar nodo e custo para atingir nodo


def depthSearch(meta, caminho, betaDisponivel, vizinhosDisponiveis):
    # print(vizinhosDisponiveis)
    global caminhoBusca, listaDeRespostas, listaDeCustos
    for i in vizinhosDisponiveis:
        # print("Nome: "+i.getNome())
        # if(betaDisponivel - i.getCusto() >= 0):
        if(i == meta):
            print("Meta atingida")
            prettyPrintNodos(caminho)
            listaDeRespostas = listaDeRespostas + [caminho]
            custo = 0
            for i in caminho:
                custo = custo+i.getCusto()
            listaDeCustos = listaDeCustos + [custo]
            caminhoBusca = caminho
        else:
            if(i.getVizinhos() != []):
                novoEstadoVizinhos = i.getVizinhos()
                #print("Novos vizinhos: ")
                # prettyPrintNodos(novoEstadoVizinhos)
                novoBeta = betaDisponivel - i.getCusto()
                novoCaminho = caminho+[i]
                # print("Caminho: ")
                # prettyPrintNodos(caminho)
                # print("Novo Beta: ", novoBeta)
                depthSearch(meta, novoCaminho, novoBeta, novoEstadoVizinhos)
        # else:
        # return False


# def solver(listaDePrioridades, beta):  # , vizinhosDisponiveis):
#     global vizinhosDisponiveis, energizados, custoAtual, flag
#     temp_flag = 0
#     while(flag != True):
#         temp_flag = 0
#         for i in listaDePrioridades:
#             if((i.getNome() in vizinhosDisponiveis) and (i.getCusto()+custoAtual < beta) and temp_flag == 0):
#                 energizados, vizinhosDisponiveis = energizar(
#                     i, custoAtual, energizados, vizinhosDisponiveis)
#                 custoAtual = custoAtual + i.getCusto()
#                 temp_flag = 1
#             if(i.getNome() == 'N' and temp_flag == 0):
#                 flag = True
#     print("Resultado: " + str(energizados))
#     print("Custo Total:" + str(custoAtual))

print("Resolvendo o problema: Atingir meta "+metaFinal.getNome()+" com Beta = " +
      str(betaMaximo)+" e partindo da lista de vizinhos: "+str(getNameListaNodos(vizinhos)))
depthSearch(metaFinal, [], betaMaximo, vizinhos)
print("Caminho Busca: ")
prettyPrintNodos(caminhoBusca)
print("Lista de respostas: ")
for i in listaDeRespostas:
    prettyPrintNodos(i)
print(listaDeCustos)
