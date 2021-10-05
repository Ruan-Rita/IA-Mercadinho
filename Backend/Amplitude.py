from libsBasic import *
class AmplitudeMethod:

    def amplitude(self, inicio, fim):

        totalObj = len(fim)
        cont = int(0)
        caminho = []

        while True:
            print("0---)==================> : While de nivel 1")
            # manipular a FILA para a busca
            l1 = lista()

            # cópia para apresentar o caminho (somente inserção)
            l2 = lista()

            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio, 0, None)
            l2.insereUltimo(inicio, 0, None)
            print("Insere ponto inicial?  ")
            print("l1")
            print(l1.exibeCaminho())
            # print(l1.exibeCaminho1())
            print("l2")
            print(l2)

            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
            flag5 = True
            
            print("linha")
            print(linha)

            print("visitado")
            print(visitado)

            while l1.vazio() == False and flag5:
                print("0---)==================> : While de nivel 2")

                # remove o primeiro da fila
                atual = l1.deletaPrimeiro()
                # atual = l1.primeiro()
                print("atual =====----===--==-=-=-===-=-=-=-=-=-=-=-=")
                print(atual.valor1)
                print(atual.valor2)
                
                # print(if atual "Está vazio" else "Não alguma coisa")

                if atual is None: break

                ind = nos.index(atual.valor1)
                print("index do no atual")
                print(ind)
                # varre todos as conexões dentro do grafo a partir de atual
                for i in range(len(grafo[ind])):
                    print("0---)==================> : While de nivel 3")


                    novo = grafo[ind][i]
                    print("novo nó a ser percorrido")
                    print(novo)

                    # pressuponho que não foi visitado
                    flag = True

                    # controle de nós repetidos
                    print("controle de nós ---------------------------------------------------")
                    for j in range(len(visitado)):
                        print("visitado: " , visitado[j][0] , " é == novo: ", novo)
                        if visitado[j][0] == novo:
                            print("sim ele é ")
                            print("visitado[j][1] ", visitado[j][1] , " é == (atual.valor2 + 1):" , (atual.valor2 + 1))
                            
                            if visitado[j][1] <= (atual.valor2 + 1):
                                print("sim ele ja foi visitado")
                                flag = False
                            else:
                                print("não foi visitado")
                                visitado[j][1] = atual.valor2 + 1
                            break
                        
                        if novo in caminho:
                            flag = False
                        

                    print("Fim controle de nós ---------------------------------------------------")

                    # se não foi visitado inclui na fila
                    if flag:
                        print("vamos adiconar um no na fila")
                        
                        l1.insereUltimo(novo, atual.valor2 + 1, atual)
                        l2.insereUltimo(novo, atual.valor2 + 1, atual)
                        print("l1")
                        print(l1.exibeCaminho())
                        print("l2")
                        print(l2.exibeCaminho())
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.valor2 + 1)
                        print("novo")
                        print(novo)
                        
                        print("atual valor2")
                        print(atual.valor2 + 1)


                        visitado.append(linha)
                        print("add no visitado")
                        print(visitado)

                        # verifica se é o objetivo
                        if novo in fim:
                            print("novo está contido no fim")
                            print("novo é:" + novo)
                            print("L2 Caminho vai add no caminho -------------------------878787887878")
                            print(l2.exibeCaminho())
                            
                            

                            caminho += l2.exibeCaminho()
                            print("caminho  ")
                            print(caminho)
                            fim.remove(novo)
                            print("NovoFim: ")
                            print(fim)  
                            print("NovoInicio: ")
                            print(novo)                          
                            inicio = novo
                            flag5 = False
                            # print("Fila:\n",l1.exibeLista())
                            # print("\nÁrvore de busca:\n",l2.exibeLista())
                            cont += 1
                            if cont < totalObj:
                                print("cont: ")
                                print(cont)
                                caminho.pop()
                                print("cont < totalObj remove caminho:-********************************************- ")
                                print("Próximo Fim: ")
                                print(fim)
                                print("Caminho:")
                                print(caminho)
                                # TESTE -------------------------------------------------------
                                # l1 = lista()
                                # l1.insereUltimo(novo, 0, None)
                                
                                # TESTE -------------------------------------------------------
                                # manipular a FILA para a busca
                                l1 = lista()
                                # cópia para apresentar o caminho (somente inserção)
                                l2 = lista()
                                # insere ponto inicial como nó raiz da árvore
                                l1.insereUltimo(inicio, 0, None)
                                l2.insereUltimo(inicio, 0, None)
                                print("l1")
                                print(l1.exibeCaminho())
                                print("l2")
                                print(l2.exibeCaminho())
                                break
                                # l1.insereUltimo(novo, 0, None)
                            else:
                                print("Acabou - ")
                                return caminho

        return "caminho não encontrado"