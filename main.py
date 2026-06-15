def chatbot():
    print("🤖 AI Customer Support Chatbot")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Bot: Thank you for visiting. Have a great day!")
            break

        elif "order" in user_input:
            print("Bot: Please provide your order ID. (Demo: ORDER123)")

        elif "return" in user_input or "refund" in user_input:
            print("Bot: Returns are accepted within 30 days of delivery.")

        elif "recommend" in user_input or "product" in user_input:
            print(
                "Bot: I recommend our lightweight waterproof camping tent for outdoor trips."
            )

        elif "human" in user_input or "agent" in user_input:
            print(
                "Bot: A support representative will contact you shortly. "
                "Please share your email."
            )

        else:
            print(
                "Bot: I can help with orders, returns, product recommendations, "
                "and customer support."
            )


if __name__ == "__main__":
    chatbot()
