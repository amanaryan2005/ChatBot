from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("API key not found. Please set GOOGLE_API_KEY in .env file.")
    # In a real app, you might want to handle this more gracefully or crash early.

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        if not data or "message" not in data:
             return jsonify({"error": "Message is required"}), 400
        
        user_input = data["message"]
        response = model.generate_content(user_input)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
