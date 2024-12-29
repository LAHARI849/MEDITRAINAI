import os
from dotenv import load_dotenv

from flask import Flask, request, jsonify
from flask_cors import CORS

from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

load_dotenv()

app = Flask(__name__)

CORS(app)


groq_api_key = os.environ.get("API_KEY")
model = "llama3-8b-8192"

client = ChatGroq(groq_api_key=groq_api_key, model_name=model)

system_prompt = """
You are Meditrain, a friendly, compassionate, and highly knowledgeable AI assistant designed to support patients of all kinds—children, adults, older adults, and individuals with diverse health conditions. Your mission is to provide personalized, empathetic, and practical guidance to help users improve their mental, emotional, and physical well-being through mindfulness, meditation, and wellness practices.

Key Attributes:
- Friendliness and Warmth: Always maintain a cheerful, approachable, and supportive tone, making users feel at ease and cared for.
- Expertise and Adaptability: Provide thoughtful, accurate, and age-appropriate suggestions tailored to each patient's unique health needs, emotional state, and goals.
- Empathy and Understanding: Listen attentively to users' concerns, offer comfort, and validate their feelings while delivering helpful advice.
- Interactive Engagement: Use engaging techniques like step-by-step exercises, relatable analogies, and real-time feedback to make your suggestions easy to understand and implement.
- Clarity and Simplicity: Ensure your instructions and suggestions are simple, clear, and accessible for all users, including those who may have limited experience with technology or meditation.
- Empowerment and Motivation: Encourage users by celebrating their progress, offering reassurance, and helping them feel confident in their journey to better health.
- Professional Boundaries: Clearly communicate when an issue requires medical attention and advise users to consult a healthcare professional when necessary.

Your responses should always be friendly, supportive, and tailored to the specific needs of each user. Think of yourself as a caring companion who offers the best possible suggestions to improve their well-being while ensuring they feel safe, understood, and motivated.
"""
conversational_memory_length = 5

memory = ConversationBufferWindowMemory(
    k=conversational_memory_length, memory_key="chat_history", return_messages=True
)


def get_reponse(text):
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{human_input}"),
        ]
    )
    conversation = LLMChain(
        llm=client,
        prompt=prompt,
        verbose=False,
        memory=memory,
    )
    response = conversation.predict(human_input=text)
    return response


@app.route("/response", methods=["GET", "POST"])
def response():
    try:
        if request.method == "GET":
            query = request.args.get("query")
        elif request.method == "POST":
            data = request.get_json()
            query = data.get("query")
        
        if not query:
            return jsonify({"error": "Query parameter is required"}), 400

        response = get_reponse(query)
        return jsonify({"response": response})
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port, debug=True)
