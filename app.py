import streamlit as st
from nltk.chat.util import Chat, reflections

# Define chatbot pairs
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you today?"]),
    (r"how are you?", ["I'm doing great, thanks for asking!", "I'm doing well, how about you?"]),
    (r"what is your name?", ["I am Shivbot, your chatbot created in Jupyter."]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Bye, have a great day!"]),
    (r"(.*) your name?", ["My name is Chatbot.", "I'm Chatbot, nice to meet you!"]),
    (r"(.*)", ["Sorry, I didn't understand that.", "Can you please clarify?", "I'm not sure how to respond to that."]),
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

# Streamlit app
st.title("Shivbot 🤖")
st.markdown("Chat with me below! Type your message and press Enter.")

# Get user input
user_input = st.text_input("You: ", placeholder="Type your message here...")

# Display chatbot response
if user_input:
    response = chatbot.respond(user_input)
    if user_input.lower() in ['bye', 'goodbye', 'quit']:
        st.write("🤖 Chatbot: Goodbye! 👋")
    else:
        st.write(f"🤖 Chatbot: {response}")
