#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


img=cv2.imread("gradient.jpg")


# In[38]:


# cv2.threshold(source, thresholdValue, maxVal, thresholdingTechnique) 
# cv2.THRESH_BINARY: If pixel intensity is greater than the set threshold, value set to 255, else set to 0 (black).
# cv2.THRESH_BINARY_INV: Inverted or Opposite case of cv2.THRESH_BINARY.
# cv.THRESH_TRUNC: If pixel intensity value is greater than threshold, it is truncated to the threshold. All other values remain the same.
# cv.THRESH_TOZERO: Pixel intensity is set to 0, for all the pixels intensity, less than the threshold value.
# cv.THRESH_TOZERO_INV: Inverted or Opposite case of cv2.THRESH_TOZERO.


ret,thresh1=cv2.threshold(img,127,np.max(img),cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(img,127,np.max(img),cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(img,127,np.max(img),cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(img,127,np.max(img),cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(img,127,np.max(img),cv2.THRESH_TOZERO_INV)


# In[43]:


# np.max(img)


# In[39]:


titels=['original image', "BINARY","INV BINARY ","TRUNK ","TO ZERO ","INV TO ZERO "]


# In[40]:


images=[img,thresh1,thresh2,thresh3,thresh4,thresh5]


# In[41]:


len(images)


# In[45]:


for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titels[i])



# In[ ]:




