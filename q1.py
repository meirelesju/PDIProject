import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

def RGBtoYIQ():
    img = Image.open("q1Test/Detran_Minas-Gerais.jpg") #abre a imagem p/ leitura
    width, height = img.size #retorna uma tupla com a altura e largura da imagem e seta os valores nas variaveis
    out = Image.new('RGB', img.size) #cria o arquivo que vai salvar a imagem convertida 

    print ("Convertendo RGB para YIQ")
    for x in range (width):
        for y in range (height):
            [R,G,B] = img.getpixel((x, y)) #pega os valores rgb do pixel indicado e seta nas variáveis         
            Y = 0.299*R + 0.587*G + 0.114*B
            I = 0.596*R - 0.274*G - 0.322*B
            Q = 0.211*R - 0.523*G + 0.312*B   
         
            #print (Y, I, Q)
            #I+=128
            #Q+=128
            
            value = (round(Y),round(I),round(Q))
            out.putpixel((x, y), value) #coloca os novos valores dos pixels no arquivo que foi criado p/ salvar a imagem convertida
    out.save('q1Test/new.jpg') #salva a imagem nova/convertida
    print("Done!")

def YIQtoRGB():
    img2 = Image.open("q1Test/new.jpg")
    width, height = img2.size

    out2 = Image.new('RGB', img2.size)
    print ("Convertendo YIQ para RGB")
    for x in range (width):
            for y in range (height):
                [Y,I,Q] = img2.getpixel((x, y))
                
                #I-=128
                #Q-=128
          
                R = 1.000*Y + 0.956*I + 0.621*Q
                G = 1.000*Y - 0.272*I - 0.647*Q
                B = 1.000*Y - 1.106*I + 1.703*Q
                
                if R >= 256:
                    R=255 
                if G >= 256:
                    G=255
                if B >= 256:
                    B=255
                if R <= 0:
                    R=0 
                if G <= 0:
                    G=0
                if B <= 0:
                    B=0
                
                value = (round(R),round(G),round(B))
                out2.putpixel((x, y), value)
        
    out2.save('q1Test/new2.jpg')
    print("Done!")


RGBtoYIQ()
YIQtoRGB()

#-----------------Visualização das imagens-----------------------#

filename = ['q1Test/Detran_Minas-Gerais.jpg', 'q1Test/new.jpg', 'q1Test/new2.jpg']
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

plt.show() #inicia o loop pra abertura da janela

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