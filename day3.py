import re

# A dictionary that maps keywords to predefined responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm a chatbot created to assist you.",
    "help": "Sure, I'm here to help. What do you need assistance with?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! I'm happy to help.",
    "default": "I'm not sure I understand. Could you please rephrase?"
}


# FUNCTION TO FIND THE APPROPRIATE RESPONSE
def chatbot_response(text):
    # convert
    text = text.lower()
    # iterate through the predefined
    for response in responses:
        if re.search(response, text, re.IGNORECASE):
            return responses[response]
    # function
    return responses["default"]

    # Main function


def chatbot():
    print("Chatbot: hello how are u ")
    while True:
        # Get user input
        user_input = input("You: ")
        # If user exit => exit
        if user_input.lower() == "exit":
            print("Goodbye")
            break
        #
        response = chatbot_response(user_input)
        #
        print("Response:",response)
# run chatbot
chatbot()