listaOriginal = ["A", "B", "C", "T", "D", "E", "F", "T"]
resultadoOriginal = []
custoOriginal = 0
resultadoFinal = []
custoFinal = 0


def recursao(lista, resultado, custo, meta):
    global resultadoFinal, custoFinal
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


resposta, custoResposta = recursao(
    listaOriginal, resultadoOriginal, custoOriginal, "T")
print(resposta)
print(custoResposta)
