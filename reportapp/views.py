from django.shortcuts import render, redirect
from PIL import Image
import numpy as np
import base64
from io import BytesIO
from ocr_function import Lipid_Profile, Rft

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
            prediction = Rft(img)

        # Convert the image to RGB if it's in RGBA mode (for JPEG compatibility)
        img_pil = Image.open(image)
        if img_pil.mode == 'RGBA':
            img_pil = img_pil.convert('RGB')

        # Convert the image to base64
        buffered = BytesIO()
        img_pil.save(buffered, format="JPEG")  # Save image to buffer as JPEG
        img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')  # Convert to base64

        # Store the prediction and the base64 image in the session
        request.session['prediction'] = prediction
        request.session['image_base64'] = img_base64

        return redirect('result')

    return render(request, 'index.html')

def result(request):
    # Retrieve the prediction and base64 image from the session
    prediction = request.session.get('prediction', 'No prediction found')
    image_base64 = request.session.get('image_base64', '')

    # Pass the prediction and base64 image to the template
    return render(request, 'resultpage.html', {'prediction': prediction.upper, 'image_base64': image_base64})
