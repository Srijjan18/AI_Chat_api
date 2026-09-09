# AI Chat Application

A simple AI-powered chat application built using FastAPI and Google Gemini API. Users can enter messages through a web interface and receive AI-generated responses.

## Features

- Interactive web-based chat interface
- FastAPI backend
- Google Gemini LLM integration
- REST API endpoints
- Environment variable support for secure API key storage
- Basic error handling

## Tech Stack

- Python
- FastAPI
- Google Gemini API
- Pydantic
- HTML
- CSS
- JavaScript

## Project Structure

```text
AI_chat_api/
│
├── main.py
├── llm_service.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── static/
    └── index.html
```

## API Endpoints

### GET /

Loads the AI Chat web application.

### POST /chat

Sends a user message to the Gemini LLM and returns the generated response.

Example request:

```json
{
  "message": "Explain FastAPI in simple words"
}
```

Example response:

```json
{
  "response": "FastAPI is a Python framework used to build APIs and backend services."
}
```

### GET /models

Returns information about the configured LLM.

Example response:

```json
{
  "model": "gemini-3.6-flash",
  "provider": "Google Gemini"
}
```

## Application Flow

```text
User
  ↓
Web Frontend
  ↓
FastAPI Backend
  ↓
Gemini API
  ↓
Gemini LLM
  ↓
FastAPI Response
  ↓
Web Frontend
```

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd AI_chat_api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```bash
uvicorn main:app --reload
```

Open the application in your browser:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

## Author

Srijjan Thummaji