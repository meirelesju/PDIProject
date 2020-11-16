import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

<<<<<<< HEAD
def RGBtoYIQ(filename):
    img = mpimg.imread(filename) #o imreadcarrega a imagem sendo um array de pixels
=======
def RGBtoYIQ():
    img = mpimg.imread("q1Test/Detran_Minas-Gerais.jpg") #o imreadcarrega a imagem sendo um array de pixels
>>>>>>> c7de1c3fd70acc2f515398ed8aabcfee85170137

    #mascara yiq
    yiq =np.array([[ 0.299 , 0.596,  0.211 ],
                [ 0.587, - 0.274, - 0.523 ],
                [ 0.114, - 0.322 ,0.312 ]]) 

    #mutiplicação das matrizes
    rgbToYiq = np.dot(img/255,yiq) # divide por 255 para ficar com valores entre 0 e 1
    return rgbToYiq        

<<<<<<< HEAD
def YIQtoRGB(rgbToYiq, filepath):
=======
def YIQtoRGB(rgbToYiq):
>>>>>>> c7de1c3fd70acc2f515398ed8aabcfee85170137
    #mascara yiq
    yiq =np.array([[ 0.299 , 0.596,  0.211 ],
                [ 0.587, - 0.274, - 0.523 ],
                [ 0.114, - 0.322 ,0.312 ]]) 
                
    #o "inv" server para inverter a matriz yiq pra virar uma matriz rgb
    rgb = np.linalg.inv(yiq)
<<<<<<< HEAD

    yiqToRgb = np.dot(rgbToYiq,rgb) 
    
    yiqToRgb[yiqToRgb > 1] = 1
    yiqToRgb[yiqToRgb < 0] = 0
    plt.imsave(filepath, yiqToRgb)

#-----------------Visualização das imagens-----------------------#
def printImages():
    filename = [initialPath, savePath]
    titles = ['Original', 'YIQ to RGB']
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

    plt.show() #inicia o loop pra abertura da janela

#Quando importar na questão 2, só irá rodar as funções que eu chamar por causa desse if 
if __name__ == "__main__":
    
    initialPath = 'q1Test/slides.jpg'
    yiq = RGBtoYIQ(initialPath)
    savePath = 'q1Test/imagemrgb.jpg'
    YIQtoRGB(yiq, savePath)
    printImages()
=======
   
    yiqToRgb = np.dot(rgbToYiq, rgb)
    print(yiqToRgb) 
    
    yiqToRgb[yiqToRgb > 1] = 1
    yiqToRgb[yiqToRgb < 0] = 0
    plt.imsave( 'q1Test/imagemrgb.png', yiqToRgb)
   

#-----------------Visualização das imagens-----------------------#

yiq = RGBtoYIQ()
YIQtoRGB(yiq)

filename = ['q1Test/Detran_Minas-Gerais.jpg','q1Test/imagemrgb.png']
titles = ['Original', 'YIQ to RGB']
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
>>>>>>> c7de1c3fd70acc2f515398ed8aabcfee85170137
