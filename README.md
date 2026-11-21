# FAQ Chatbot

## Project Description
The FAQ Chatbot is a simple web-based application developed using Python and Flask. It interacts with users and provides answers to frequently asked questions through a chat interface.

## Technologies Used
- Python
- Flask
- HTML
- CSS
- JavaScript

## Features
- Interactive chatbot interface
- Answers frequently asked questions
- Predefined question and answer database
- Instant responses to user messages
- Enter key support for sending messages
- User-friendly design
- Handles unknown questions with a default response

## Project Structure
```text
FAQ_Chatbot/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── README.md
```

## How to Run the Project

1. Install Python on your system.
2. Install Flask using:

```bash
python -m pip install flask
```

3. Open the project folder in VS Code.
4. Run the application:

```bash
python app.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Sample Questions
- Hello
- What is FAQ?
- What is Python?
- What is Flask?
- What is Machine Learning?
- What is a chatbot?

## Working
The user enters a question in the chatbot interface. JavaScript sends the question to the Flask backend. Flask checks the predefined FAQ database and returns the matching answer. The chatbot displays the response on the screen.

## Future Enhancements
- Add more frequently asked questions.
- Integrate AI-based responses.
- Add voice input and output.
- Improve natural language understanding.

## Author
Developed as part of the CodeAlpha Artificial Intelligence Internship.
