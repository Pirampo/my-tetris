"""
piece.py
Representa uma peça (tetromino) individual: seu tipo, posição
na grade e rotação atual.
"""

import random
from settings import FORMATOS, CORES_PECAS


class Piece:
    def __init__(self, coluna_inicial):
        self.tipo = random.choice(list(FORMATOS.keys()))
        self.rotacoes = FORMATOS[self.tipo]
        self.rotacao_atual = 0
        self.cor = CORES_PECAS[self.tipo]

        # Posição do canto superior-esquerdo da matriz da peça na grade
        self.linha = 0
        self.coluna = coluna_inicial

    def formato(self):
        """Retorna a matriz (lista de listas) da rotação atual."""
        return self.rotacoes[self.rotacao_atual]

    def celulas_ocupadas(self, linha=None, coluna=None, rotacao=None):
        """
        Retorna a lista de coordenadas (linha, coluna) que a peça
        ocupa na grade, considerando uma posição/rotação hipotética
        (útil para testar colisão antes de mover de verdade).
        """
        linha = self.linha if linha is None else linha
        coluna = self.coluna if coluna is None else coluna
        rotacao = self.rotacao_atual if rotacao is None else rotacao

        matriz = self.rotacoes[rotacao]
        celulas = []
        for dy, linha_matriz in enumerate(matriz):
            for dx, valor in enumerate(linha_matriz):
                if valor:
                    celulas.append((linha + dy, coluna + dx))
        return celulas

    def proxima_rotacao(self):
        """Retorna o índice da próxima rotação (sem aplicar ainda)."""
        return (self.rotacao_atual + 1) % len(self.rotacoes)
    