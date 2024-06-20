# Chatbot Application using Flask and Cohere

This project is a chatbot application built using Flask and the Cohere API for natural language processing. It provides an interactive chat interface that dynamically displays chat history, making it easy to communicate with the chatbot.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## About

This project is a simple chatbot application designed to demonstrate the integration of Flask with the Cohere API. The application leverages the natural language processing capabilities of the Cohere API to generate responses to user inputs, providing an engaging and interactive chat experience.

**Technologies Used:**
- Flask: A lightweight WSGI web application framework in Python.
- Cohere API: A natural language processing API for generating and understanding text.
- Python: The programming language used for building the application.

## Features

- **Interactive chat interface**: Users can interact with the chatbot through a web-based interface.
- **Integration with Cohere API**: Utilizes the Cohere API for generating natural language responses.
- **Dynamic chat history display**: Chat history is displayed dynamically, providing a seamless chat experience.

## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

Make sure you have the following prerequisites installed:

- Python (version 3.6 or higher)
- Flask
- Cohere
- python-dotenv

### Installation

Step-by-step guide to install and configure the project.

1. **Clone the repository**:
   ```bash
     git clone https://github.com/hmgtech/cohere-chat.git
    ```
2. Navigate to the project directory:

    ```bash
    Copy code
    cd cohere-chat
    ```
3. Install dependencies:
   ```bash
     pip install -r requirements.txt
    ```

4. Create a ```.env``` file in the root directory and add your Cohere API key and desired port:
    ```bash
    COHERE_API_KEY=your_cohere_api_key
    PORT=5000
    ```

## Usage

Instructions on how to use the application.

1. **Start the Flask application**:
   ```bash
     python app.py
   ```
2. Open a web browser and go to ```http://localhost:5000``` to interact with the chatbot.
## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](License) file for details.

## Acknowledgements

- [Cohere](https://cohere.ai) for providing the natural language processing API.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Python](https://www.python.org/) for being the programming language of choice.
