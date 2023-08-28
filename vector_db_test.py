from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import AzureOpenAI
from langchain import PromptTemplate
import openai
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma, FAISS
from langchain.document_loaders import PyPDFLoader
import langchain


import os
import getpass

import prompts.anki as anki

# openai_api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
# openai_api_key = os.getenv("AZURE_OPENAI_KEY_1")
ENGINE_NAME = "EricChatGPT"
# openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")

to_load = ["./pdf_data/giussani_cardiovascular_handout.pdf",
           "./pdf_data/fraser_cardiovascular_handout.pdf"]

llm = AzureOpenAI(
    temperature=0,
    deployment_name=ENGINE_NAME,
    model_name=ENGINE_NAME,
)
embeddings = langchain.embeddings.HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

faiss_index = None


for i, path in enumerate(to_load):
    loader = PyPDFLoader(path)
    text_splitter = CharacterTextSplitter(separator='\n \n', chunk_size=200, chunk_overlap=0)
    docs = loader.load_and_split(text_splitter)

    if i == 0:
        faiss_index = FAISS.from_documents(docs, embeddings)
    else:
        faiss_index_i = FAISS.from_documents(docs, embeddings)
        faiss_index.merge_from(faiss_index_i)

    print(path + '; n: ' + str(len(docs)) + ' docs added')

faiss_index.save_local("./vectorstores/cardiovascular_HFembeddings")

docs = faiss_index.similarity_search(anki.arteriolar_control_card, k=3)
for doc in docs:
    print(str(doc.metadata["page"]) + ":", doc.page_content)

'''text_splitter = CharacterTextSplitter(chunk_size=10, chunk_overlap=0)
documents = text_splitter.split_documents(pages)
print(len(documents))
db = Chroma.from_documents(documents[:15], OpenAIEmbeddings())


query = "Lindqvist effect"
docs = db.similarity_search(query)
print(docs[0].page_content)'''