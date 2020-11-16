from q1 import RGBtoYIQ, YIQtoRGB
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np

<<<<<<< HEAD
filepath = "q2Test/slides.jpg"

class Imagem:
    img = Image.open(filepath) #abre a imagem p/ leitura
    width, height = img.size #retorna uma tupla com a altura e largura da imagem e seta os valores nas variaveis
     
def negative(str):
    out = Image.new('RGB', Imagem.img.size) #cria o arquivo que vai salvar a imagem convertida
    print("Convertendo para negativo na banda desejada")
    for x in range(Imagem.width):
        for y in range(Imagem.height):
            
            if str == 'R':
                [R,G,B] = Imagem.img.getpixel((x,y)) #pega os valores rgb do pixel indicado e seta nas variáveis
                Rpixel  = 255 - R
                out.putpixel((x,y),(Rpixel, G, B)) #coloca os novos valores dos pixels no arquivo que foi criado p/ salvar a imagem convertida
                filename = 'R.jpg'
            
            if str == 'G':
                [R,G,B] = Imagem.img.getpixel((x,y)) 
                Gpixel  = 255 - G
                out.putpixel((x,y),(R, Gpixel, B)) 
                filename = 'G.jpg'
            
            if str == 'B':
                [R,G,B] = Imagem.img.getpixel((x,y)) 
                Bpixel  = 255 - B      
                out.putpixel((x,y),(R, G, Bpixel)) 
                filename = 'B.jpg'

            if str == 'RGB':
                [R,G,B] = Imagem.img.getpixel((x,y)) 
                Rpixel  = 255 - R
                Gpixel  = 255 - G
                Bpixel  = 255 - B      
                out.putpixel((x,y),(Rpixel, Gpixel, Bpixel)) 
                filename = 'RGB.jpg'

    out.save('q2Test/negative'+filename)#salva a imagem nova/convertida
    print("Done!")

def negativeY():
    filename = 'q2Test/slides.jpg'
    arr = np.array(RGBtoYIQ(filename))
    height, width, banda = arr.shape # altura, largura e banda (que são 3)
    
    print("Convertendo para negativo na banda y")  
    for x in range(width):
        for y in range(height):            
            arr[y,x,0] = 1 - arr[y,x,0]  
            #print(arr[x,y,0])
   
    YIQtoRGB(arr, 'q2Test/negativeY.jpg')
  
    print("Done!")

=======
def RGBtoYIQ():
    img = Image.open("q2Test/slides.png") #abre a imagem p/ leitura
    width, height = img.size #retorna uma tupla com a altura e largura da imagem e seta os valores nas variaveis
    out = Image.new('RGB', img.size) #cria o arquivo que vai salvar a imagem convertida 

    print ("Convertendo RGB para YIQ")
    for x in range (width):
        for y in range (height):
            [R,G,B] = img.getpixel((x, y)) #pega os valores rgb do pixel indicado e seta nas variáveis   

            R = R/255
            G = G/255
            B = B/255      
            Y = 0.299*R + 0.587*G + 0.114*B
            I = 0.596*R - 0.274*G - 0.322*B
            Q = 0.211*R - 0.523*G + 0.312*B   
         
            #print (Y, I, Q)
            #I+=128
            #Q+=128
            
            value = (round(Y*255),round(I*255),round(Q*255))
            out.putpixel((x, y), value) #coloca os novos valores dos pixels no arquivo que foi criado p/ salvar a imagem convertida
    out.save('q2Test/slides1.png') #salva a imagem nova/convertida
    print("Done!")

def YIQtoRGB():
    img2 = Image.open("q2Test/slides1.png")
    width, height = img2.size

    out2 = Image.new('RGB', img2.size)
    print ("Convertendo YIQ para RGB")
    for x in range (width):
            for y in range (height):
                [Y,I,Q] = img2.getpixel((x, y))
                
                #I-=128
                #Q-=128
          
                Y = Y /255
                I = I/255
                Q =
                R = 1.000*Y + 0.956*I + 0.621*Q
                G = 1.000*Y - 0.272*I - 0.647*Q
                B = 1.000*Y - 1.106*I + 1.703*Q
                
                if R >= 1:
                    R=1 
                if G >= 1:
                    G=1
                if B >= 1:
                    B=1
                if R <= 0:
                    R=0 
                if G <= 0:
                    G=0
                if B <= 0:
                    B=0
                
                value = ((R),(G),(B))
                out2.putpixel((x, y), value)
        
    out2.save('q2Test/slides3.png')
    print("Done!")


RGBtoYIQ()
YIQtoRGB()
>>>>>>> c7de1c3fd70acc2f515398ed8aabcfee85170137

banda = 'RGB'
negative(banda)
#negativeY()

<<<<<<< HEAD
#-----------------Visualização das imagens-----------------------#
name = 'q2Test/negative'
filename = ['q2Test/slides.jpg', name+ banda+'.jpg']
titles = ['Original', 'Negativa']
=======
filename = ['q2Test/slides.png', 'q2Test/slides1.png', 'q2Test/slides3.png']
titles = ['Original', 'RGB to YIQ', 'YIQ to RGB']
>>>>>>> c7de1c3fd70acc2f515398ed8aabcfee85170137
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

plt.show() #inicia o loop pra abertura da janela

<<<<<<< HEAD

=======
'''
#Pra ver individualmente
filename = ['pp.png', 'new.png', 'new2.png']
for i in range (len(filename)):
    image = mpimg.imread(filename[i])
    plt.figure()
    plt.imshow(image)
    plt.axis('off')
plt.show()
'''
>>>>>>> c7de1c3fd70acc2f515398ed8aabcfee85170137
