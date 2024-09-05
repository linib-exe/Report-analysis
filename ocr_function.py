import pytesseract
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import pandas as pd
from binarization_function import binarization
from model_function import model

def Lipid_Profile(img):
    recognized_headings = []
    recognized_investigations = []
    first_column = []
    second_column = []
    third_column = []
    forth_column = []
    test = ''
    tests = ['lipidprofile']
    headings = ['investigation', 'result', 'referencevalue', 'unit']
    investigations = ['cholesteroltotal', 'triglycerides', 'hdlcholesterol', 'ldlcholesterol', 'vldlcholesterol', 'non-hdlcholesterol']
    outliers = ['sampletype', 'spectraphotometry', 'calculated', 'tat:1day(normal:1-3days)', 'normal', 'calculated', 'serum(2ml)', 'spectrophotometry', 'high', 'veryhigh','spectrophatometry']


    # Binarize the image (Otsu and Adaptive)
    binary_img_otsu, binary_img_adaptive = binarization(img)

    # Convert the adaptive thresholded image to RGB for OCR (if needed)
    img_rgb = cv2.cvtColor(binary_img_otsu, cv2.COLOR_GRAY2RGB)

    # Perform OCR
    text = pytesseract.image_to_string(img_rgb)
    text_cleaned = text.replace(" ", "").replace("\n", " ").lower()
    words_list = text_cleaned.split()

    for i in words_list:
        if i in tests:
            test = i

    for i in words_list:
        if i != 'result':
            if i in investigations:
                first_column.append(i)
        else:
            break

    for i in words_list:
        if i!='referencevalue':
            if i not in first_column:
                if i not in headings:
                    if i not in outliers:
                        if i not in tests:
                            second_column.append(i)
        else:
            break

    for i in words_list:
        if i!='unit':
            if i not in first_column:
                if i not in second_column:
                    if i not in headings:
                        if i not in outliers:
                            if i not in tests:
                                third_column.append(i)
        else:
            break

    for i in words_list:
        if i not in headings:
            if i not in outliers:
                if i not in first_column:
                    if i not in second_column:
                        if i not in third_column:
                            if i not in tests:
                                forth_column.append(i)

    for i in words_list:
        if i in headings:
            recognized_headings.append(i)
        
    for i in words_list:
        if i in investigations:
            recognized_investigations.append(i)

    column_values = [first_column,second_column,third_column,forth_column]
    data = {headings[i]: pd.Series(column_values[i]) for i in range(len(headings))}
    df = pd.DataFrame(data)
    column_values_np = df['result'].values
    prediction = model(column_values_np.reshape(1, -1))
    df.to_csv('data.csv', index=False)

    print(f"Words List: {words_list}")
    print(f"Headings: {recognized_headings}")
    print(f"{recognized_headings[0]}: {first_column}")
    print(f"{recognized_headings[1]}: {second_column}")
    print(f"{recognized_headings[2]}: {third_column}")
    print(f"{recognized_headings[3]}: {forth_column}")
    print(f"Test:{test}")
    print(f"Result:{prediction}")


def Rft(img):
    recognized_headings = []
    recognized_investigations = []
    first_column = []
    second_column = []
    third_column = []
    forth_column = []
    test = ''
    tests = ['kidneyfunctiontest(kft)']
    headings = ['investigation', 'result', 'referencevalue', 'unit']
    investigations = ['urea', 'creatinine', 'uricacid', 'calcium,total', 'phosphorus', 'alkalinephosphatase(alp)','totalprotein','albumin','sodium','potassium','chloride']
    outliers = ['primarysampletype:', 'ureaseuv', 'modifiedjaffe,kinetic', 'uricase', 'normal', 'arsenazoill', 'molybdateuv', 'ifcc', 'biuret', 'bcg','indirectise','indirect[se','indirectise','serum']


    # Binarize the image (Otsu and Adaptive)
    binary_img_otsu, binary_img_adaptive = binarization(img)

    # Convert the adaptive thresholded image to RGB for OCR (if needed)
    img_rgb = cv2.cvtColor(binary_img_otsu, cv2.COLOR_GRAY2RGB)

    # Perform OCR
    text = pytesseract.image_to_string(img_rgb)
    text_cleaned = text.replace(" ", "").replace("\n", " ").lower()
    words_list = text_cleaned.split()

    for i in words_list:
        if i in tests:
            test = i

    for i in words_list:
        if i != 'result':
            if i in investigations:
                first_column.append(i)
        else:
            break

    for i in words_list:
        if i!='referencevalue':
            if i not in first_column:
                if i not in headings:
                    if i not in outliers:
                        if i not in tests:
                            second_column.append(i)
        else:
            break

    for i in words_list:
        if i!='unit':
            if i not in first_column:
                if i not in second_column:
                    if i not in headings:
                        if i not in outliers:
                            if i not in tests:
                                third_column.append(i)
        else:
            break

    for i in words_list:
        if i not in headings:
            if i not in outliers:
                if i not in first_column:
                    if i not in second_column:
                        if i not in third_column:
                            if i not in tests:
                                forth_column.append(i)

    for i in words_list:
        if i in headings:
            recognized_headings.append(i)
        
    for i in words_list:
        if i in investigations:
            recognized_investigations.append(i)

    column_values = [first_column,second_column,third_column,forth_column]
    data = {headings[i]: pd.Series(column_values[i]) for i in range(len(headings))}
    df = pd.DataFrame(data)
    prediction = model(df)
    df.to_csv('data.csv', index=False)

    print(f"Words List: {words_list}")
    print(f"Headings: {recognized_headings}")
    print(f"{recognized_headings[0]}: {first_column}")
    print(f"{recognized_headings[1]}: {second_column}")
    print(f"{recognized_headings[2]}: {third_column}")
    print(f"{recognized_headings[3]}: {forth_column}")
    print(f"Test:{test}")
    print(f"Result:{prediction}")


