from faq import FAQ_RESPONSES
from product_data import PRODUCTS

print("🤖 AI Customer Support Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("Bot: Thanks for visiting!")
        break

    elif "return" in user:
        print("Bot:", FAQ_RESPONSES["return"])

    elif "refund" in user:
        print("Bot:", FAQ_RESPONSES["refund"])

    elif "shipping" in user:
        print("Bot:", FAQ_RESPONSES["shipping"])

    elif "tent" in user:
        print("Bot:", PRODUCTS["tent"])

    elif "backpack" in user:
        print("Bot:", PRODUCTS["backpack"])

    elif "sleeping" in user:
        print("Bot:", PRODUCTS["sleeping bag"])

    elif "human" in user or "agent" in user:
        print("Bot: A human support representative will contact you shortly.")

    else:
        print("Bot: I can help with returns, refunds, shipping, products, and customer support.")
