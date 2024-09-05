import cv2
import matplotlib.pyplot as plt

# Read image
image_path = 'lipid_profile/lipid1.png'
img = cv2.imread(image_path)

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding
binary_img_adaptive = cv2.adaptiveThreshold(gray_img, 255, 
                                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY, 11, 2)

# Apply Otsu's thresholding
_, binary_img_otsu = cv2.threshold(gray_img, 0, 255, 
                                    cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display using Matplotlib
plt.figure(figsize=(20, 10))

# Original
plt.subplot(3, 1, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')  # Hide axes

# Otsu Binarized Image
plt.subplot(3, 1, 2)
plt.title('Otsu Binarized Image')
plt.imshow(binary_img_otsu, cmap='gray')
plt.axis('off')  # Hide axes

#  Adaptive Binarized Image
plt.subplot(3, 1, 3)
plt.title('Adaptive Binarized Image')
plt.imshow(binary_img_adaptive, cmap='gray')
plt.axis('off')  # Hide axes

# Show the plot
plt.show()