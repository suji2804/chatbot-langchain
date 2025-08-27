# Chatbot with OpenAI and Langchain

This project is a simple chatbot web application built using [Streamlit](https://streamlit.io/), [Langchain](https://python.langchain.com/), and [OpenAI](https://openai.com/) APIs. The chatbot answers user questions about Large Language Models (LLMs).

## Features

- Interactive web UI using Streamlit
- Uses OpenAI's GPT-3.5-turbo model via Langchain
- Customizable prompt template
- Environment variable support for API keys

## Setup

1. **Clone the repository**  
   ```
   git clone <your-repo-url>
   cd chatbot
   ```

2. **Create and activate a virtual environment**  
   ```
   python -m venv venv
   venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

4. **Create a `.env` file**  
   Add your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   LANGCHAIN_API_KEY=your_langchain_api_key
   ```

## Running the App

Start the Streamlit server:
```
streamlit run app.py
```
Open the provided local URL in your browser.

## Usage

- Enter a question about LLMs in the input box.
- The chatbot will respond using OpenAI's GPT-3.5-turbo model.

## File Structure

- `app.py` — Main Streamlit app
- `.env` — Environment variables (not included; create your own)
- `requirements.txt` — Python dependencies

## Notes

- Make sure your API keys are valid and have sufficient quota.
- Do **not** share your `.env` file or API keys publicly.

