import cv2
import numpy as np

cores = [
(255, 0, 0),   # Azul
(0, 255, 0),   # Verde
(0, 0, 255),   # Vermelho
]

x = int(input("Digite o valor da largura da imagen: "))
y = int(input("Digite o valor da altura da imagen: "))

imagem = np.zeros((y, x, 3), dtype=np.uint8)

b,g,r = cores

cv2.imwrite('teste.png', imagem)
