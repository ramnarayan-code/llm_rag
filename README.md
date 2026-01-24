# PageIndex RAG Agent

An expert AI chatbot specialized in the EU AI Act, powered by **PageIndex** and LangChain. This agent demonstrates how to build a high-performance RAG (Retrieval-Augmented Generation) application with minimal setup.

## 🚀 Why PageIndex?

PageIndex is a **vectorless, reasoning-based RAG (retrieval) framework** that simulates how human experts navigate and extract knowledge from long, complex documents. 

Instead of relying on vector similarity search, it transforms documents into a **tree-structured index** and enables LLMs to perform **agentic reasoning** over that structure for context-aware retrieval. 

### Comparison: PageIndex vs. Conventional Vector DB

| Feature | Conventional Vector DB (Pinecone, Weaviate, etc.) | PageIndex |
| :--- | :--- | :--- |
| **Data Preparation** | Requires manual chunking, overlapping, and cleaning. | **No chunking required.** Just upload the document. |
| **Embedding** | Must choose an embedding model and manage vector conversions. | **Vectorless.** Uses a tree-structured index for reasoning-based retrieval. |
| **Retrieval Method** | K-Nearest Neighbors (KNN) based on mathematical similarity. | **Agentic Reasoning.** Simulates human expert navigation. |
| **Traceability** | Often a "black box"; hard to explain why specific chunks matched. | **Interpretable & Traceable.** Retrieval logic is clear and reasoned. |
| **Infrastructure** | Requires managing a vector database and index pipeline. | **Zero infra.** Direct API-driven insight without the overhead. |
| **Context Awareness** | Often loses document structure and hierarchy. | **Full Context.** Understands the document's original structure. |

## ✨ Features

- **Direct Document Querying**: Talk to your PDF as if it were a knowledge base.
- **Structural Understanding**: Automatically retrieves and understands the document's table of contents.
- **Interactive CLI**: Easy-to-use command-line interface for real-time questions.
- **EU AI Act Expert**: Pre-configured to provide professional insights into the European Union AI Act.

## 🛠️ Setup

### 1. Prerequisites
- Python 3.8+
- [PageIndex](https://pageindex.ai) API Key
- OpenAI API Key

### 2. Installation
Clone the repository and install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file or export the following variables:
- `PAGEINDEX_API_KEY`: Your PageIndex API Key.
- `OPENAI_API_KEY`: Your OpenAI API Key.
- `EU_AI_ACT_DOCUMENT_ID`: The ID of the EU AI Act document in your PageIndex workspace.

## 🏃 Running the Application

You can use the provided shell script to quickly launch the agent:

```bash
./run_rag.sh
```

Or run it directly with Python:

```bash
python pageindex_rag_agent.py
```

## 📁 Codebase Overview

- `pageindex_rag_agent.py`: The core LangChain agent logic, including tools for querying documents and fetching tree structures.
- `run_rag.sh`: A helper script to set environment variables and start the agent.
- `eu_ai_act.pdf`: The reference document used by the agent.
- `requirements.txt`: Project dependencies.
