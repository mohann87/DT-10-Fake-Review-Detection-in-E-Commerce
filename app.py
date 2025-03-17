from flask import Flask, render_template, request, jsonify
import joblib  # For loading a trained ML model (if you have one)
import re
import string

app = Flask(__name__)

# Load a trained model (Replace 'fake_review_model.pkl' with your actual model file)
try:
    model = joblib.load("fake_review_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")  # Ensure your vectorizer is also saved
except:
    model = None
    vectorizer = None

# Function to preprocess text
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = text.strip()
    return text

@app.route("/")
def home():
    return render_template("index.html")  # Ensure index.html exists in "templates" folder

@app.route("/predict", methods=["POST"])
def predict():
    review = request.form["review"]
    processed_review = preprocess_text(review)

    if model and vectorizer:
        review_vectorized = vectorizer.transform([processed_review])  # Convert text to features
        prediction = model.predict(review_vectorized)[0]  # Predict fake or real
        result = "Fake Review" if prediction == 1 else "Real Review"
    else:
        result = "Model not loaded. Please train and load a model."

    return render_template("index.html", review=review, result=result)

if __name__ == "__main__":
    app.run(debug=True)
