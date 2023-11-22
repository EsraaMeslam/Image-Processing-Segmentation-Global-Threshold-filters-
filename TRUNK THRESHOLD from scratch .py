#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[11]:


def TRUNK_THRSHOLD(img,threshold_val):
    
    trunk_img=np.zeros_like(img)
    
    rows,cols=np.shape(img)
    
    for row in range (rows):
        for col in range (cols):
            if(img[row,col]>threshold_val):
                trunk_img[row,col]=threshold_val
            else:
                trunk_img[row,col]=img[row,col]
                

    return trunk_img


# In[12]:


img=cv2.imread("gradient.jpg",0)
threshold_val=128


# In[13]:


trunk_img= TRUNK_THRSHOLD(img,threshold_val)


# In[14]:


titles=["ORIGINAL IMAGE","TRUNK THRESHOLD IMAGE "]
images=[img,trunk_img]


for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])


# In[ ]:




