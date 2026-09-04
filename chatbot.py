# Basic Rule-Based Chatbot
# CodeAlpha - Task 4

def get_response(user_input):
    text = user_input.lower().strip()

    if text in ["hello", "hi", "hey", "yo", "hiya"]:
        return "Hi! How can I help you today?"
    elif "how are you" in text or "how're you" in text:
        return "I'm fine, thanks! How about you?"
    elif "your name" in text or "who are you" in text:
        return "I'm a simple chatbot built for the CodeAlpha internship."
    elif "what can you do" in text or "help" in text:
        return "You can ask me things like 'hello', 'how are you', 'what's the time', or say 'bye' to exit."
    elif "thank" in text:
        return "You're welcome!"
    elif "your age" in text or "how old are you" in text:
        return "I don't have an age — I'm just a bunch of code!"
    elif "weather" in text:
        return "I can't check live weather, but I hope it's nice outside!"
    elif "time" in text:
        import datetime
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}."
    elif "joke" in text:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"
    elif "what is your purpose" in text or "why were you made" in text:
        return "I was built as a CodeAlpha internship project to practice rule-based logic in Python."
    elif text in ["bye", "goodbye", "exit", "quit", "see you"]:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Try saying 'help' to see what I can do."

def main():
    print("=" * 40)
    print("        SIMPLE CHATBOT")
    print("=" * 40)
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit", "see you"]:
            break

if __name__ == "__main__":
    main()