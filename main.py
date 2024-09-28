import chromadb
import streamlit as st

from model_functions import readNew

client = chromadb.Client()

if "news" not in [col.name for col in client.list_collections()]:
    collection = client.create_collection("news")
else:
    collection = client.get_collection("news")

st.write(
    """
# My first app
Hello *world!*
"""
)

title = st.text_input("New URL", placeholder="Add URl")
if title:
    with st.spinner("Processing..."):
        response = readNew(title, collection)
        print(response)
        st.write(response)
