from solver import *

prioridades = [NodoA, NodoC, NodoG, NodoL,
               NodoO, NodoP, NodoF, NodoB, NodoM, NodoN]

beta = 20

vizinhos = [NodoA]

# if(listaDePrioridades[i].getCusto() + betaAcumulado < betaMaximo):
#     nodosLigados, nodosDisponiveis, betaAcumulado = energizar(
#         listaDePrioridades[i], betaAcumulado, [], vizinhos)
#     prettyPrintNodos(nodosLigados)
#     prettyPrintNodos(nodosDisponiveis)
#     print(betaAcumulado)


# solve_priority_problem(prioridades, beta, vizinhos)


# for i in prioridades:
#     if(i == NodoA and betaMaximo > NodoA.getCusto()):
#         a, custoAtual, c = energizar(NodoA, custoAtual, [], vizinhos)
#         print(c)
#     else:
#         print("Meta: Nodo "+str(i.getNome()))
#         listaDeRespostas, listaDeCustos = depthSearch(
#             i, [], betaMaximo, vizinhos)
#         print("Lista de respostas")
#         for j in listaDeRespostas:
#             prettyPrintNodos(j)
#         print("Lista de custos: ")
#         print(listaDeCustos)
#         if(len(listaDeCustos) > 0):
#             if(listaDeCustos[0] < betaMaximo):
#                 a, custoAtual, c = energizar(i, custoAtual, [], vizinhos)
#                 vizinhos = a
#                 print("B: ")
#                 print(custoAtual)
#                 custoAtual = custoAtual + custoAtual
#     del listaDeRespostas[:]
#     del listaDeCustos[:]
#     print("Beta atual: "+str(custoAtual))

# print(custoAtual)

depthSearch(NodoG, [], 70, vizinhos)
print("Caminho Busca: ")
prettyPrintNodos(caminhoBusca)
print("Respostas: ")
for i in listaDeRespostas:
    prettyPrintNodos(i)
print(listaDeCustos)
