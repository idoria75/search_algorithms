from definicoes import *

custoAtual = 0
custoMaximo = 70
vizinhosDisponiveis = [NodoA]
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


def depth_search(lista, resultado, custo, meta):
    global resultadoBusca, custoBusca, energizados
    print(lista)
    print(energizados)
    if(lista == []):
        return [], 0
    else:
        for i in lista:
            if(not(i in energizados)):
                if(i != meta.getNome()):
                    custoAtual = custo+i.getCusto()
                    listaAtual = i.getVizinhos()
                    resultadoAtual = resultado + [i]
                    resultado, custo = depth_search(
                        listaAtual, resultadoAtual, custoAtual, meta)
                    if(meta.getNome() in resultado):
                        resultadoBusca = resultado
                        custoBusca = custo
                        print("Resultado Final: " + str(resultadoBusca))
    return resultado, custo


print(NodoG)
print(NodoG.getNome())
depth_search(vizinhosDisponiveis, resultadoBusca, custoBusca, NodoG)
