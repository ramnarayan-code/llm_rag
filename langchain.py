# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r2Cq6R1FOODKLLaz12stEr5Z2gNqQ6-c
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install --upgrade --quiet  langchain langchain-openai faiss-cpu tiktoken

from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import os
os.environ['OPENAI_API_KEY'] = ''
print(os.getenv('OPENAI_API_KEY'))

vectorstore = FAISS.from_texts(
    ["Vegetables & Fruits are in Section A",
    "Cereals are in Section B",
    "Milk products are in Section C",
    "Household cleaning are in Section D",
    "Baby products are in Section E",
    "Chocolates are in Section F"], embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()

template = """
Provide only the location of the product for the given customer's query in the Question
1. Classify the product requested in the customer's query under one of the following categories:
    - Vegetables & Fruits
    - Cereals
    - Milk products
    - Household cleaning
    - Baby products
    - Chocolates
2. Based on the category, follow the below location instructions and provide the location of the product briefly:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI()

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

chain.invoke("where is onion?")

chain.invoke("where could i find diapers?")

chain.invoke("where could one find Harpic?")

chain.invoke("where could one find Ritter sports?")

chain.invoke("where could I find pacifier?")

chain.invoke("how could I locate Müsli?")

chain.invoke("how could I locate Kelloggs?")

chain.invoke("where could I find Bottle food?")
