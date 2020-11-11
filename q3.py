import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import time 
import numpy as np
from scipy import signal

def Correlation(img,linhas,colunas,flag):
    height = img.shape[0]
    width = img.shape[1]
    mask = np.zeros((linhas,colunas))
    h,w = mask.shape
    if(flag == 1):
        a = h //2
        c = w //2
    else:
        a = h
        c = w
    # garantia que a mascara percorra sem passar pelas extremidades
    img_corr = np.zeros(img.shape, 'uint8')
    for i in range(linhas):
        for t in range(colunas):
            mask[i][t] = 1/25
    init = time.time()
    for i in range(a, height - a):
        for j in range(c, width - c):
            sumR = 0
            sumG = 0
            sumB = 0
            for m in range(h):
                for n in range(w):
                    sumR += np.multiply(mask[m, n], img[i-h+m, j-w+n, 0])
                    sumG += np.multiply(mask[m, n], img[i-h+m, j-w+n, 1])
                    sumB += np.multiply(mask[m, n], img[i-h+m, j-w+n, 2])
            
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
            img_corr[i, j, 0] = sumR
            img_corr[i, j, 1] = sumG
            img_corr[i, j, 2] = sumB

    fim = time.time()
    print(fim-init)
    return img_corr



linhas = 25
colunas = 25
img = Image.open("q3Test/slides.png")
img = np.array(img)
teste = Correlation(img , linhas,colunas,1)
output = Image.fromarray(teste)
output.save('teste.png')
output.show()