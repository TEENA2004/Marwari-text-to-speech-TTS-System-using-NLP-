import pickle

model = {
    "नमस्ते": "राम राम",
    "आप कैसे हैं?": "तूं के करै सै?",
    "धन्यवाद": "बधाई हो",
    "बुखार आने पर क्या करें?": "बखर आन् पर कय करं?"
}

with open("translation_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model updated ✅")
