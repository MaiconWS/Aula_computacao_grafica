import cv2
import numpy as np
import random

cores = [
    (255, 0, 0),   # Azul
    (0, 255, 0),   # Verde
    (0, 0, 255),   # Vermelho
    (255, 255, 0), # Amarelo (Azul + Verde)
    (0, 255, 255), # Ciano (Verde + Vermelho)
    (255, 0, 255), # Magenta (Azul + Vermelho)
    (255, 127, 0), # Laranja
    (0, 127, 255), # Rosa
    (127, 127, 127), # Cinza
    (0, 0, 0)     # Preto
]

imagem = np.zeros((50, 50, 3), dtype=np.uint8)

for y in range(50):
    for x in range(50):
        cor_aleatoria = random.choice(cores)
        imagem[y, x] = cor_aleatoria

cv2.imwrite('imagem_aleatoria.png', imagem)