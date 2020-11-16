import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import time 
import numpy as np
from scipy import signal

def Matriz(linhas,colunas,flag):
    if(flag == 1):
    
    #define linhas e colunas da mascara
        linhas = 15
        colunas = 15
        mask = np.zeros((linhas,colunas))
        for i in range(colunas):
            for t in range(linhas):
                mask[i][t] = 1/(linhas*colunas)
    else:
        mask = np.array([[-1,-2,-1],
                         [0,0,0],
                         [1,2,1]])
    

    return mask

def Correlation(img,a,c,mask):
    img_corr = np.zeros(img.shape, 'uint8')
    height = img.shape[0]
    width = img.shape[1]
    h,w = mask.shape
    init = time.time()
    for i in range(a, height + a):
        for j in range(c, width + c):
            sumR = 0
            sumG = 0
            sumB = 0
            if(c <= width and a <= height ):
                if(a!=0 and c !=0):
                    for m in range(h):
                        for n in range(w):
                            sumR += np.multiply(mask[m, n], newR[i+m-a, j-c+n])
                            sumG += np.multiply(mask[m, n], newG[i-a+m, j-c+n])
                            sumB += np.multiply(mask[m, n], newB[i-a+m, j-c+n])
                elif (a == 0):
                    for m in range(h):
                        for n in range(w):
                            sumR += np.multiply(mask[m, n], newR[i, j-c+n])
                            sumG += np.multiply(mask[m, n], newG[i, j-c+n])
                            sumB += np.multiply(mask[m, n], newB[i, j-c+n])
                elif (c == 0):
                    for m in range(h):
                        for n in range(w):
                            sumR += np.multiply(mask[m, n], newR[i+m-a, j])
                            sumG += np.multiply(mask[m, n], newG[i-a+m, j])
                            sumB += np.multiply(mask[m, n], newB[i-a+m, j])
                
                if sumR < 0:
                    sumR = -sumR
                elif sumR > 255:
                    sumR = 255
                if sumG < 0:
                    sumG = -sumG
                elif sumG > 255:
                    sumG = 255
                if sumB < 0:
                    sumB = -sumB
                elif sumB > 255:
                    sumB = 255
                
            img_corr[i - a, j - c, 0] = sumR
            img_corr[i - a , j - c, 1] = sumG
            img_corr[i - a, j - c, 2] = sumB
    
    fim = time.time()
    print(fim-init)
    return img_corr




#abertura da imagem
img = Image.open("q3Test/slides.png")
img = np.array(img)

#altura e largura da imagem
height = img.shape[0]
width = img.shape[1]


mask = Matriz(15,15,1) 
    
h,w = mask.shape

a = h //2
c = w//2


#Quando se faz a extensão por zero é preciso adicionar exatemente a metade da altura e da largura arredondado
# para baixo a matriz original    
newR = np.zeros((height+(2*a), width+(2*c)))
newG = np.zeros((height+(2*a), width+(2*c)))
newB = np.zeros((height+(2*a), width+(2*c)))




#preenchimento das novas matrizes RGB
for i in range(height):
    for j in range(width):
        if(i<height and j < width ):
            newR[i +a][j+c] = img[i,j,0]
                
            newG[i +a][j+c] = img[i,j,1]  
            newB[i +a][j+c] = img[i,j,2]     
    # garantia que a mascara percorra sem passar pelas extremidades
#preenchimento do filtro media




teste = Correlation(img,a,c,mask)


output = Image.fromarray(teste)
flag = 1
if(flag == 1):
    output.save('q3Test/media.png')
else:
    output.save('q3Test/sobel.png')
output.show()