from definicoes import *

custoAtual = 0
custoMaximo = 70
vizinhosDisponiveis = [NodoA]
energizados = []

resultadoBusca = []
custoBusca = 0


def depth_search(lista, resultado, custo, meta):
    print("Lista:" + str(lista))
    print("Resultado:" + str(resultado))
    print("Custo:" + str(custo))
    print("Meta:" + str(meta))
    for i in lista:
        print(i.getNome())
        # if i.getNome() == meta.getNome():
        if(meta in lista):
            return True
        else:
            print(i.getVizinhos())
    return False
    # global resultadoBusca, custoBusca, energizados
    # print(lista)
    # print(energizados)
    # if(lista == []):
    #     return [], 0
    # else:
    #     for i in lista:
    #         if(not(i in energizados)):
    #             if(i != meta.getNome()):
    #                 custoAtual = custo+i.getCusto()
    #                 energizados, lista = energizar(i, custoAtual,)
    #                 resultadoAtual = resultado + [i]
    #                 resultado, custo = depth_search(
    #                     listaAtual, resultadoAtual, custoAtual, meta)
    #                 if(meta.getNome() in resultado):
    #                     resultadoBusca = resultado
    #                     custoBusca = custo
    #                     print("Resultado Final: " + str(resultadoBusca))
    # return resultado, custo


print(NodoG)
print(NodoG.getNome())
print(depth_search(vizinhosDisponiveis, resultadoBusca, custoBusca, NodoA))
