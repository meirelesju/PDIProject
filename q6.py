import numpy as np 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from scipy import signal
from sklearn.preprocessing import normalize


def buscaMascaraCorrelacaoCruzadaNormalizada():
    mascara = mpimg.imread("q6Test/babooneye.png")*255
    mascaraR = []
    mascaraG = []
    mascaraB = []

    for row in mascara:
        # mascara é uma lista de rows que possuem listas de pixels que são listas [R, G, B] cujos indices são [0, 1, 2]
        mascaraR.append([pixel[0] for pixel in row]) # Dá um append no R com uma lista que representa uma linha apenas com o valor de R
        mascaraG.append([pixel[1] for pixel in row]) # Dá um append no G com uma lista que representa uma linha apenas com o valor de G
        mascaraB.append([pixel[2] for pixel in row]) # Dá um append no B com uma lista que representa uma linha apenas com o valor de B

    mascaraNormalizadaR = normalize(np.asmatrix(mascaraR))
    mascaraNormalizadaG = normalize(np.asmatrix(mascaraG))
    mascaraNormalizadaB = normalize(np.asmatrix(mascaraB))

    #tamanho da mascara
    m, n, _ = mascara.shape

    imagem = mpimg.imread("q6Test/baboon.png")*255
    #pegando o tamanho da imagem
    A, L, rgb = imagem.shape
    
    mediaCorrelacoesRGB = np.zeros((A, L))

    #extensão com zeros
    exty = int((m) / 2)
    extx = int((n) / 2)

    #nova matriz extendida
    matrizExt = np.zeros((A+2*exty, L+2*extx, rgb))

    #adicionando valores da imagem original na matrix extendida 
    matrizExt[exty:A+exty, extx:L+extx] = imagem
    #print(matrizExt.shape)

    #pegando os pixels da imagem
    for y in range (exty , A+exty):
        for x in range (extx , L+extx):
            valoresR = normalize(matrizExt[y-exty : y+exty + 1, x-extx : x+extx + 1, 0])
            valoresG = normalize(matrizExt[y-exty : y+exty + 1, x-extx : x+extx + 1, 1])
            ValoresB = normalize(matrizExt[y-exty : y+exty + 1, x-extx : x+extx + 1, 2])
            # mode='valid' define que o resultado da operação não operará em linhas e colunas extendidas por zero
            # será apenas a operação pura entre as duas matrizes
            # boundary='symm' significa que as bordas serão simétricas
            # É necessário pegar o elemento [0][0], pois o correlate2d apenas retorna uma lista de listas, mesmo
            # que o resultado seja apenas um elemento
            correlacaoR = signal.correlate2d(valoresR, mascaraNormalizadaR, mode='valid', boundary='symm')[0][0]
            correlacaoG = signal.correlate2d(valoresG, mascaraNormalizadaG, mode='valid', boundary='symm')[0][0]
            correlacaoB = signal.correlate2d(ValoresB, mascaraNormalizadaB, mode='valid', boundary='symm')[0][0]

            mediaCorrelacoesRGB[y-exty,x-extx] = (correlacaoR + correlacaoG + correlacaoB) / 3

    # Encontra-se a maior correlação:
    maiorCorrelacao = 0
    maiorCorrelacaoX = 0
    maiorCorrelacaoY = 0
    for y in range(len(mediaCorrelacoesRGB)):
        for x in range(len(mediaCorrelacoesRGB[0])):
            if mediaCorrelacoesRGB[y][x] > maiorCorrelacao:
                maiorCorrelacao = mediaCorrelacoesRGB[y][x]
                maiorCorrelacaoX = x
                maiorCorrelacaoY = y

    # Visualização da Imagem
    fig, ax = plt.subplots(1)
    ax.imshow(imagem/255) # Exibe a imagem no gráfico
    # É criado um retângulo para adicionar na imagem:
    rect = patches.Rectangle((maiorCorrelacaoX-extx, maiorCorrelacaoY-exty), n, m, linewidth=3,edgecolor='b',facecolor='none')
    ax.add_patch(rect) # Adiciona o retângulo na imagem
    plt.savefig("q6Test/q6resultado.png") # Salva o que foi plotado
    plt.show()
    

buscaMascaraCorrelacaoCruzadaNormalizada()