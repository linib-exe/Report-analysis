from django.shortcuts import render
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np
from ocr_function import Lipid_Profile,Rft

# Create your views here.
def home(request):
    if request.method == 'POST':
        image = request.FILES.get('image')

        # Convert the image to a format OpenCV can handle
        img = Image.open(image)
        img = np.array(img)

        test = request.POST.get('report_type')

        if test == 'lipid_profile':
            # Call the Lipid_Profile function with the grayscale image
            Lipid_Profile(img)

        elif test == 'rft':
            Rft(img)


        
    return render(request, 'index.html')

