from flask import Flask, render_template, request
import re

app = Flask(__name__)

def is_fake_review(review):
    fake_keywords = ["free", "guaranteed", "best", "amazing", "exclusive", "winner"]
    for word in fake_keywords:
        if re.search(rf"\b{word}\b", review, re.IGNORECASE):
            return True
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        review = request.form['review']
        result = "Fake Review Detected!" if is_fake_review(review) else "Review Seems Genuine."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
