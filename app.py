from typing import Dict
from collections import Counter
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_website_content(url: str) -> str:
    response = requests.get(url)
    return response.text

def extract_words(content: str) -> Dict[str, int]:
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()
    words = text.split()
    word_count = Counter(words)
    return dict(word_count)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        content = get_website_content(url)
        word_count = extract_words(content)
        return jsonify(word_count)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
