def simple_chatbot():
    print("🤖 Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        # Take user input
        user_input = input("You: ").lower().strip()

        # Exit condition
        if user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day 😊")
            break

        # Greeting responses
        elif "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hello! How can I help you?")

        # Asking about the chatbot
        elif "who are you" in user_input or "what are you" in user_input:
            print("🤖 Chatbot: I’m a simple rule-based chatbot created using Python!")

        # Asking about time
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"🤖 Chatbot: The current time is {now}.")

        # Asking about date
        elif "date" in user_input:
            from datetime import datetime
            today = datetime.now().strftime("%Y-%m-%d")
            print(f"🤖 Chatbot: Today’s date is {today}.")

        # Asking for help
        elif "help" in user_input:
            print("🤖 Chatbot: I can answer basic questions like time, date, or greetings!")

        # Asking how chatbot is
        elif "how are you" in user_input:
            print("🤖 Chatbot: I’m just a program, but I’m running fine! How about you?")

        # Asking about creator
        elif "who made you" in user_input:
            print("🤖 Chatbot: I was created by a Python programmer!")

        # Default response for unknown queries
        else:
            print("🤖 Chatbot: I’m not sure how to respond to that. Try asking something else.")

# Run the chatbot
if _name_ == "_main_":
    simple_chatbot()