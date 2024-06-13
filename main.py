import os
import cohere
from flask import Flask, render_template, send_file

co = cohere.Client("Rx2DD4J8sBxsrhsoUPrNbVulsqWPlrQxbAntYvCL")

app = Flask(__name__, template_folder='src')

@app.route("/")
def index():
    response = co.chat(
        chat_history=[
            {"role": "USER", "message": "Who discovered gravity?"},
            {
                "role": "CHATBOT",
                "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton",
            },
        ],
        message="What year was he born?",
        connectors=[{"id": "web-search"}],
    )

    # Convert response to JSON string
    response_json = response.json()
    # return send_file('src/index.html')

    return render_template('index.html', response=response_json)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
