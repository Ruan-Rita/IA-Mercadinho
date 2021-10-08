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

amplitudeClass = AmplitudeMethod()
bidirecionalClass = BirecionalMethod()
profundidadeClass = ProfundidadeMethod()
profundidadeLimitada = ProfundidadeLimitadaMethod()
profundidadeIterativoClass = ProfundidadeIterativoMethod()


origem = "A"
destino = ["F","J"]

# caminho = amplitudeClass.amplitude(origem, destino)
# print("\nAmplitude...........: ", caminho)

caminho = profundidadeClass.profundidade(origem, destino)
print("\nProf. ...: ",caminho)


# caminho = profundidadeLimitada.profundidadeLimitada(origem,destino,2)
# print("\nProf. Limitada (2)..: ",caminho)

# caminho = profundidadeLimitada.profundidadeLimitada(origem,destino,3)
# print("\nProf. Limitada (3)..: ",caminho)

# caminho = profundidadeLimitada.profundidadeLimitada(origem,destino,4)
# print("\nProf. Limitada (4)..: ",caminho)


# caminho = profundidadeIterativoClass.aprofundamentoIterativo(origem,destino)
# print("\nAprof. Iterativo...:",caminho)


# caminho = bidirecionalClass.bidirecional(origem,destino)
# print("\nBidirecional.......: ",caminho)
