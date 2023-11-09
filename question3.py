print("question3 assignment1 dip by 18i0728")

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
img1 = mpimg.imread('rect7.jpg')
img2 = mpimg.imread('rect1.jpg')


def StackHorizontal(img1_para,img2_para):
    height_img1, width_img1 = img1_para.shape[0:2]
    height_img2, width_img2 = img2_para.shape[0:2]
    counter1=0
    for item in img1[0][0]:
       # Incrementing counter variable to get each item in the list
       counter1 = counter1 + 1
    counter2=0
    for item in img2[0][0]:
        # Incrementing counter variable to get each item in the list
         counter2 = counter2 + 1
    print(counter1)
    print(counter2)
    channels_img1=counter1
    channels_img2=counter2
    if (height_img1==height_img2) and (width_img1==width_img2):
        print("size of both images matched\n   now checking the channels info of both images")
        if(channels_img1==channels_img2):
           print("\nchannels matched !!images are compatible for horizontal stacking")
           
           d3 = [[[0 for col in range(3)]for row in range(width_img1*2)] for x in range(height_img1)]
           
           i = 0
           while i < height_img1:
               j=0
               z=0
               while j < width_img1*2:
                    if(j<width_img1):
                       k=0
                       while k < channels_img1:
                          d3[i][j][k]=img1_para[i][j][k]
                          k+=1            
                    else:      
                        k=0
                        while k < channels_img1:
                          d3[i][j][k]=img2_para[i][z][k]
                          k+=1
                        z+=1
                        
                    j+=1
                    
                    
               i+=1
   
           arr = np.array(d3)
           imgplot = plt.imshow(arr)
           plt.show()
    
           
        else:
            print("channels didnot matched\nhence images are not compatible for stacking")
    else:
        print("images are not compatible for horizantle stacking")
    
# Load an color image in grayscale
StackHorizontal(img1,img2)

