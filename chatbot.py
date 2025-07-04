print("Welcome! I'm PoliteBot. Type 'exit' anytime to leave.")

while True:
    msg = input("You: ").lower()

    if msg == "exit":
        print("PoliteBot: It was a pleasure talking to you. Goodbye!")
        break
    elif "hello" in msg or "hi" in msg:
        print("PoliteBot: Hello! How may I assist you today?")
    elif "thanks" in msg or "thank you" in msg:
        print("PoliteBot: You're most welcome!")
    elif "weather" in msg:
        print("PoliteBot: Sorry, I can't check the weather yet.")
    else:
        print("PoliteBot: I'm still learning. Could you please rephrase?")
