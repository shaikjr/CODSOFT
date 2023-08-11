def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if user_input in ["hey", "hello", "hi"]:
        return "Hello! How can I help you today?"
    elif "hlo" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here to help!"
    elif "what's your name" in user_input or "who are you" in user_input:
        return "I am a simple rule-based chatbot."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "thank you" in user_input:
        return "You're welcome!"
    elif "help" in user_input:
        return "I'm here to assist you. What do you need help with?"
    elif "weather" in user_input:
        return "I'm sorry, but I don't have access to real-time data. You can check a weather website or app for that!"
    else:
        return "I'm sorry, I didn't quite understand that."

print("Chatbot: Hi there! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
