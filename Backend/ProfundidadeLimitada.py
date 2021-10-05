from libsBasic import *
class ProfundidadeLimitadaMethod:
    def profundidadeLimitada(self, inicio, fim, limite):
        caminho = []

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio, 0, None)
        l2.insereUltimo(inicio, 0, None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            if atual is None: break

            if atual.valor2 < limite:
                ind = nos.index(atual.valor1)

                # varre todos as conexões dentro do grafo a partir de atual
                for i in range(len(grafo[ind]) - 1, -1, -1):

                    novo = grafo[ind][i]
                    # print("\tFilho de atual: ",novo)
                    flag = True  # pressuponho que não foi visitado

                    # para cada conexão verifica se já foi visitado
                    for j in range(len(visitado)):
                        if visitado[j][0] == novo:
                            if visitado[j][1] <= (atual.valor2 + 1):
                                flag = False
                            else:
                                visitado[j][1] = atual.valor2 + 1
                            break

                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.valor2 + 1, atual)
                        l2.insereUltimo(novo, atual.valor2 + 1, atual)

                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.valor2 + 1)
                        visitado.append(linha)

                        # verifica se é o objetivo
                        if novo == fim:
                            caminho += l2.exibeCaminho()
                            # print("Árvore de busca:\n",l2.exibeLista())
                            return caminho

        return "caminho não encontrado"