import streamlit as st
import requests
import json

class AgricultureChatbot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.groq_url = "https://api.groq.com/openai/v1/chat/completions"  # Groq API URL

    def agriculture_chatbot(self, user_input):
        """Agriculture chatbot using Groq"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        
        payload = {
            "model": "llama3-8b-8192",  # Replace with the correct model name if needed
            "messages": [
                {"role": "system", "content": "You are a helpful AI assistant specialized in agriculture. You assist users with farming advice, crop management, pest control, irrigation, soil health, and general agricultural queries. Always encourage users to consult with local agricultural experts or professionals for tailored advice."},
                {"role": "user", "content": user_input}
            ],
            "max_tokens": 150
        }

        try:
            response = requests.post(self.groq_url, json=payload, headers=headers)
            response_data = response.json()

            if 'choices' in response_data and len(response_data['choices']) > 0:
                return response_data['choices'][0]['message']['content']
            else:
                return "Sorry, I couldn't generate a response. Please try again later."

        except Exception as e:
            return f"Chatbot error: {str(e)}"

# Initialize Groq API key for chatbot
api_key = "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"  # Your Groq API key
chatbot = AgricultureChatbot(api_key)  # Creating an instance of the agriculture chatbot

# Title of the app
st.title("Agriculture Chatbot")

# Input field for user to ask questions
user_input = st.text_input("Ask a farming-related question:")

if st.button('Ask'):
    if user_input:
        # Get the response from the chatbot
        response_message = chatbot.agriculture_chatbot(user_input)
        st.write(f"**Chatbot:** {response_message}")
    else:
        st.warning("Please ask a valid question.")
