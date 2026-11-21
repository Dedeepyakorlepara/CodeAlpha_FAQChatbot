
from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

faqs = {
    "what is your name": "I am an FAQ Chatbot.",
    "what is faq": "FAQ stands for Frequently Asked Questions.",
    "what are your working hours": "Our working hours are 9 AM to 5 PM.",
    "how can i contact you": "You can contact us through email.",
    "where are you located": "We are located in India.",
    "what services do you provide": "We provide customer support and information services.",
    "how can i register": "You can register by filling out the registration form.",
    "thank you": "You're welcome! Happy to help.",
    "hello": "Hello! How can I help you today?",
    "hi": "Hi! Welcome. Ask me anything.",
    "what is artificial intelligence": "Artificial Intelligence allows machines to perform tasks that normally require human intelligence.",
    "what is machine learning": "Machine Learning helps computers learn from data.",
    "what is python": "Python is a popular programming language.",
    "what is flask": "Flask is a lightweight Python web framework.",
    "what is chatbot": "A chatbot is a software application that communicates with users.",
    "how can i get support": "You can contact our support team through email.",
    "is registration free": "Yes, registration is free.",
    "can i use this chatbot anytime": "You can use this chatbot whenever the application is running.",
    "what is your purpose": "My purpose is to answer frequently asked questions.",
    "good morning": "Good morning! How can I help you?"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_message = request.json["message"].lower().strip()
    clean_message = re.sub(r"[^a-z0-9\s]", "", user_message)

    answer = "Sorry, I don't know the answer. Please try another question."

    for question, reply in faqs.items():
        if question == clean_message:
            answer = reply
            break

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
