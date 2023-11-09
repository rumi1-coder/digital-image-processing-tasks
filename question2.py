
print("question2 assignment1 Dip by 18i0728")
def ConvertToGray(img_para):
    R, G, B = img_para[:,:,0], img_para[:,:,1], img_para[:,:,2]
    imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
    plt.imshow(imgGray, cmap='gray')
    plt.show()
    
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('test.png')
ConvertToGray(img)


