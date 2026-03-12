Here’s a clear, beginner-friendly `README.md` for your RAG project, designed to explain what it does, how it works, and how someone can run it from scratch.

---

## 📄 `README.md`

````markdown
# 🧠 RAG-Food: Simple Retrieval-Augmented Generation with ChromaDB + Ollama

This is a **minimal working RAG (Retrieval-Augmented Generation)** demo using:

- ✅ Local LLM via [Ollama](https://ollama.com/)
- ✅ Local embeddings via `mxbai-embed-large`
- ✅ [ChromaDB](https://www.trychroma.com/) as the vector database
- ✅ A simple food dataset in JSON (Indian foods, fruits, etc.)

---

## 🎯 What This Does

This app allows you to ask questions like:

- “Which Indian dish uses chickpeas?”
- “What dessert is made from milk and soaked in syrup?”
- “What is masala dosa made of?”

It **does not rely on the LLM’s built-in memory**. Instead, it:

1. **Embeds your custom text data** (about food) using `mxbai-embed-large`
2. Stores those embeddings in **ChromaDB**
3. For any question, it:
   - Embeds your question
   - Finds relevant context via similarity search
   - Passes that context + question to a local LLM (`llama3.2`)
4. Returns a natural-language answer grounded in your data.

---

## 📦 Requirements

### ✅ Software

- Python 3.8+
- Ollama installed and running locally
- ChromaDB installed

### ✅ Ollama Models Needed

Run these in your terminal to install them:

```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
````

> Make sure `ollama` is running in the background. You can test it with:
>
> ```bash
> ollama run llama3.2
> ```

---

## 🛠️ Installation & Setup

### 1. Clone or download this repo

```bash
git clone https://github.com/yourname/rag-food
cd rag-food
```

### 2. Install Python dependencies

```bash
pip install chromadb requests
```

### 3. Run the RAG app

```bash
python rag_run.py
```

If it's the first time, it will:

* Create `foods.json` if missing
* Generate embeddings for all food items
* Load them into ChromaDB
* Run a few example questions

---

## 📁 File Structure

```
rag-food/
├── rag_run.py       # Main app script
├── foods.json       # Food knowledge base (created if missing)
├── README.md        # This file
```

---

## 🧠 How It Works (Step-by-Step)

1. **Data** is loaded from `foods.json`
2. Each entry is embedded using Ollama's `mxbai-embed-large`
3. Embeddings are stored in ChromaDB
4. When you ask a question:

   * The question is embedded
   * The top 1–2 most relevant chunks are retrieved
   * The context + question is passed to `llama3.2`
   * The model answers using that info only

---

## 🔍 Try Custom Questions

You can update `rag_run.py` to include your own questions like:

```python
print(rag_query("What is tandoori chicken?"))
print(rag_query("Which foods are spicy and vegetarian?"))
```

---

## 🚀 Next Ideas

* Swap in larger datasets (Wikipedia articles, recipes, PDFs)
* Add a web UI with Gradio or Flask
* Cache embeddings to avoid reprocessing on every run

---

## 👨‍🍳 Credits

Made by Callum using:

* [Ollama](https://ollama.com)
* [ChromaDB](https://www.trychroma.com)
* [mxbai-embed-large](https://ollama.com/library/mxbai-embed-large)
* Indian food inspiration 🍛

---

# RAG Food System Enhancement

## Author
Joanna Marie Fesalbon

---

## Project Overview

This project enhances the RAG (Retrieval-Augmented Generation) Food System by expanding its food database with 15 additional food entries. The goal of this enhancement is to improve the system’s ability to answer diverse food-related queries using semantic search and vector embeddings.

The added entries include Filipino dishes, healthy Filipino food options, and unique international dishes. These additions allow the RAG system to retrieve more relevant information and generate more accurate responses when users ask questions related to food, nutrition, and cultural cuisine.

This project also demonstrates the use of Git and GitHub for professional development workflows including repository forking, committing changes, resolving merge conflicts, and pushing updates to a remote repository.

---

# Added Food Items

## Filipino Cuisine
1. Chicken Adobo  
2. Sinigang  
3. Pancit Canton  
4. Kare-Kare  
5. Lechon
   
## Healthy Filipino Foods
6. Chopsuey  
7. Chicken Tinola  
8. Ginisang Monggo  
9. Ensaladang Talong  
10. Fresh Lumpiang Ubod

## International Dishes
11. Paella (Spain)
12. Goulash (HUngary)
13. Tagine (Morocco)
14. Pierogi (Poland)
15. Ratatouille (France)

These additions improve the diversity of the food knowledge base and allow the system to respond to a wider range of queries.

---

# Installation and Setup

Follow these steps to run the project locally.

## 1. Clone the Repository

```bash
git clone https://github.com/joannafesalbon02/ragfood.git

## 2. Navigate to the Project Folder

```bash
cd ragfood

## 3. Run the RAG System

```bash
python rag_run.py

After running the script, the system will allow users to ask questions related to the food items stored in the database.

---

# Sample Queries Tested

The RAG system was tested with different types of food-related questions to evaluate how well it retrieves information from the database.

Example queries include:
- What is Chicken Adobo?
- Tell me about sinigang.
- Which foods are healthy?
- Which food are good for balanced diet?
- Tell me about European dishes in the database.
- What foods come from Asia?
- What foods are commonly served during celebration?
- Why is Lechon considered a special dish in Filipino celebration?
- Which foods are cooked by slow simmering
- What dishes are usually served with rice?

These tests confirm that the RAG system can successfully retrieve and generate responses using the enhanced food dataset.

---

# Screenshots

Screenshots of the RAG system answering queries are included in the **screenshots folder** to demonstrate successful system operation and testing.

Example screenshots include:



---

# Personal Reflection

This project helped me understand how Retrieval-Augmented Generation (RAG) works by combining a knowledge database with language models. Through this activity, I learned how structured datasets can be used to enhance AI systems by providing them with additional knowledge sources that improve response accuracy.

By adding new food entries to the database, I observed how the RAG system retrieves relevant information using vector embeddings and semantic similarity instead of relying only on exact keyword matches. This allows the system to generate more meaningful responses based on the context of the user’s question.

Another important part of this project was learning how to use Git and GitHub for version control. I practiced important development workflows such as forking a repository, committing changes, resolving merge conflicts, and pushing updates to a remote repository. These experiences helped me better understand how developers manage and maintain collaborative projects.

Overall, this project strengthened my understanding of AI-powered information retrieval systems and improved my technical skills in Python, Git, and repository management. It also demonstrated how RAG systems can be applied to real-world applications such as intelligent search tools and AI-powered knowledge assistants.

