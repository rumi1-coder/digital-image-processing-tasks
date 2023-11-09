print("question4 assignment1 dip by 18i0728")
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
 
# Read Images
img = mpimg.imread('test2.jpg')
 


def FlipImg(img_para,flag=0):
    height_img, width_img = img_para.shape[0:2]
    
    counter1=0
    for item in img[0][0]:
       # Incrementing counter variable to get each item in the list
       counter1 = counter1 + 1
   
    channels_img=counter1
    print("here")
    d3 = [[[0 for col in range(3)]for row in range(width_img)] for x in range(height_img)] 
    if(flag==0):
          
       print(len(d3[0]))
       #print(iflip)
       i=0
       while i < height_img:
           j=0
           iflp=width_img-1
           while j<width_img:
               k=0
               while k<3:
                   d3[i][iflp][k]=img_para[i][j][k]
                   k+=1
               j+=1
               iflp-=1
           i+=1
    else:
           
          
        i=0
        iflp=height_img-1
        while i < height_img:
             j=0
             while j<width_img:
                 k=0
                 while k<3:
                     d3[iflp][j][k]=img_para[i][j][k]
                     k+=1
                 j+=1
                 
             i+=1
             iflp-=1
        
        
            
    arr = np.array(d3)
    imgplot = plt.imshow(arr)
    plt.show()
    imgplot = plt.imshow(img)
    plt.show()
    
    print('here')
    """ i = 0
       while i < height_img:
            j=0
            iflip=width_img-1
            while j < width_img:
                k=0
                while k < channels_img:
                      d3[i][iflip][k]=img_para[i][j][k]
                      k+=1            
                j+=1
                iflip-=1
                #print(iflip)
            i+=1
    print('here')
   
    arr = np.array(d3)
    plt.imshow(arr)
    """
           
     
    
# Load an color image in grayscale
FlipImg(img,0)

