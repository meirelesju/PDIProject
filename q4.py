import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import time 
import numpy as np
from scipy import signal

def Correlation(img,linhas,colunas):
    height = img.shape[0]
    width = img.shape[1]
    mask = np.zeros((linhas,colunas))

    h,w = mask.shape
    
    a = h //2
    c = w //2
    
    newR = np.zeros((height+(2*a), width+(2*c)))
    newG = np.zeros((height+(2*a), width+(2*c)))
    newB = np.zeros((height+(2*a), width+(2*c)))
    
    for i in range(height):
        for j in range(width):
            if(i<height and j < width ):
                newR[i +a][j+c] = img[i,j,0]
                
                newG[i +a][j+c] = img[i,j,1]  
                newB[i +a][j+c] = img[i,j,2]     
    # garantia que a mascara percorra sem passar pelas extremidades
    
    img_corr = np.zeros(img.shape, 'uint8')
    for i in range(h):
        for t in range(w):
            mask[i][t] = 1/(colunas * linhas)
    init = time.time()
    for i in range(a, height + a):
        for j in range(c, width + c):
            sumR = 0
            sumG = 0
            sumB = 0
            if(c <= width and a <= height ):
                # Tive que fazer essa separação pois na hora de passar o filtro quando linhas ou colunas forem 1 não vai haver deslocamento horizontal ou vertical na mascara
            
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
    
    print("A matriz de ",linhas, "linhas e ",colunas,"colunas foi executada em:",fim - init)
    return img_corr


#Abertura da Imagem
img = Image.open("q4Test/slides.png")
img = np.array(img)



img1 = Correlation(img,1,25)
output = Image.fromarray(img1)
output.save('q4Test/1x25.png')

img2 = Correlation(img,25,1)
output = Image.fromarray(img2)
output.save('q4Test/25x1.png')

img3 = Correlation(img,25,25)
output = Image.fromarray(img3)
output.save('q4Test/25x25.png')


