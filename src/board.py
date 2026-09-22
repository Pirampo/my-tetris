"""
board.py
Representa o tabuleiro do jogo: a grade fixa (blocos já assentados),
verificação de colisão e remoção de linhas completas.
"""

from settings import COLUNAS, LINHAS


class Board:
    def __init__(self):
        # grade[linha][coluna] = None (vazio) ou uma cor (bloco fixo)
        self.grade = [[None for _ in range(COLUNAS)] for _ in range(LINHAS)]

    def posicao_valida(self, celulas):
        """
        Verifica se todas as células (linha, coluna) de uma peça
        estão dentro dos limites e não colidem com blocos já fixados.
        """
        for linha, coluna in celulas:
            if coluna < 0 or coluna >= COLUNAS:
                return False
            if linha >= LINHAS:
                return False
            if linha >= 0 and self.grade[linha][coluna] is not None:
                return False
        return True

    def fixar_peca(self, peca):
        """Grava a peça atual permanentemente na grade."""
        for linha, coluna in peca.celulas_ocupadas():
            if linha >= 0:  # ignora células que ainda estão acima do topo
                self.grade[linha][coluna] = peca.cor

    def limpar_linhas_completas(self):
        """
        Remove linhas totalmente preenchidas e desce as linhas acima.
        Retorna quantas linhas foram removidas (útil para pontuação).
        """
        linhas_restantes = [linha for linha in self.grade if not all(linha)]
        quantidade_removida = LINHAS - len(linhas_restantes)

        # adiciona linhas vazias no topo para repor o que foi removido
        for _ in range(quantidade_removida):
            linhas_restantes.insert(0, [None for _ in range(COLUNAS)])

        self.grade = linhas_restantes
        return quantidade_removida

    def topo_bloqueado(self):
        """Se a linha do topo já tem algum bloco, é game over."""
        return any(celula is not None for celula in self.grade[0])