"""
    Aqui começa no nó A(Entrada),
    e seguindo por linha
"""
graph = [
    ["E","C"],                      # aqui é o nó A
    ["F", "G", "H", "I", "j"],      # aqui é o nó E
    ["E", "K"],                      # aqui é o nó F
    ["F", "L"],                      # aqui é o nó K
    ["E", "L"],                      # aqui é o nó G
    ["G", "K","O", "M"],                      # aqui é o nó L
    ["A", "D","E"],                      # aqui é o nó C
    ["E", "M"],                      # aqui é o nó H
    ["H", "L", "N", "O"],                      # aqui é o nó M
    ["M", "I", "O"],                      # aqui é o nó N
    ["M", "N", "L", "J"],                      # aqui é o nó O
    ["E", "N"],                      # aqui é o nó I
    ["C", "D", 'J'],                      # aqui é o nó B
    ["B", "C", "J"],                      # aqui é o nó D
    ["B", "D", "C", "E", "O"],                      # aqui é o nó j
]