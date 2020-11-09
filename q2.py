import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

def Negative():
    img = Image.open("q2Test/slides.png") #abre a imagem p/ leitura
    width, height = img.size #retorna uma tupla com a altura e largura da imagem e seta os valores nas variaveis
    out = Image.new('RGB', img.size) #cria o arquivo que vai salvar a imagem convertida 

    print("Convertendo para negativo")
    for x in range(width):
        for y in range(height):
            [R,G,B] = img.getpixel((x,y)) #pega os valores rgb do pixel indicado e seta nas variáveis
            
            Rpixel  = 255 - R
            Gpixel  = 255 - G
            Bpixel  = 255 - B
            
            out.putpixel((x,y),(Rpixel, Gpixel, Bpixel)) #coloca os novos valores dos pixels no arquivo que foi criado p/ salvar a imagem convertida
    
    out.save('q2Test/negative.png')#salva a imagem nova/convertida
    print("Done!")

Negative()

#-----------------Visualização das imagens-----------------------#

filename = ['q2Test/slides.png', 'q2Test/negative.png']
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