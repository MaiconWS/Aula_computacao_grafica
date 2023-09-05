# pip install opencv-python

import cv2

imagem = cv2.imread("arquivo.png")

if imagem is None:
    print("Erro ao carregar a imagem!")
    exit()

altura, largura, canais = imagem.shape

print(f"Número total de pixels: {altura * largura}")
print(f"Largura da imagem: {largura} pixels")
print(f"Altura da imagem: {altura} pixels")

# B, G, R = cv2.split(imagem)

x, y = 9, 9
pixel = imagem[y, x]
b, g, r = pixel

print(f"Pixel em ({x}, {y}):")
print(f"Vermelho (R): {r}")
print(f"Verde (G): {g}")
print(f"Azul (B): {b}")

cv2.imshow("Imagem Original", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()