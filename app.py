import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Render ke Dashboard mein 'GEMINI_API_KEY' set karna
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    response = model.generate_content(user_message)
    return jsonify({"reply": response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
