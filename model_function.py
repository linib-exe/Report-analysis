import joblib

def model(data):
    # Load the model back
    loaded_rf_classifier = joblib.load('random_forest_model.pkl')
    loaded_label_encoder = joblib.load('label_encoder.pkl')
    # Predict using the loaded model
    y_pred = loaded_rf_classifier.predict(data)
    return loaded_label_encoder.inverse_transform(y_pred)[0]