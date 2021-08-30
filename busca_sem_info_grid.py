class No(object):
    def __init__(self, pai=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai       = pai
        self.valor1    = valor1
        self.valor2    = valor2
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, v1, v2, p):
        novo_no = No(p, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, v1, v2, p):

        novo_no = No(p, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no

    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
        
    def exibeLista(self):
        
        aux = self.head
        str = []
        while aux != None:
            temp = []
            temp.append(aux.valor1)
            temp.append(aux.valor2)
            str.append(temp)
            aux = aux.proximo
        
        return str
    
    def exibeCaminho(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.valor1)
            atual = atual.pai
        caminho.append(atual.valor1)
        caminho = caminho[::-1]
        return caminho
    
    def exibeCaminho1(self,valor):
                
        atual = self.head
        while atual.valor1 != valor:
            atual = atual.proximo
    
        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.valor1)
            atual = atual.pai
        caminho.append(atual.valor1)
        return caminho

    def primeiro(self):
        return self.head
    
    def ultimo(self):
        return self.tail

class busca(object):

    def amplitude(self, inicio, fim):
        
        caminho = []

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() is not None:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()
            if atual is None: break

            filhos = []
            filhos = self.sucessor(atual.valor1[0],atual.valor1[1])

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(filhos)):

                novo = filhos[i]
                flag = True  # pressuponho que não foi visitado

                # para cada conexão verifica se já foi visitado
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.valor2+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.valor2+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor2 + 1, atual)
                    l2.insereUltimo(novo, atual.valor2 + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor2+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho += l2.exibeCaminho()
                        #print("Árvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"


    def profundidade(self, inicio, fim):
        
        caminho = []

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)


        while l1.vazio() is not None:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            if atual is None: break

            filhos = []
            filhos = self.sucessor(atual.valor1[0],atual.valor1[1])

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(filhos)):

                novo = filhos[i]
                flag = True  # pressuponho que não foi visitado

                # para cada conexão verifica se já foi visitado
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.valor2+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.valor2+1
                        break
                    
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor2 + 1, atual)
                    l2.insereUltimo(novo, atual.valor2 + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor2+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho += l2.exibeCaminho()
                        #print("Árvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"


    def sucessor(self,x,y):

        f = []

        # direita
        if (y+1)<10:
            if mapa[x][y+1]!="-1":
                linha= []
                linha.append(x)
                linha.append(y+1)
                f.append(linha)

        # esquerda
        if (y-1)>=0:
            if mapa[x][y-1]!="-1":
                linha= []
                linha.append(x)
                linha.append(y-1)
                f.append(linha)

        # acima
        if (x+1)<11:
            if mapa[x+1][y]!="-1":
                linha= []
                linha.append(x+1)
                linha.append(y)
                f.append(linha)

        # abaixo
        if (x-1)>=0:
            if mapa[x-1][y]!="-1":
                linha= []
                linha.append(x-1)
                linha.append(y)
                f.append(linha)

        return f


"""
********************************************************************
        PROBLEMA 3: ASPIRADOR DE PÓ
********************************************************************
"""

mapa = [
            [ "1", "1" ,"1" ,"1", "1", "1", "1", "1", "1", "1"],
            [ "1", "1" ,"1" ,"1", "1", "1", "1","-1", "1", "1"],
            [ "1", "1" ,"1","-1","-1","-1", "1", "1","-1", "1"],
            [ "1", "1","-1","-1", "1", "1", "1", "1","-1", "1"],
            ["-1", "1", "1", "1", "1", "1", "1", "1","-1", "1"],
            ["-1", "1","-1","-1","-1","-1", "1", "1","-1", "1"],
            [ "1", "1","-1", "1", "1", "1", "1", "1", "1", "1"],
            [ "1", "1", "1", "1", "1", "1", "1", "1","-1","-1"],
            [ "1","-1","-1", "1", "1","-1","-1", "1", "1", "1"],
            [ "1","-1", "1", "1", "1", "1", "1", "1", "1", "1"],
            [ "1","-1", "1", "1","-1", "1", "1", "1", "1", "1"]
]


sol = busca()
caminho = []


# PROBLEMA C
origem  = [9,7]
destino = [1,1]


caminho = sol.amplitude(origem,destino)
print("\nAmplitude.......: ",caminho)

caminho = sol.profundidade(origem,destino)
print("Profundidade....: ",caminho)


"""


caminho = sol.profundidade_limitada(origem,destino,2)
print("Prof. Limitada_2: ",caminho)
caminho = sol.profundidade_limitada(origem,destino,3)
print("Prof. Limitada_3: ",caminho)
caminho = sol.profundidade_limitada(origem,destino,4)
print("Prof. Limitada_4: ",caminho)
caminho = sol.aprofundamento_iterativo(origem,destino,10)
print("Aprof. Iterativo: ",caminho)

caminho = sol.bidirecional(origem,destino)
print("Bidirecional....: ",caminho)
"""






"""

    
    def profundidade_limitada(self, inicio, fim, limite):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        flag1 = False
        while l1.vazio() is not None and flag1==False:
            atual = l1.deletaUltimo()
            if atual is None: break

            # verifica o limite
            if atual.valor2 < limite:
                ind = nos.index(atual.valor1)
                for i in range(len(grafo[ind])-1,-1,-1):
                    novo = grafo[ind][i]
                    flag = True
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1]<=(atual.valor2+1):
                                flag = False
                            else:
                                visitado[j][1]=atual.valor2+1
                            break
                    
                    if flag:
                        l1.insereUltimo(novo, atual.valor2 + 1 , atual)
                        l2.insereUltimo(novo, atual.valor2 + 1, atual)
                        linha = []
                        linha.append(novo)
                        linha.append(atual.valor2+1)
                        visitado.append(linha)
                        if novo == fim:
                            flag1 = True
        
        caminho = []
        if flag1:
            caminho = l2.exibeCaminho()
        else:
            caminho = "odartnocne oãn ohnimaC"
        return caminho

    def aprofundamento_iterativo(self, inicio, fim, l_max):
        
        for limite in range(1,l_max+1):
            l1 = lista()
            l2 = lista()
            visitado = []
            
            l1.insereUltimo(inicio,0,None)
            l2.insereUltimo(inicio,0,None)
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
            
            while l1.vazio() is not None:
                atual = l1.deletaUltimo()
                if atual is None: break
                if atual.valor2 < limite:
                    ind = nos.index(atual.valor1)
                    for i in range(len(grafo[ind])-1,-1,-1):
                        novo = grafo[ind][i]
                        flag = True
                        for j in range(len(visitado)):
                            if visitado[j][0]==novo:
                                if visitado[j][1]<=(atual.valor2+1):
                                    flag = False
                                else:
                                    visitado[j][1]=atual.valor2+1
                                break
                        
                        if flag:
                            l1.insereUltimo(novo, atual.valor2 + 1 , atual)
                            l2.insereUltimo(novo, atual.valor2 + 1, atual)
                            linha = []
                            linha.append(novo)
                            linha.append(atual.valor2+1)
                            visitado.append(linha)
                            if novo == fim:
                                caminho = []
                                caminho = l2.exibeCaminho()
                                return caminho

    def bidirecional(self, inicio, fim):

        # listas para a busca a partir da origem - busca 1
        l1 = lista()
        l2 = lista()

        # listas para a busca a partir da destino -  busca 2
        l3 = lista()
        l4 = lista()

        # cria estrutura para controle de nós visitados
        visitado = []

        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)
        linha = []
        linha.append(inicio)
        linha.append(1)
        visitado.append(linha)
        
        l3.insereUltimo(fim,0,None)
        l4.insereUltimo(fim,0,None)
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
                        if visitado[j][0]==novo:
                            if visitado[j][1] == 1:
                                flag2 = False
                            else:
                                flag3 = True
                            break
                    # for j
                        
                    if flag2:
                        l1.insereUltimo(novo, atual.valor2 + 1 , atual)
                        l2.insereUltimo(novo, atual.valor2 + 1, atual)
                        
                        if flag3:
                            caminho = []
                            caminho = l2.exibeCaminho()
                            caminho = caminho[::-1]
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
                
                
                if(l1.vazio()!=True):
                    aux = l1.primeiro()
                    if aux.valor2 == atual.valor2:
                        flag1 = True
                    else:
                        flag1 = False                

            # EXECUÇÃO DO SEGUNDO AMPLITUDE - BUSCA 2
            flag1 = True
            while flag1:
                atual = l3.deletaPrimeiro()
                if atual==None:
                    break
                ind = nos.index(atual.valor1)
                for i in range(len(grafo[ind])):
                    novo = grafo[ind][i]
                    flag2 = True
                    flag3 = False
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1] == 2:
                                flag2 = False
                            else:
                                flag3 = True
                            break
                        
                    if flag2:
                        l3.insereUltimo(novo, atual.valor2 + 1 , atual)
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
                        
                if(l3.vazio() != True):
                    aux = l3.primeiro()
                    if(atual.valor2 == aux.valor2):
                        flag1 = True
                    else:
                        flag1 = False
                

"""