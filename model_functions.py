from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
import chromadb
import ollama

bs_transformer = BeautifulSoupTransformer()
client = chromadb.Client()
collection = client.create_collection("new")


def readNew(url):
    loader = AsyncChromiumLoader([url])
    body = bs_transformer.transform_documents(
        loader.load(), tags_to_extract=["article"]
    )
    title = bs_transformer.transform_documents(loader.load(), tags_to_extract=["h1"])

    # embedding
    str_body = str(body)
    str_title = str(title)
    response = ollama.embeddings(model="mxbai-embed-large", prompt=str_body)
    embedding = response["embedding"]
    collection.add(ids=[str_title], embeddings=[embedding], documents=[str_body])

    # results
    response = ollama.embeddings(prompt=str_title, model="mxbai-embed-large")
    results = collection.query(query_embeddings=[response["embedding"]], n_results=1)
    data = results["documents"][0][0]

    output = ollama.generate(
        model="llama3.2",
        prompt=f"Using this data: {data}. And based on the title {title} answer what happened? and why?",
    )

    print(output["response"])
    collection.delete(ids=[str_title])
