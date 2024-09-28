# Web Content Analyzer

This project is a Python-based tool that analyzes web content using language models and vector embeddings. It fetches web pages, processes their content, and generates summaries based on the extracted information.

## Features

- Web page content extraction
- Text embedding generation
- Vector database integration
- AI-powered content summarization

## Dependencies

- langchain_community
- ollama
- chromadb
- streamlit

## Main Components

### model_functions.py

This file contains the core functionality of the project:

- `readNew(url, collection)`: Fetches a web page, processes its content, generates embeddings, and produces a summary.

### main.py

This file is the entry point of the application. It uses Streamlit to create a simple web user interface:

- Initializes a ChromaDB collection called "news"
- Provides a user interface to input a URL
- Processes the input URL using the `readNew` function
- Displays the generated summary

## Usage

To use this tool:

1. Make sure you have Ollama set up with the following models:

   - mxbai-embed-large (for embeddings)
   - llama3.2 (for text generation)

2. Install the necessary dependencies:

   ```bash
   pip install langchain_community ollama chromadb streamlit
   ```

3. Run the Streamlit application:

   ```bash
   streamlit run main.py
   ```

4. Enter a URL in the web interface to analyze the content.

## Note

This project is currently set up to use local models through Ollama. Ensure you have the required models installed and configured properly.

## Future Improvements

- Add error handling and input validation
- Implement caching to avoid repeated processing of the same URLs
- Expand documentation with setup instructions and examples
- Enhance the user interface with more options and visualizations

## License

[MIT](https://choosealicense.com/licenses/mit/)
