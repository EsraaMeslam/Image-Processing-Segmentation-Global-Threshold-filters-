#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[6]:


def INV_BINRRY_THRSHOLD(img,threshold_val):
    
    inv_binary_img=np.zeros_like(img)
    
    rows,cols=np.shape(img)
    
    for row in range (rows):
        for col in range (cols):
            if(img[row,col]>threshold_val):
                inv_binary_img[row,col]=0
            else:
                inv_binary_img[row,col]=255
    return inv_binary_img
                


# In[7]:


img=cv2.imread("gradient.jpg",0)
threshold_val=128


# In[8]:


inv_binary_img= INV_BINRRY_THRSHOLD(img,threshold_val)


# In[9]:


titles=["ORIGINAL IMAGE","INV BINARY THRESHOLD "]
images=[img,inv_binary_img]


for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])


# In[ ]:




