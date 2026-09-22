"""
settings.py
Todas as constantes do jogo ficam aqui: tamanho da grade, cores,
velocidade, e o formato de cada peça (tetromino).

Manter isso separado facilita ajustar o "balanceamento" do jogo
sem mexer na lógica em outros arquivos.
"""

# --- Dimensões da grade (tabuleiro) ---
COLUNAS = 10
LINHAS = 20
TAMANHO_CELULA = 30  # em pixels

LARGURA_TELA = COLUNAS * TAMANHO_CELULA
ALTURA_TELA = LINHAS * TAMANHO_CELULA

# --- Cores (R, G, B) ---
PRETO = (0, 0, 0)
CINZA_ESCURO = (30, 30, 30)
BRANCO = (255, 255, 255)

CORES_PECAS = {
    "I": (0, 255, 255),
    "O": (255, 255, 0),
    "T": (160, 32, 240),
    "S": (0, 255, 0),
    "Z": (255, 0, 0),
    "J": (0, 0, 255),
    "L": (255, 165, 0),
}

# --- Velocidade ---
FPS = 60
VELOCIDADE_QUEDA_MS = 500  # peça desce uma linha a cada X milissegundos

# --- Formatos das peças ---
# Cada peça é definida por uma lista de rotações.
# Cada rotação é uma matriz de 0s e 1s (1 = bloco preenchido).
FORMATOS = {
    "I": [
        [[0, 0, 0, 0],
         [1, 1, 1, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],
        [[0, 0, 1, 0],
         [0, 0, 1, 0],
         [0, 0, 1, 0],
         [0, 0, 1, 0]],
    ],
    "O": [
        [[1, 1],
         [1, 1]],
    ],
    "T": [
        [[0, 1, 0],
         [1, 1, 1],
         [0, 0, 0]],
        [[0, 1, 0],
         [0, 1, 1],
         [0, 1, 0]],
        [[0, 0, 0],
         [1, 1, 1],
         [0, 1, 0]],
        [[0, 1, 0],
         [1, 1, 0],
         [0, 1, 0]],
    ],
    "S": [
        [[0, 1, 1],
         [1, 1, 0],
         [0, 0, 0]],
        [[0, 1, 0],
         [0, 1, 1],
         [0, 0, 1]],
    ],
    "Z": [
        [[1, 1, 0],
         [0, 1, 1],
         [0, 0, 0]],
        [[0, 0, 1],
         [0, 1, 1],
         [0, 1, 0]],
    ],
    "J": [
        [[1, 0, 0],
         [1, 1, 1],
         [0, 0, 0]],
        [[0, 1, 1],
         [0, 1, 0],
         [0, 1, 0]],
        [[0, 0, 0],
         [1, 1, 1],
         [0, 0, 1]],
        [[0, 1, 0],
         [0, 1, 0],
         [1, 1, 0]],
    ],
    "L": [
        [[0, 0, 1],
         [1, 1, 1],
         [0, 0, 0]],
        [[0, 1, 0],
         [0, 1, 0],
         [0, 1, 1]],
        [[0, 0, 0],
         [1, 1, 1],
         [1, 0, 0]],
        [[1, 1, 0],
         [0, 1, 0],
         [0, 1, 0]],
    ],
}