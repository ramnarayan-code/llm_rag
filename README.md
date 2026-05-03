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

### Example
## Uploaded EU AI Act PDF in the PageIndex Platform
<img width="1905" height="935" alt="image" src="https://github.com/user-attachments/assets/7fb4eca2-cf80-4287-abb3-58b37e6477cd" /> <br/>

## Example queries
<img width="1615" height="748" alt="Screenshot 2026-05-03 102326" src="https://github.com/user-attachments/assets/145aaae3-b079-49c2-bf73-a66f3944e495" /> <br/>


<img width="1420" height="748" alt="image" src="https://github.com/user-attachments/assets/3249cd5d-c02b-438c-ba26-a960f3141cbd" /> <br/>



<img width="681" height="563" alt="image" src="https://github.com/user-attachments/assets/64af35cd-1435-45a8-84cb-da33b7e6c566" />
