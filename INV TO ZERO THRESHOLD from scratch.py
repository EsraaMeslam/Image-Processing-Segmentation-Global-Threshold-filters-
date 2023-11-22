#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[2]:


def INV_TO_ZERO_THRSHOLD(img,threshold_val):
    
    inv_to_zero_img=np.zeros_like(img)
    
    rows,cols=np.shape(img)
    
    for row in range (rows):
        for col in range (cols):
            if(img[row,col]>threshold_val):
                inv_to_zero_img[row,col]=0
            else:
                inv_to_zero_img[row,col]=img[row,col]
    return inv_to_zero_img


# In[3]:


img=cv2.imread("gradient.jpg",0)
threshold_val=128


# In[4]:


inv_to_zero_img= INV_TO_ZERO_THRSHOLD(img,threshold_val)


# In[5]:


titles=["ORIGINAL IMAGE","INV TO ZERO THRESHOLD "]
images=[img,inv_to_zero_img]


for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])


# In[ ]:




