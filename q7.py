import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from scipy import signal
from sklearn.preprocessing import normalize

def correlacao(img, mascara):
    soma = 0
    # Shape retorna um par (numero de linhas, numero de colunas):
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            soma += img.item((y,x)) * mascara.item((y,x))

    return soma

pattern = mpimg.imread("q7Test/babooneye.png")*255
pattern_altura = len(pattern)
pattern_largura = len(pattern[0])
pattern_r = []
pattern_g = []
pattern_b = []

for row in pattern:
    # pattern é uma lista de rows que possuem listas de pixels que são listas [R, G, B] cujos indices são [0, 1, 2]
    pattern_r.append([pixel[0] for pixel in row]) # Dá um append no R com uma lista que representa uma linha apenas com o valor de R
    pattern_g.append([pixel[1] for pixel in row]) # Dá um append no G com uma lista que representa uma linha apenas com o valor de G
    pattern_b.append([pixel[2] for pixel in row]) # Dá um append no B com uma lista que representa uma linha apenas com o valor de B

pattern_r = np.asmatrix(pattern_r)
pattern_g = np.asmatrix(pattern_g)
pattern_b = np.asmatrix(pattern_b)

imagem = mpimg.imread("q7Test/baboon.png")*255
imagem_altura = len(imagem)
imagem_largura = len(imagem[0])
imagem_r = []
imagem_g = []
imagem_b = []

for row in imagem:
    # pattern é uma lista de rows que possuem listas de pixels que são listas [R, G, B] cujos indices são [0, 1, 2]
    imagem_r.append([pixel[0] for pixel in row]) # Dá um append no R com uma lista que representa uma linha apenas com o valor de R
    imagem_g.append([pixel[1] for pixel in row]) # Dá um append no G com uma lista que representa uma linha apenas com o valor de G
    imagem_b.append([pixel[2] for pixel in row]) # Dá um append no B com uma lista que representa uma linha apenas com o valor de B

metade_pattern_altura = int(pattern_altura/2)
metade_pattern_largura = int(pattern_largura/2)
# Para obter uma extensão por zero correta é necessário aumentar para cima e 
# para baixo metade do tamanho vertical da mascara
# A tupla indica o aumento em (cima, baixo)
aumento_extensao_vertical = (metade_pattern_altura, metade_pattern_altura)
# Para obter uma extensão por zero correta é necessário aumentar para direita
# e esquerda metade do tamanho horizontal da mascara
# A tupla indica o aumento em (esquerda, direita)
aumento_extensao_horizontal = (metade_pattern_largura, metade_pattern_largura)
# Adiciona a extensão por zeros:
r_extensao_zero = np.pad(imagem_r, (aumento_extensao_vertical, aumento_extensao_horizontal), 'constant')
g_extensao_zero = np.pad(imagem_g, (aumento_extensao_vertical, aumento_extensao_horizontal), 'constant')
b_extensao_zero = np.pad(imagem_b, (aumento_extensao_vertical, aumento_extensao_horizontal), 'constant')

media_correlacao = []
for y in range(imagem_altura):
    # Checa se a vizinhança que será executada agora não ultrapassará a altura da imagem:
    if imagem_altura < (y + pattern_altura):
        # Porque se for ultrapassar já encerra a extração de correlações:
        break

    media_correlacao_linha = []
    for x in range(imagem_largura):
        # Checa se a vizinhança que será executada agora não ultrapassará a largura da linha da imagem:
        if imagem_largura < (x + pattern_largura):
            # Porque se for ultrapassar já pula pra próxima linha:
            break
        
        xs_da_vizinhanca = [index for index in range(x, x + pattern_largura)]
        ys_da_vizinhanca = [index for index in range(y, y + pattern_altura)]
        # ix gera uma matriz de pares com todas as possibilidades dos indices do primeiro parametro com os
        # indices do segundo parametro, ou seja, se for passado [0,2] e [6,7] 
        # ele gerará uma matriz de indices: [[0,6], [0,7], [2,6], [2,7]]
        indices_da_vizinhanca = np.ix_(ys_da_vizinhanca, xs_da_vizinhanca)

        r_vizinhanca = r_extensao_zero[indices_da_vizinhanca]
        g_vizinhanca = g_extensao_zero[indices_da_vizinhanca]
        b_vizinhanca = b_extensao_zero[indices_da_vizinhanca]

        r_correlacao = correlacao(r_vizinhanca, pattern_r)
        g_correlacao = correlacao(g_vizinhanca, pattern_g)
        b_correlacao = correlacao(b_vizinhanca, pattern_b)
        
        media_correlacao_rgb = (r_correlacao + g_correlacao + b_correlacao)/3

        media_correlacao_linha.append(media_correlacao_rgb)
    media_correlacao.append(media_correlacao_linha)

# Encontra-se a maior correlação:
maior_correlacao = 0
maior_correlacao_x = 0
maior_correlacao_y = 0
for y in range(len(media_correlacao)):
    for x in range(len(media_correlacao[0])):
        if media_correlacao[y][x] > maior_correlacao:
            maior_correlacao = media_correlacao[y][x]
            maior_correlacao_x = x
            maior_correlacao_y = y

fig,ax = plt.subplots(1)
ax.imshow(imagem/255)
rect = patches.Rectangle((maior_correlacao_x-metade_pattern_largura, maior_correlacao_y-metade_pattern_altura), pattern_largura, pattern_altura, linewidth=3,edgecolor='b',facecolor='none')
ax.add_patch(rect)
plt.show()