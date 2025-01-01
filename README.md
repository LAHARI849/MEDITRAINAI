
# MEDITRAIN AI

Meditrain ai is an AI-powered chatbot application designed to provide personalized and compassionate support to individuals seeking mindfulness, meditation, and wellness guidance. This repository contains the backend API (app2.py), the user interface (ui.py), and the requirements.txt for managing dependencies.

# LIVE DEMO
You can view the live version of this project here: [Live Demo](https://meditrainai-27.onrender.com)

## Features

- **Friendly and Compassionate**: Offers a cheerful, supportive tone to make users feel at ease.
- **Personalized Guidance**: Provides age-appropriate, tailored suggestions based on the user's needs.
- **Interactive Engagement**: Utilizes step-by-step exercises and relatable analogies to simplify suggestions.
- **Empowerment and Motivation**: Encourages users by celebrating progress and boosting confidence.



## Installation


## Prerequisites
- Ensure you have the following installed on your system:

    Python 3.8 or later

    pip (Python package installer)

- Installation Steps

   1) **Clone the repository:**

   - git clone https://github.com/your_username/meditrain.git
          cd meditrain

   2) **Install dependencies:**
   - Run the following command to install the required Python packages:

      pip install -r requirements.txt

   3) **Create a .env file:**
- Inside the project directory, create a file named .env and add your Groq API key:

      API_KEY=your_groq_api_key

   4) **Run the backend server:**
- Start the Flask application:

      python app2.py

    The server will run on http://127.0.0.1:5000.

  5) **Run the frontend:**
- Start the Streamlit application:

      streamlit run ui.py

   - Access the application on http://localhost:8501.

## Files in the Repository

- **app2.py:**

  This file contains the Flask-based backend server that interacts with the Groq API to process user queries and return AI-generated responses.

- **ui.py:**

  This file contains the Streamlit-based user interface that allows users to interact with the chatbot.

- **requirements.txt:**

  This file lists all the dependencies required for the project.
    
## API Reference

The backend server exposes the following API endpoint:

## POST /response
- Description: Accepts a user query and returns an AI-generated response.

  - Request Body (JSON):

  {
  "query": "your question here"
  }

   - Response Body (JSON):
  {
  "response": "AI response here"
  }
## Contributing

We welcome contributions to improve Meditrain! To contribute:

Fork the repository.

- Create a new branch (git checkout -b feature-name).

- Make your changes and commit them (git commit -m 'Add feature').

- Push to the branch (git push origin feature-name).

- Open a pull request.


## License

This project is licensed under the MIT License. See the LICENSE file for more details.


## Acknowledgements

 - Groq API

- LangChain

- Streamlit

- Flask

## Roadmap

## Current Project Structure

The project is organized into the following components:

- **Backend (app2.py)**: Implements the Flask API that handles user queries and integrates with the Groq API for AI responses.

- **Frontend (ui.py)**: Provides a user-friendly interface built with Streamlit for interacting with the chatbot.

- **Environment Configuration (.env)**: Contains sensitive API keys for secure integration.

- **Dependencies (requirements.txt)**: Lists all Python packages required to run the application.

## Future enhancements may include:

- Expanding the chatbot’s memory capabilities.

- Adding support for multiple languages.

- Integrating advanced analytics to track user engagement.


## Screenshot
## CHAT INTERFACE
![Screenshot](https://github.com/LAHARI849/MEDITRAINAI/blob/1c33f41d63b70fcde50e2f664bfe0eedd953b984/frontend/screenshot.jpeg)

