from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
import ollama


bs_transformer = BeautifulSoupTransformer()


def readNew(url, collection):
    loader = WebBaseLoader(url)
    document = loader.load()

    title = document[0].metadata["title"]
    body = document[0].page_content[:3000]

    # Embedding
    str_body = str(body)
    str_title = str(title)
    response = ollama.embeddings(model="mxbai-embed-large", prompt=str_body)
    embedding = response["embedding"]
    collection.add(ids=[str_title], embeddings=[embedding], documents=[str_body])

    # Results
    response = ollama.embeddings(prompt=str_title, model="mxbai-embed-large")
    results = collection.query(query_embeddings=[response["embedding"]], n_results=1)
    data = results["documents"][0][0]

    output = ollama.generate(
        model="llama3.2",
        prompt=f"Using this data: {data}. And based on the title {title} answer what happened? and why?",
    )

    collection.delete(ids=[str_title])

    return str(output["response"])
