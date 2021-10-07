from Amplitude import AmplitudeMethod
from Bidirecional import BirecionalMethod
from ProfundidadeIterativo import ProfundidadeIterativoMethod
from Profundidade import ProfundidadeMethod 
from ProfundidadeLimitada import ProfundidadeLimitadaMethod

"""
********************************************************************
        PROBLEMA 1: MAPA DE SUPER MERCADO
********************************************************************
"""


caminho = []

op = 2
"""
while op != 1:
    if op == 2:
        origem = input("\nDefina a Origem: ")
        destino = input("Defina o Destino: ")
        op = 3
    escolha = int(input("Escolha qual algoritmo você deseja usar:"
                    "\n1) Amplitude"
                    "\n2) Profundidade\n\n"))
    if escolha == 1:
        caminho = sol.amplitude(origem, destino)
        print("\nAmplitude...........: ", caminho)
        escolha == 0
    if escolha == 2:
        caminho = sol.profundidade(origem, destino)
        print("\nProfundidade........: ", caminho)
        escolha == 0

    op = int(input("\n\nO que você deseja fazer agora?"
               "\n\n1) Sair"
               "\n2) Usar outra origem e destino"
               "\n3) Usar outro algoritmo de busca\n"))
    print(op)
print("ENCERRADO")
"""
amplitudeClass = AmplitudeMethod()
bidirecionalClass = BirecionalMethod()
profundidadeClass = ProfundidadeMethod()
profundidadeLimitada = ProfundidadeLimitadaMethod()
profundidadeIterativoClass = ProfundidadeIterativoMethod()


origem = "A"
destino = ["F","J"]

# caminho = amplitudeClass.amplitude(origem, destino)
# print("\nAmplitude...........: ", caminho)


# caminho = profundidadeLimitada.profundidadeLimitada(origem,destino,2)
# print("\nProf. Limitada (2)..: ",caminho)

# caminho = profundidadeLimitada.profundidadeLimitada(origem,destino,3)
# print("\nProf. Limitada (3)..: ",caminho)

# caminho = profundidadeLimitada.profundidadeLimitada(origem,destino,4)
# print("\nProf. Limitada (4)..: ",caminho)


caminho = profundidadeIterativoClass.aprofundamentoIterativo(origem,destino)
print("\nAprof. Iterativo...:",caminho)


# caminho = bidirecionalClass.bidirecional(origem,destino)
# print("\nBidirecional.......: ",caminho)
