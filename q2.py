import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

def Negative():
    img = Image.open("q2Test/slides.png")
    width, height = img.size
    out = Image.new('RGB', img.size)

    print("Convertendo para negativo")
    for x in range(width):
        for y in range(height):
            [R,G,B] = img.getpixel((x,y))
            
            Rpixel  = 255 - R
            Gpixel  = 255 - G
            Bpixel  = 255 - B
            
            out.putpixel((x,y),(Rpixel, Gpixel, Bpixel))
    
    out.save('q2Test/negative.png')
    print("Done!")

Negative()

#-----------------Visualização das imagens-----------------------#

filename = ['q2Test/slides.png', 'q2Test/negative.png']
titles = ['Original', 'Negativa']
fig=plt.figure(figsize=(8, 8))
columns = 2
rows = 1
ax=[]

for i in range(columns*rows):
    img = mpimg.imread(filename[i])
    ax.append(fig.add_subplot(rows, columns, i+1))
    ax[-1].set_title(titles[i])
    plt.imshow(img)
    plt.axis('off')

plt.show()

