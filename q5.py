import numpy as np 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
def mediana ():

    imagem = mpimg.imread("q5Test/Detran_Minas-Gerais.jpg")
    #tamanho da mascara
    m = 3
    n = 3
    #pegando o tamanho da imagem
    A, L, rgb = imagem.shape
    #matriz pra armazenar a saida
    filtroMediana = np.zeros_like(imagem)

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
        for x in range (extx , L +extx):
            
            valoresR = matrizExt[y-exty : y+exty + 1, x-extx : x+extx + 1, 0]
            valoresG = matrizExt[y-exty : y+exty + 1, x-extx : x+extx + 1, 1]
            ValoresB = matrizExt[y-exty : y+exty + 1, x-extx : x+extx + 1, 2]
          
            if valoresR.shape[0]* valoresR.shape[1] == 4*2:
                print(valoresR.shape)

            medianaR = int(np.median(valoresR))
            medianaG = int(np.median(valoresG))
            medianaB = int(np.median(ValoresB))
             

            filtroMediana[y -exty,x -extx,0] = medianaR
            filtroMediana[y -exty,x -extx,1] = medianaG
            filtroMediana[y -exty,x -extx,2] = medianaB

    #plt.imshow(filtroMediana)
    #plt.axis('off')
    #plt.show()
    plt.imsave( 'q1Test/filtromediana.png', filtroMediana)
    

mediana()

#-----------------Visualização das imagens-----------------------#


filename = ['q5Test/Detran_Minas-Gerais.jpg','q1Test/filtromediana.png']
titles = ['Original', 'Filtro Mediana']
fig=plt.figure(figsize=(7, 7)) #define o tamanho que as figuras terão na janela

#define quantas linhas e colunas de imagem deverão aparecer na mesma janela
columns = 2
rows = 1

figuras=[] #usaremos p/ separar cada imagem p/ poder organiza-las individualmente

for i in range(columns*rows):
    img = mpimg.imread(filename[i])  #lê as imagens
    figuras.append(fig.add_subplot(rows, columns, i+1)) #adiciona os espaços onde as imagens ficarão na janela
    figuras[-1].set_title(titles[i]) #seta os títulos
    plt.imshow(img) #mostra as imagens na janela
    plt.axis('off') #tira a amostragem dos eixos x e y das imagens

plt.show() #inicia o loop pra abertura da janela'''