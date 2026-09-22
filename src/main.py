"""
main.py
Ponto de entrada do jogo. Cuida do loop principal: capturar input,
atualizar o estado (queda da peça, colisão, linhas completas) e
desenhar tudo na tela.
 
Rode com: python3 src/main.py  (a partir da raiz do projeto)
"""
 
import pygame
import sys
 
from settings import (
    COLUNAS, LINHAS, TAMANHO_CELULA, LARGURA_TELA, ALTURA_TELA,
    PRETO, CINZA_ESCURO, BRANCO, FPS, VELOCIDADE_QUEDA_MS,
)
from board import Board
from pieces import Piece
 
 
def desenhar_grade(tela):
    """Desenha as linhas de grade só pra referência visual."""
    for x in range(0, LARGURA_TELA, TAMANHO_CELULA):
        pygame.draw.line(tela, CINZA_ESCURO, (x, 0), (x, ALTURA_TELA))
    for y in range(0, ALTURA_TELA, TAMANHO_CELULA):
        pygame.draw.line(tela, CINZA_ESCURO, (0, y), (LARGURA_TELA, y))
 
 
def desenhar_board(tela, board):
    """Desenha os blocos já fixados no tabuleiro."""
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            cor = board.grade[linha][coluna]
            if cor is not None:
                retangulo = pygame.Rect(
                    coluna * TAMANHO_CELULA,
                    linha * TAMANHO_CELULA,
                    TAMANHO_CELULA,
                    TAMANHO_CELULA,
                )
                pygame.draw.rect(tela, cor, retangulo)
 
 
def desenhar_peca(tela, peca):
    """Desenha a peça que está caindo no momento."""
    for linha, coluna in peca.celulas_ocupadas():
        if linha >= 0:  # não desenha o que ainda está acima do topo
            retangulo = pygame.Rect(
                coluna * TAMANHO_CELULA,
                linha * TAMANHO_CELULA,
                TAMANHO_CELULA,
                TAMANHO_CELULA,
            )
            pygame.draw.rect(tela, peca.cor, retangulo)
 
 
def peca_pode_mover(board, peca, delta_linha=0, delta_coluna=0, nova_rotacao=None):
    """Testa se mover/rotacionar a peça resultaria em posição válida."""
    rotacao = peca.rotacao_atual if nova_rotacao is None else nova_rotacao
    celulas_teste = peca.celulas_ocupadas(
        linha=peca.linha + delta_linha,
        coluna=peca.coluna + delta_coluna,
        rotacao=rotacao,
    )
    return board.posicao_valida(celulas_teste)
 
 
def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Meu Tetris")
    relogio = pygame.time.Clock()
 
    board = Board()
    peca_atual = Piece(coluna_inicial=COLUNAS // 2 - 2)
 
    tempo_ultima_queda = pygame.time.get_ticks()
    pontuacao = 0
    jogo_ativo = True
 
    while jogo_ativo:
        agora = pygame.time.get_ticks()
 
        # --- Eventos (input do jogador) ---
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_ativo = False
 
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and peca_pode_mover(board, peca_atual, delta_coluna=-1):
                    peca_atual.coluna -= 1
                elif evento.key == pygame.K_RIGHT and peca_pode_mover(board, peca_atual, delta_coluna=1):
                    peca_atual.coluna += 1
                elif evento.key == pygame.K_DOWN and peca_pode_mover(board, peca_atual, delta_linha=1):
                    peca_atual.linha += 1
                elif evento.key == pygame.K_UP:
                    nova_rotacao = peca_atual.proxima_rotacao()
                    if peca_pode_mover(board, peca_atual, nova_rotacao=nova_rotacao):
                        peca_atual.rotacao_atual = nova_rotacao
 
        # --- Queda automática por tempo ---
        if agora - tempo_ultima_queda > VELOCIDADE_QUEDA_MS:
            if peca_pode_mover(board, peca_atual, delta_linha=1):
                peca_atual.linha += 1
            else:
                # peça não pode mais descer: fixa no tabuleiro
                board.fixar_peca(peca_atual)
                linhas_removidas = board.limpar_linhas_completas()
                pontuacao += linhas_removidas * 100
 
                if board.topo_bloqueado():
                    print(f"Game over! Pontuação final: {pontuacao}")
                    jogo_ativo = False
                else:
                    peca_atual = Piece(coluna_inicial=COLUNAS // 2 - 2)
 
            tempo_ultima_queda = agora
 
        # --- Desenho ---
        tela.fill(PRETO)
        desenhar_grade(tela)
        desenhar_board(tela, board)
        desenhar_peca(tela, peca_atual)
        pygame.display.set_caption(f"Meu Tetris — Pontuação: {pontuacao}")
        pygame.display.flip()
 
        relogio.tick(FPS)
 
    pygame.quit()
    sys.exit()
 
 
if __name__ == "__main__":
    main()