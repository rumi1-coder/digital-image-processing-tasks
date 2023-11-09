
print("question5 assignment1 Dip by 18i0728")
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
img1 = mpimg.imread('rect1.jpg')
img2 = mpimg.imread('rect7.jpg')
def CommonImg(img_para1,img_para2):
    height1, width1 = img_para1.shape[0:2]
    height2, width2 = img_para2.shape[0:2]
    if(height1*width1 >= height2*width2):
       d3 = [[[0 for col in range(3)]for row in range(width1)] for x in range(height1)] 
       i=0
       while i<height1:
           j=0
           while j<width1:
                  if i<=height2 and j<=width2:
                      if (img_para1[i][j][0]==img_para2[i][j][0])and(img_para1[i][j][1]==img_para2[i][j][1])and(img_para1[i][j][2]==img_para2[i][j][2]):
                          d3[i][j][0]=img_para1[i][j][0]
                          d3[i][j][1]=img_para1[i][j][1]
                          d3[i][j][2]=img_para1[i][j][2]
                      else:
                          d3[i][j][0]=0
                          d3[i][j][1]=0
                          d3[i][j][1]=0
                  else:
                          d3[i][j][0]=0
                          d3[i][j][1]=0
                          d3[i][j][1]=0
                  j+=1
           i+=1
                         
               
    else:
         d3 = [[[0 for col in range(3)]for row in range(width2)] for x in range(height2)] 
         i=0
         while i<height1:
           j=0
           while j<width1:
                  if i<=height2 and j<=width2:
                      if (img_para1[i][j][0]==img_para2[i][j][1])and(img_para1[i][j][1]==img_para2[i][j][1])and(img_para1[i][j][2]==img_para2[i][j][2]):
                          d3[i][j][0]=img_para1[i][j][0]
                          d3[i][j][1]=img_para1[i][j][1]
                          d3[i][j][2]=img_para1[i][j][2]
                      else:
                          d3[i][j][0]=0
                          d3[i][j][1]=0
                          d3[i][j][1]=0
                  else:
                          d3[i][j][0]=0
                          d3[i][j][1]=0
                          d3[i][j][1]=0
                  j+=1
           i+=1
        
    arr = np.array(d3)
    imgplot = plt.imshow(arr)
    plt.show()
    

img = mpimg.imread('test.png')
CommonImg(img1,img2)


