class No(object):
    def __init__(self, pai=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai = pai
        self.valor1 = valor1
        self.valor2 = valor2
        self.anterior = anterior
        self.proximo = proximo


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
            novo_no.anterior = self.tail
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

    def primeiro(self):
        return self.head

    def ultimo(self):
        return self.tail

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

    def exibeCaminho1(self, valor):

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


nos = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]

grafo = [
    ["E", "C"],                           # Nó A
    ["C", "D", "J", "E", "G", "H", "I"],  # Nó B
    ["A", "D", "E", "B"],                 # Nó C
    ["B", "C", "J", "G", "H", "I", "E"],  # Nó D
    ["F", "G", "H", "I", "J"],            # Nó E
    ["E", "K"],                           # Nó F
    ["E", "L", "B", "D", "H", "I", "J", "C"],  # Nó G
    ["E", "M", "B", "D", "G", "I", "J", "C"],  # Nó H
    ["E", "N", "B", "D", "G", "H", "J", "C"],  # Nó I
    ["B", "D", "C", "E", "O", "H", "I", "G"],  # Nó J
    ["F", "L"],                 # Nó K
    ["G", "K", "O", "M"],       # Nó L
    ["H", "L", "N", "O"],       # Nó M
    ["M", "I", "O"],            # Nó N
    ["M", "N", "L", "J"]        # Nó O
]

distancia = [
    ["A", "E", 12.5], ["A", "C", 10],
    ["B", "D", 5], ["B", "C", 12.5], ["B", "J", 15], ["B", "E", 27.5], ["B", "I", 20], ["B", "H", 22.5], ["B", "G", 30],
    ["C", "A", 10], ["C", "E", 12.5], ["C", "B", 12.5], ["C", "D", 12.5],
    ["D", "B", 5], ["D", "C", 12.5], ["D", "J", 20], ["D", "E", 27.5], ["D", "G", 30], ["D", "H", 22.5], ["D", "I", 20],
    ["E"]
]