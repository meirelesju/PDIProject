from q1 import RGBtoYIQ, YIQtoRGB
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np

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


banda = 'RGB'
negative(banda)
#negativeY()

#-----------------Visualização das imagens-----------------------#
name = 'q2Test/negative'
filename = ['q2Test/slides.jpg', name+ banda+'.jpg']
titles = ['Original', 'Negativa']
fig=plt.figure(figsize=(8, 8)) #define o tamanho que as figuras terão na janela

#define quantas linhas e colunas de imagem deverão aparecer na mesma janela
columns = 2
rows = 1

figuras=[] #usaremos p/ separar cada imagem p/ poder organiza-las individualmente

for i in range(columns*rows): 
    img = mpimg.imread(filename[i]) #lê as imagens
    figuras.append(fig.add_subplot(rows, columns, i+1)) #adiciona os espaços onde as imagens ficarão na janela
    figuras[-1].set_title(titles[i]) #seta os títulos
    plt.imshow(img) #mostra as imagens na janela
    plt.axis('off') #tira a amostragem dos eixos x e y das imagens

plt.show() #inicia o loop pra abertura da janela

