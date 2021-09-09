#---------------------------------------------
#    AQUI COMECA NO NÓ A(Entrada),
#    SEGUINDO LINHA A LINHA DAQUELA IMAGEM 
#    QUE ESTÁ NO GRUPO
#---------------------------------------------

def graph():
    return [
        ["E","C"],                      # Aqui é o nó A
        ["F", "G", "H", "I", "j"],      # Aqui é o nó E
        ["E", "K"],                     # Aqui é o nó F
        ["F", "L"],                     # Aqui é o nó K
        ["E", "L"],                     # Aqui é o nó G
        ["G", "K","O", "M"],            # Aqui é o nó L
        ["A", "D","E"],                 # Aqui é o nó C
        ["E", "M"],                     # Aqui é o nó H
        ["H", "L", "N", "O"],           # Aqui é o nó M
        ["M", "I", "O"],                # Aqui é o nó N
        ["M", "N", "L", "J"],           # Aqui é o nó O
        ["E", "N"],                     # Aqui é o nó I
        ["C", "D", 'J'],                # Aqui é o nó B
        ["B", "C", "J"],                # Aqui é o nó D
        ["B", "D", "C", "E", "O"],      # Aqui é o nó j
    ]