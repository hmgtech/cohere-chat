import os
import cohere
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Cohere client with API key from environment variable
co = cohere.Client("Rx2DD4J8sBxsrhsoUPrNbVulsqWPlrQxbAntYvCL")

app = Flask(__name__, template_folder='src')

# Initial chat history
initial_chat_history = [
    {"role": "USER", "message": "Who discovered gravity?"},
    {"role": "CHATBOT", "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton"},
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_message = request.form["user-input"]

        # Add user's message to chat history
        initial_chat_history.append({"role": "USER", "message": user_message})

        # Call Cohere API to get response
        response = co.chat(
            chat_history=initial_chat_history,
            message=user_message,
            connectors=[{"id": "web-search"}],
        )

        # Add bot's response to chat history
        initial_chat_history.append({"role": "CHATBOT", "message": response["message"]})

    return render_template('index.html', messages=initial_chat_history)

def main():
    # Get port from environment variable or use default 80
    port = int(os.getenv("PORT", 80))
    app.run(port=port)

if __name__ == "__main__":
    main()
