import pytesseract
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import pandas as pd

image_path = 'test.png'
img = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
image = Image.open(image_path)
text = pytesseract.image_to_string(image)
text_cleaned =  text.replace(" ", "").replace("\n", " ").lower()
words_list = text_cleaned.split()

headings = ['investigation','result','referencevalue','unit']
investigations = ['chloride','proteins','sugar','colour','quantity','appearance','coagulum','blood']
outliers = ['chemicalexamination','physicalexamination']

recognized_headings = []
recognized_investigations = []
first_column = []
second_column = []
third_column = []
forth_column = []

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
                    second_column.append(i)
    else:
        break

for i in words_list:
    if i!='unit':
        if i not in first_column:
            if i not in second_column:
                if i not in headings:
                    if i not in outliers:
                        third_column.append(i)
    else:
        break

for i in words_list:
    if i not in headings:
        if i not in outliers:
            if i not in first_column:
                if i not in second_column:
                    if i not in third_column:
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
df.to_csv('data.csv', index=False)

print(f"Words List: {words_list}")
print(f"Recognized Headings: {recognized_headings}")
print(f"Recognized Investigations: {recognized_investigations}")
print(f"First Column: {first_column}")
print(f"Second Column: {second_column}")
print(f"Third Column: {third_column}")
print(f"Forth Column: {forth_column}")

