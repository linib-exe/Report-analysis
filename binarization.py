import cv2
import matplotlib.pyplot as plt

# Load the color image
image_path = 'lipid_profile/lipid1.png'
img = cv2.imread(image_path)

# Check if the image was loaded properly
if img is None:
    print("Error: Could not load image.")
else:
    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply global thresholding
    _, binary_img_global = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

    # Apply adaptive thresholding
    binary_img_adaptive = cv2.adaptiveThreshold(gray_img, 255, 
                                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                cv2.THRESH_BINARY, 11, 2)

    # Apply Otsu's thresholding
    _, binary_img_otsu = cv2.threshold(gray_img, 0, 255, 
                                        cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Set up the figure for plotting
    plt.figure(figsize=(12, 10))

    # Original Image
    plt.subplot(2, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
    plt.title('Original Image')
    plt.axis('off')  # Hide axes

    # Grayscale Image
    plt.subplot(2, 3, 2)
    plt.imshow(gray_img, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')  # Hide axes

    # Global Binary Image
    plt.subplot(2, 3, 3)
    plt.imshow(binary_img_global, cmap='gray')
    plt.title('Global Binary Image')
    plt.axis('off')  # Hide axes

    # Adaptive Binary Image
    plt.subplot(2, 3, 4)
    plt.imshow(binary_img_adaptive, cmap='gray')
    plt.title('Adaptive Binary Image')
    plt.axis('off')  # Hide axes

    # Otsu Binary Image
    plt.subplot(2, 3, 5)
    plt.imshow(binary_img_otsu, cmap='gray')
    plt.title("Otsu's Binary Image")
    plt.axis('off')  # Hide axes

    # Show the plot
    plt.tight_layout()
    plt.show()
