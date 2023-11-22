#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[2]:


def BINRRY_THRSHOLD(img,threshold_val):
    
    binary_img=np.zeros_like(img)
    
    rows,cols=np.shape(img)
    
    for row in range (rows):
        for col in range (cols):
            if(img[row,col]>threshold_val):
                binary_img[row,col]=255
            else:
                binary_img[row,col]=0
    return binary_img
                
                
    
    


# In[5]:


img=cv2.imread("gradient.jpg",0)
threshold_val=128


# In[6]:


binary_img= BINRRY_THRSHOLD(img,threshold_val)


# In[16]:


titles=["ORIGINAL IMAGE","BINARY THRESHOLD IMAGE"]
images=[img,binary_img]


for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])


# In[ ]:




