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
👩🏻‍💼 Joanna Marie Fesalbon

---

## 💻 Project Overview 

   This project enhances the RAG (Retrieval-Augmented Generation) Food System by expanding its food database with 15 additional food entries. The goal of this enhancement is to improve the system’s ability to answer diverse food-related queries using semantic search and vector embeddings.

   The added entries include Filipino dishes, healthy Filipino food options, and unique international dishes. These additions allow the RAG system to retrieve more relevant information and generate more accurate responses when users ask questions related to food, nutrition, and cultural cuisine.

This project also demonstrates the use of Git and GitHub for professional development workflows including repository forking, committing changes, resolving merge conflicts, and pushing updates to a remote repository.

---

# 🍽️ Added Food Items 

## 🍜 Filipino Cuisine 
1. Chicken Adobo  
2. Sinigang  
3. Pancit Canton  
4. Kare-Kare  
5. Lechon
   
## 🥗 Healthy Filipino Foods 
6. Chopsuey  
7. Chicken Tinola  
8. Ginisang Monggo  
9. Ensaladang Talong  
10. Fresh Lumpiang Ubod

## 🌏 International Dishes 
11. Paella (Spain)
12. Goulash (HUngary)
13. Tagine (Morocco)
14. Pierogi (Poland)
15. Ratatouille (France)

These additions improve the diversity of the food knowledge base and allow the system to respond to a wider range of queries.

---

## 🗂️ Project Structure

```
ragfood/
│
├── foods.json      # Food database containing food information
├── rag_run.py      # Python script to run the RAG system
├── README.md       # Project documentation
├── .gitignore      # Git ignore configuration
├── Q1.png          # Sample query result
├── Q2.png          # Sample query result
└── Q3.png          # Sample query result
```

---

## 💻🖱️ Installation and Setup

---

Follow these steps to run the project locally.

Clone the Repository

### 1. Clone the Repository

```
</> Bash
git clone https://github.com/joannafesalbon02/ragfood
```

### 2. Navigate to the Project Folder

```
Command
cd ragfood
```

### 3. Run the RAG System

```
Command
python rag_run.py
```

After running the script, the system will allow users to ask questions related to the food items stored in the database.

---

# 🧐 Sample Queries Tested

The RAG system was tested with different types of food-related questions to evaluate how well it retrieves information from the database.

Example queries include:
- What is Chicken Adobo?
- Tell me about sinigang.
- Which foods are healthy?

These tests confirm that the RAG system can successfully retrieve and generate responses using the enhanced food dataset.

Below are sample queries executed in the RAG Food System demonstrating how the system retrieves food information from the enhanced dataset.

## 💾 Sample Query Results:

### Query 1
[Query 1 Result](Q1.png)

### Query 2
[Query 2 Result](Q2.png)

### Query 3
[Query 3 Result](Q3.png)

---
```
## Enhancements Made

The following improvements were implemented in this project:

- Added 15 new food items to the database
- Expanded the food dataset for better retrieval
- Implemented Git workflow using forked repository
- Added documentation and sample query results
```
---
# 📝 Personal Reflection

   Working on this project helped me understand how Retrieval-Augmented Generation (RAG) systems function by combining a knowledge database with language models. Before doing this activity, I only had a basic idea of how AI could answer questions using stored information. Through building and testing the RAG Food System, I was able to see how an AI model can retrieve relevant data from a structured dataset and use it to generate more accurate and meaningful responses.

   One of the most interesting parts of the project was adding new food items to the database and observing how the system responded to different queries. Instead of relying only on exact keyword matches, the system uses vector embeddings and semantic similarity to find related information. This means the system can understand the context of a user’s question and return relevant results even if the wording of the query is slightly different. Seeing this process in action helped me better understand how modern AI systems retrieve and process information.

   Another valuable learning experience was using Git and GitHub for version control. I practiced important development steps such as forking a repository, committing changes, resolving merge conflicts, and pushing updates to my remote repository. These tasks helped me understand how developers manage project versions and collaborate on shared codebases.

   Overall, this project improved my understanding of AI-powered retrieval systems and strengthened my technical skills in Python, Git, and repository management. It also showed me how RAG technology can be applied to real-world systems such as intelligent search tools and AI-based knowledge assistants.

