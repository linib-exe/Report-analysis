from django.shortcuts import render,redirect
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
            prediction = Lipid_Profile(img)

        elif test == 'rft':
            Rft(img)
        
        # Store the prediction in the session
        request.session['prediction'] = prediction

        return redirect('result')

    return render(request, 'index.html')

def result(request):
    # Retrieve the prediction from the session
    prediction = request.session.get('prediction', 'No prediction found')

    # Pass the prediction to the template
    return render(request, 'resultpage.html', {'prediction': prediction.upper})

