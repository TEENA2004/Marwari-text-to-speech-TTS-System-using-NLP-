import pandas as pd
import joblib
import os
import re

# Load translation model
model_path = os.path.join("translation_model", "translation_model.pkl")
model = joblib.load(model_path)

# Function to translate Hindi to Marwari using model dictionary
def translate_input(hindi_text):
    if hindi_text in model:
        return model[hindi_text]
    else:
        return "अनुवाद उपलब्ध नहीं है"

# ✅ Function to clean or preprocess Hindi input
def preprocess_text(text):
    # Lowercase conversion
    text = text.lower()

    # Remove punctuations and special characters
    text = re.sub(r'[^\w\s]', '', text)

    # Remove extra whitespace
    text = text.strip()

    return text

