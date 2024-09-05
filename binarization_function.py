import cv2

def binarization(img):
    if img is None:
        raise ValueError("Error: Could not load image.")
    else:
        # Convert the image to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply Otsu's thresholding
        _, binary_img_otsu = cv2.threshold(gray_img, 0, 255, 
                                            cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # Apply adaptive thresholding
        binary_img_adaptive = cv2.adaptiveThreshold(gray_img, 255, 
                                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                    cv2.THRESH_BINARY, 11, 2)
        
        return binary_img_otsu, binary_img_adaptive



