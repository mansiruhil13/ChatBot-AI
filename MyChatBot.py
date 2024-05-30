import random

# Define responses for different types of user input
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "name": ["I am bot, how may i help you today?"],
    "farewell": ["Goodbye!", "See you later!", "Have a great day!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "age": ["I am just a computer program, so I don't have an age.",
            "I don't age like humans, but I'm always here to assist you!"],
    "weather": ["I'm sorry, I cannot provide real-time weather information.",
                "You might want to check a weather website or app for that."],
    "joke": ["Why don't scientists trust atoms? Because they make up everything!",
             "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them!"],
    "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm not sure I follow."],
}

# Function to generate a response based on user input
def get_response(message):
    message = message.lower()
    if any(word in message for word in ["hello", "hi", "hey"]):
        return random.choice(responses["greeting"])
    if any(word in message for word in ["name"]):
        return random.choice(responses["name"])
    elif any(word in message for word in ["goodbye", "bye", "see you"]):
        return random.choice(responses["farewell"])
    elif any(word in message for word in ["thanks", "thank you"]):
        return random.choice(responses["thanks"])
    elif "age" in message:
        return random.choice(responses["age"])
    elif "weather" in message:
        return random.choice(responses["weather"])
    elif "joke" in message:
        return random.choice(responses["joke"])
    else:
        return random.choice(responses["default"])

# Main loop to interact with the user
def main():
    print("Welcome to the Rule-based Chatbot!")
    print("Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        else:
            response = get_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()
