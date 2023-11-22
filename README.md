# Image-Processing-Segmentation-Global-Threshold-filters-

IN GLOBAL THRESHOLD
There are 5 techniques
    **1)Binary threshold
    2) Inverse binary threshold
    3)Trunk threshold
    4)To Zero threshold
    5)Inverse To Zero threshold**


**THRESH_BINARY: If the pixel is greater than the threshold, the value is set to 255 (white), else set to 0 (black).
THRESH_BINARY_INV: If the pixel is greater than the threshold, the value is set to 0 (black), else set to 255 (white).
THRESH_TRUNC: If the pixel is greater than the threshold, the value is set to the threshold, All other values remain the same.
THRESH_TOZERO:  If the pixel is less than the threshold, the value is set to 0 (black), All other values remain the same.
THRESH_TOZERO_INV:  If the pixel is greater than the threshold, the value is set to 255 (white), All other values remain the same.**


Built-in Syntax
threshold(source, threshold value, maxVal, thresholding technique) 
-> source: Input Image array (must be in Grayscale). 
-> thresholdValue: Value of Threshold below and above which pixel values will change accordingly.
-> maximal: Maximum value that can be assigned to a pixel.
-> thresholding technique: The type of thresholding to be applied. 
->mentioned above 



"Don't Forget to rename the image  (Used image) to (gradient)"

Best wishes




