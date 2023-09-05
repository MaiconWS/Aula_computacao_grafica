import cv2
import numpy as np

cores = [
(255, 0, 0),   # Azul
(0, 255, 0),   # Verde
(0, 0, 255),   # Vermelho
]

largura = int(input("Digite o valor da largura da imagen: "))
altura = int(input("Digite o valor da altura da imagen: "))

imagem = np.zeros((altura, largura, 3), dtype=np.uint8)

for y in range(altura):
    for x in range(largura):
        cor = (0,0,255)
        imagem[y, x] = cor

cv2.imwrite('teste.png', imagem)
