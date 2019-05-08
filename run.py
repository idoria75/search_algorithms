from solver import *
import time

beta = 95
print("Prioridade: "+str(prettyPrintNodos(prioridades))+", Custo: "+str(beta))

start = time.time()
solver(prioridades, beta)
end = time.time()
print("Tempo de execucao: "+str(end-start)+"s")
