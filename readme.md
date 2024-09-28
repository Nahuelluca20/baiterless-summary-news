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
- chromadb (implied by the use of collections)

## Main Components

### model_functions.py

This file contains the core functionality of the project:

- `readNew(url, collection)`: Fetches a web page, processes its content, generates embeddings, and produces a summary.

### main.py

(Content not provided, but assumed to be the entry point of the application)

## Usage

To use this tool, you need to have Ollama set up with the following models:

- mxbai-embed-large (for embeddings)
- llama3.2 (for text generation)

Then, you can call the `readNew` function with a URL and a vector collection to analyze web content.

## Note

This project is currently set up to use local models through Ollama. Ensure you have the required models installed and configured properly.

## Future Improvements

- Add error handling and input validation
- Implement caching to avoid repeated processing of the same URLs
- Expand documentation with setup instructions and examples

## License

[Add your chosen license here]
