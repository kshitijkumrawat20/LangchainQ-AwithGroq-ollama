
# Q&A ChatBot with Groq and ollama

This is a Streamlit-based chatbot application that uses LangChain and Groq models and ollama models to respond to user queries. The app allows you to select different models, set temperature settings, and control the response length using a user-friendly interface.

## Features

- **Multiple Model Selection:** Choose from a variety of models such as `llama3-70b-8192`, `llama3-8b-8192`, `mixtral-8x7b-32768`, and more.
- **Customizable Settings:** Adjust parameters like temperature and maximum tokens to refine responses.
- **Interactive Chat Interface:** Easily input your questions and receive responses directly.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kshitijkumrawat20/LangchainQ-AwithGroq-ollama.git
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   Create a `.env` file in the root directory and add your API keys:

   ```plaintext
   LANGCHAIN_API_KEY=your_langchain_api_key
   LANGCHAIN_PROJECT=your_langchain_project_name
   ```

## Usage

1. Run the application:

   ```bash
   streamlit run app.py
   ```

2. Enter your Groq API key and select the model from the sidebar.

3. Adjust the temperature and max tokens settings as needed.

4. Input your question in the text box and get responses from the chatbot.

## Configuration

### Sidebar Settings

- **API Key Input:** Enter your Groq API key.
- **Model Selection:** Choose from a list of available models.
- **Temperature:** Control the randomness of the output (0.0 - deterministic, 1.0 - more random).
- **Max Tokens:** Limit the length of the response.

### Example Environment Variables

Create a `.env` file with the following content:

```plaintext
LANGCHAIN_API_KEY=your_api_key
LANGCHAIN_PROJECT=your_project_name
```

## Contributing

Feel free to open issues or submit pull requests if you want to improve the app. All contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact:

- **Author:** Kshitij Kumrawat
- **Email:** [kshitijk146@gmail.com](mailto:kshitijk146@gmail.com)


