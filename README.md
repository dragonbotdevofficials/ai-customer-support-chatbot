# AI Customer Support Chatbot

A simple customer support chatbot built with Python.

## Features

- Order tracking assistance
- Return and refund guidance
- Product recommendations
- Human support handoff
- Interactive command-line interface

## Example

```
You: I want to return my order
Bot: Returns are accepted within 30 days of delivery.
```

## Run

```bash
python main.py
```

## Future Improvements

- AI integration (OpenAI/Gemini)
- FastAPI web API
- Database-backed order lookup
- Multi-language support
- Web interface

- ## Sample Conversation

```text
You: Where is my order?
Bot: Please provide your order ID.

You: I want to return my product.
Bot: Returns are accepted within 30 days of delivery.

You: Recommend a camping tent.
Bot: I recommend our lightweight waterproof camping tent.

You: I need a human agent.
Bot: Please share your email and our support team will contact you.
```

## AI Integration

This project is designed to support AI-powered customer interactions using Google Gemini. Configure your own API key in a local `.env` file before running AI features.

```text
GEMINI_API_KEY=your_api_key_here
```

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API server:

```bash
uvicorn app:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

FastAPI will automatically generate interactive API documentation where you can test the chatbot endpoint.

## Example API Request

POST `/chat`

```json
{
  "message": "Where is my order ORDER123?"
}
```

Example Response:

```json
{
  "user_message": "Where is my order ORDER123?",
  "bot_reply": "Your order ORDER123 is currently in transit and is expected to arrive in 2 days."
}
```
