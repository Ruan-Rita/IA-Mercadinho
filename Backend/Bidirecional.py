from libsBasic import *
class BirecionalMethod:
    def bidirecional(self, inicio, fim):

            # listas para a busca a partir da origem - busca 1
            l1 = lista()  # busca na FILA
            l2 = lista()  # cópia da árvore completa

            # listas para a busca a partir da destino -  busca 2
            l3 = lista()  # busca na FILA
            l4 = lista()  # cópia da árvore completa

            # cria estrutura para controle de nós visitados
            visitado = []

            l1.insereUltimo(inicio, 0, None)
            l2.insereUltimo(inicio, 0, None)
            linha = []
            linha.append(inicio)
            linha.append(1)
            visitado.append(linha)

            l3.insereUltimo(fim, 0, None)
            l4.insereUltimo(fim, 0, None)
            linha = []
            linha.append(fim)
            linha.append(2)
            visitado.append(linha)

            while True:

                # EXECUÇÃO DO PRIMEIRO AMPLITUDE - BUSCA 1
                flag1 = True
                while flag1:
                    atual = l1.deletaPrimeiro()
                    ind = nos.index(atual.valor1)
                    for i in range(len(grafo[ind])):
                        novo = grafo[ind][i]
                        flag2 = True
                        flag3 = False
                        for j in range(len(visitado)):
                            if visitado[j][0] == novo:
                                if visitado[j][1] == 1:  # visitado na mesma árvore
                                    flag2 = False
                                else:  # visitado na outra árvore
                                    flag3 = True
                                break
                        # for j

                        if flag2:
                            l1.insereUltimo(novo, atual.valor2 + 1, atual)
                            l2.insereUltimo(novo, atual.valor2 + 1, atual)

                            if flag3:
                                caminho = []
                                caminho = l2.exibeCaminho()
                                # caminho = caminho[::-1]
                                caminho += l4.exibeCaminho1(novo)
                                return caminho
                            else:
                                linha = []
                                linha.append(novo)
                                linha.append(1)
                                visitado.append(linha)
                            # if flag3
                        # if flag2
                    # for i

                    if (l1.vazio() != True):
                        aux = l1.primeiro()
                        if aux.valor2 == atual.valor2:
                            flag1 = True
                        else:
                            flag1 = False

                            # EXECUÇÃO DO SEGUNDO AMPLITUDE - BUSCA 2
                flag1 = True
                while flag1:
                    atual = l3.deletaPrimeiro()
                    if atual == None:
                        break
                    ind = nos.index(atual.valor1)
                    for i in range(len(grafo[ind])):
                        novo = grafo[ind][i]
                        flag2 = True
                        flag3 = False
                        for j in range(len(visitado)):
                            if visitado[j][0] == novo:
                                if visitado[j][1] == 2:
                                    flag2 = False
                                else:
                                    flag3 = True
                                break

                        if flag2:
                            l3.insereUltimo(novo, atual.valor2 + 1, atual)
                            l4.insereUltimo(novo, atual.valor2 + 1, atual)

                            if flag3:
                                caminho = []
                                caminho = l4.exibeArvore()
                                caminho = caminho[::-1]
                                caminho += l2.exibeArvore1(novo)
                                return caminho
                            else:
                                linha = []
                                linha.append(novo)
                                linha.append(2)
                                visitado.append(linha)

                    if (l3.vazio() != True):
                        aux = l3.primeiro()
                        if (atual.valor2 == aux.valor2):
                            flag1 = True
                        else:
                            flag1 = False