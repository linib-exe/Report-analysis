import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv('lipid_inference_data.csv')
df.drop(columns=['inference','test'],inplace=True)

# Convert the 'classification' column to numerical values
label_encoder = LabelEncoder()
df['classification_encoded'] = label_encoder.fit_transform(df['classification'])

# Select the features (excluding 'test' and 'inference' columns)
features = df[['cholesteroltotal', 'triglycerides', 'hdlcholesterol', 'ldlcholesterol', 'vldlcholesterol', 'non-hdlcholesterol']]
target = df['classification_encoded']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

# Initialize the Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
# Train the model
rf_classifier.fit(X_train, y_train)

# Dump the trained model to a file
joblib.dump(rf_classifier, 'random_forest_model.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')
