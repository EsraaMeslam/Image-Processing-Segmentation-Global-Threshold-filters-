# Image-Processing-Segmentation-Global-Threshold-filters-

IN GLOBAL THRESHOULD
There is 5 techinques
1)Binary threshold
2)inverse Binary thershould
3)Trunk thershould
4)To Zero thershould
5)Inverse To Zero thershould


THRESH_BINARY: If pixel intensity is greater than the set threshold, value set to 255, else set to 0 (black).
THRESH_BINARY_INV: Inverted or Opposite case of cv2.THRESH_BINARY.
THRESH_TRUNC: If pixel intensity value is greater than threshold, it is truncated to the threshold. All other values remain the same.
THRESH_TOZERO: Pixel intensity is set to 0, for all the pixels intensity, less than the threshold value.
THRESH_TOZERO_INV: Inverted or Opposite case of cv2.THRESH_TOZERO.


Built in Syntax
threshold(source, thresholdValue, maxVal, thresholdingTechnique) 
-> source: Input Image array (must be in Grayscale). 
-> thresholdValue: Value of Threshold below and above which pixel values will change accordingly.
-> maxVal: Maximum value that can be assigned to a pixel. -> thresholdingTechnique: The type of thresholding to be applied. 
->mentioned above 



"Don't Forget to rename the image  (Used image) to (gradient)"

Best wishes




