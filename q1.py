import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image as pil

def RGBtoYIQ():
    img = mpimg.imread("q1Test/Detran_Minas-Gerais.jpg") #o imreadcarrega a imagem como um array de pixels
    plt.imshow(img.astype('uint8'))
    plt.axis('off')
    plt.figure()

    #mascara yiq
    yiq =np.array([[ 0.299 , 0.596,  0.211 ],
                [ 0.587, - 0.274, - 0.523 ],
                [ 0.114, - 0.322 ,0.312 ]]) 

    #mutiplicação das matrizes
    rgbToYiq = np.dot(img/255,yiq)

    x = rgbToYiq
    plt.imsave('q1Test/imagemyiq.png' , np.asarray(np.array((x - np.min(x)) / (np.max(x) - np.min(x)))) )

    #plt.imshow(np.asarray(np.array((x - np.min(x)) / (np.max(x) - np.min(x)))) )
    #plt.axis('off')
    #plt.figure()

    return x          

def YIQtoRGB(rgbToYiq):

    yiq =np.array([[ 0.299 , 0.596,  0.211 ],
                [ 0.587, - 0.274, - 0.523 ],
                [ 0.114, - 0.322 ,0.312 ]]) 

    rgb = np.linalg.inv(yiq)
    
    yiqToRgb = np.dot(rgbToYiq *255,rgb)
    
    yiqToRgb[yiqToRgb > 255] = 255
    yiqToRgb[yiqToRgb < 0]= 0

    y = yiqToRgb
    plt.imsave('q1Test/imagemrgb.png' , np.asarray(np.array((y - np.min(y)) / (np.max(y) - np.min(y)))) )

    #plt.imshow(np.asarray(np.array((y - np.min(y)) / (np.max(y) - np.min(y)))))
    #plt.axis('off')  
    #plt.show()
    
#-----------------Visualização das imagens-----------------------#

filename = ['q1Test/Detran_Minas-Gerais.jpg', 'q1Test/imagemyiq.png', 'q1Test/imagemrgb.png']
titles = ['Original', 'RGB to YIQ', 'YIQ to RGB']
fig=plt.figure(figsize=(8, 8)) #define o tamanho que as figuras terão na janela

#define quantas linhas e colunas de imagem deverão aparecer na mesma janela
columns = 3
rows = 1

figuras=[] #usaremos p/ separar cada imagem p/ poder organiza-las individualmente

for i in range(columns*rows):
    img = mpimg.imread(filename[i])  #lê as imagens
    figuras.append(fig.add_subplot(rows, columns, i+1)) #adiciona os espaços onde as imagens ficarão na janela
    figuras[-1].set_title(titles[i]) #seta os títulos
    plt.imshow(img) #mostra as imagens na janela
    plt.axis('off') #tira a amostragem dos eixos x e y das imagens

plt.show() #inicia o loop pra abertura da janela'''
 

#Pra ver individualmente """
'''
filename = ['pp.png', 'new.png', 'new2.png']
for i in range (len(filename)):
    image = mpimg.imread(filename[i])
    plt.figure()
    plt.imshow(image)
    plt.axis('off')

plt.show()
'''

Rj = RGBtoYIQ()
YIQtoRGB(Rj)