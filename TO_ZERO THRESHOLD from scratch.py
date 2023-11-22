#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[4]:


def TO_ZERO_THRSHOLD(img,threshold_val):
    
    to_zero_img=np.zeros_like(img)
    
    rows,cols=np.shape(img)
    
    for row in range (rows):
        for col in range (cols):
            if(img[row,col]>threshold_val):
                to_zero_img[row,col]=img[row,col]
            else:
                to_zero_img[row,col]=0
    return to_zero_img


# In[5]:


img=cv2.imread("gradient.jpg",0)
threshold_val=128


# In[6]:


to_zero_img= TO_ZERO_THRSHOLD(img,threshold_val)


# In[7]:


titles=["ORIGINAL IMAGE","TO ZERO THRESHOLD "]
images=[img,to_zero_img]


for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])


# In[ ]:




