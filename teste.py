import time

startb = time.time()
listaOriginal = ["A", "B", "C", "T", "D", "E", 2, "T"]
resultadoOriginal = []
custoOriginal = 0
resultadoFinal = []
custoFinal = 0

# Para quando acha meta igual a um elemento da lista


def recursao(lista, resultado, custo, meta):
    #global resultadoFinal, custoFinal
    if(lista != []):
        if(lista[0] != meta):
            custo = custo+1
            resultado = resultado + [lista.pop(0)]
            print("Lista Atual: " + str(lista))
            print("Resultado Atual: " + str(resultado))
            resultado, custo = recursao(lista, resultado, custo, meta)
        else:
            custo = custo+1
            resultado = resultado+[meta]
    else:
        print("Lista Final: " + str(lista))
        print("Resultado Final: " + str(resultado))
        if(meta in resultado):
            print("Meta Atingida")
            print(resultado)
            print(custo)
        else:
            print("Meta nao encontrada")
            return [], 0
    return resultado, custo


start = time.time()

resposta, custoResposta = recursao(
    listaOriginal, resultadoOriginal, custoOriginal, 3)
print(resposta)
print(custoResposta)

end = time.time()
print("Tempo de execucao: " + str(end-start) + " segundos")
print("      Tempo total: " + str(end-startb) + " segundos")
