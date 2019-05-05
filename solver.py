from definicoes import *

custoAtual = 0
custoMaximo = 70
vizinhosDisponiveis = ['A']
energizados = []

resultadoBusca = []
custoBusca = 0

# def search(estadosLigados, estadoAtual, estadoMeta, custoAtual):
#     for i in estadoAtual.getVizinhos():
#         if(i.getVizinhos() == []):
#             break
#         elif(estadoMeta in i.getVizinhos()):
#             novoCusto = custoAtual + i.getCusto()
#             energizar(i, custoAtual,)

# def depth_search(lista, resultado, custo, meta):


def solver(listaDePrioridades, beta):  # , vizinhosDisponiveis):
    global vizinhosDisponiveis
    global energizados
    global custoAtual
    for i in listaDePrioridades:
        if((i.getNome() in vizinhosDisponiveis) and (i.getCusto()+custoAtual < beta)):
            energizados, vizinhosDisponiveis = energizar(
                i, custoAtual, energizados, vizinhosDisponiveis)
            custoAtual = custoAtual + i.getCusto()
        elif (not(i.getNome in vizinhosDisponiveis) and (i.getCusto()+custoAtual < beta)):
            # (*) Tentar ligar um nodo vizinho
            # Deste vizinho, tentar ligar outro
                # Se nao tiver outro vizinho, para e volta para (*)
                # Se tiver outro vizinho, repete (*)
            for j in vizinhosDisponiveis:
                print(search(energizados, j, i, custoAtual))

        else:
            break

    print("Resultado: " + str(energizados))
    print("Custo Total:" + str(custoAtual))
