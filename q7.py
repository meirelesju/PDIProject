import numpy as np 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from scipy import signal
from sklearn.preprocessing import normalize


def correlacao():
    mask = mpimg.imread("q7Test\\babooneye.png")*255
    maskR = []
    maskG = []
    maskB = []

    for row in mask:
        # mask é uma lista de rows que possuem listas de pixels que são listas [R, G, B] cujos indices são [0, 1, 2]
        maskR.append([pixel[0] for pixel in row]) # Dá um append no R com uma lista que representa uma linha apenas com o valor de R
        maskG.append([pixel[1] for pixel in row]) # Dá um append no G com uma lista que representa uma linha apenas com o valor de G
        maskB.append([pixel[2] for pixel in row]) # Dá um append no B com uma lista que representa uma linha apenas com o valor de B

    maskR = np.asarray(maskR)
    maskG = np.asarray(maskG)
    maskB = np.asarray(maskB)

    #tamanho da mask
    h, w, _ = mask.shape

    imagem = mpimg.imread("q7Test\\baboon.png")*255
    #pegando o tamanho da imagem
    A, L, rgb = imagem.shape
    
    mediaCorrelacoesRGB = np.zeros((A, L))

    #extensão com zeros
    exty = int((h) / 2)
    extx = int((w) / 2)

    #nova matriz extendida
    matrizExt = np.zeros((A+2*exty, L+2*extx, rgb))

    #adicionando valores da imagem original na matrix extendida 
    matrizExt[exty:A+exty, extx:L+extx] = imagem
    #print(matrizExt.shape)

    #pegando os pixels da imagem
    for y in range (exty , A+exty):
        for x in range (extx , L+extx):
            valoresR = matrizExt[y-exty : y+exty + 1, x-extx : x+extx + 1, 0]
            valoresG = matrizExt[y-exty : y+exty + 1, x-extx : x+extx + 1, 1]
            valoresB = matrizExt[y-exty : y+exty + 1, x-extx : x+extx + 1, 2]
            
            sumR = 0
            sumG = 0
            sumB = 0
            for m in range(h):
                for n in range(w):
                    sumR += maskR.item((m,n)) * valoresR.item((m,n))
                    sumG += maskG.item((m,n)) * valoresG.item((m,n))
                    sumB += maskB.item((m,n)) * valoresB.item((m,n))

            mediaCorrelacoesRGB[y-exty,x-extx] = (sumR + sumG + sumB) / 3

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
    rect = patches.Rectangle((maiorCorrelacaoX-extx, maiorCorrelacaoY-exty), w, h, linewidth=3,edgecolor='b',facecolor='none')
    ax.add_patch(rect) # Adiciona o retângulo na imagem
    plt.savefig("q7Test\\resultado.png") # Salva o que foi plotado
    plt.show()
    

correlacao()