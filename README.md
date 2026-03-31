# 🍽️ RAGFood: Local-to-Cloud RAG Migration Project
---
# 👩🏻‍💼 Author
**Joanna Marie Fesalbon**  
---

**Cloud Migration / RAGFood Project**

## 💻 Project Overview
RAGFood is a food recommendation and food information retrieval system built using **Retrieval-Augmented Generation (RAG)**.  
This project started as a **local-only implementation** using **ChromaDB** and a local LLM workflow, then was migrated into a **cloud-powered version** using **Upstash Vector** and **Groq API**.

The goal of this project is to demonstrate how a traditional local RAG system can be transformed into a more scalable, cloud-ready solution while preserving retrieval quality and improving deployment readiness.

This repository contains both:

- **Local Version (Week 2)** → ChromaDB-based retrieval system
- **Cloud Version (Week 3)** → Upstash Vector + Groq-powered RAG system

---

# 🎯 Project Objectives
This project was completed to achieve the following:

- Build a functional local Retrieval-Augmented Generation system
- Migrate vector storage from local database to cloud vector database
- Replace local model workflow with cloud-based LLM inference
- Improve system organization, maintainability, and documentation
- Expand the dataset with more diverse and detailed food entries
- Test semantic retrieval quality and response performance
- Present the final system in a professional GitHub portfolio format

---

# 🧠 What is RAG?
**RAG (Retrieval-Augmented Generation)** is a system design that combines:

1. **Retrieval** → finds the most relevant stored information
2. **Generation** → uses an LLM to answer naturally based on the retrieved context

Instead of answering only from model memory, the system first searches a knowledge base and then generates a response grounded in those results.

In this project, the knowledge base is a curated food dataset containing descriptions, cuisine origin, nutritional value, cooking methods, dietary tags, allergens, and cultural context.

---

# 🏗️ Repository Structure

RAGFOOD-MAIN
├── .vscode
├── chroma_db
├── cloud-version
│ ├── data
│ │ └── foods.json
│ ├── docs
│ │ ├── Week 3 Test Queries
│ │ └── Comparison and Quality Assessment
│ ├── MIGRATION_PLAN.md
│ ├── .env
│ └── rag_run.py
├── local-version
├── foods.json
├── Q1.png
├── Q2.png
├── Q3.png
├── rag_run.py
├── .gitignore
└── README.md

---

# ⚙️ System Architecture

## 📍 BEFORE: Local RAG Architecture

```text
User Question
     │
     ▼
rag_run.py
     │
     ├── Generate Query Embedding using Ollama
     │        │
     │        ▼
     │   Ollama Embeddings API
     │
     ├── Search Similar Documents
     │        │
     │        ▼
     │     ChromaDB
     │
     ├── Retrieve Top Food Entries
     │
     ├── Build Prompt with Context
     │
     ├── Send Prompt to Ollama
     │        │
     │        ▼
     │   Ollama Generate API
     │
     ▼
Final Answer to User

```

### Local Version Components
- **Python CLI application**
- **ChromaDB** for local vector storage
- **foods.json** as dataset source
- Local retrieval and generation pipeline

### Local Version Characteristics
- Works offline or locally
- Requires local setup and dependencies
- Retrieval depends on locally stored vectors
- More manual setup for embeddings and storage

---

## ☁️ AFTER: Cloud RAG Architecture

```text
User Question
     │
     ▼
rag_run.py
     │
     ├── Query Relevant Food Entries
     │        │
     │        ▼
     │   Upstash Vector Database
     │
     ├── Retrieve Top Food Entries
     │
     ├── Build Prompt with Context
     │
     ├── Send Prompt to Groq Cloud API
     │        │
     │        ▼
     │   Groq LLM (llama-3.1-8b-instant)
     │
     ▼
Final Answer to User

```

### Cloud Version Components
- **Python CLI application**
- **Upstash Vector** for cloud-based semantic retrieval
- **Groq API** for fast answer generation
- Expanded and enhanced food dataset
- Improved modular and cloud-ready workflow

### Cloud Version Characteristics
- Cloud-based vector storage
- Faster and more scalable retrieval pipeline
- Cleaner deployment path
- Better suited for production-style workflows

---

# 🔄 Cloud Migration Overview

This project migrated the local RAG implementation into a cloud-based system by changing the retrieval and generation stack.

## Key Migration Changes

### ✅ Vector Database Migration
**Before:** ChromaDB  
**After:** Upstash Vector

The local vector store was replaced with a cloud vector database to support scalable semantic search and easier cloud integration.

### ✅ Embedding Workflow Simplification
**Before:** manual/local embedding process  
**After:** raw text upsert into Upstash

The cloud version was updated to upload raw text directly instead of relying on local vector handling logic.

### ✅ LLM Integration Upgrade
**Before:** local/original LLM workflow  
**After:** Groq API

The generation layer was migrated to **Groq** for faster cloud-based inference.

### ✅ Improved Error Handling
The cloud version includes:
- dependency checks
- environment variable checks
- safer startup handling
- cloud service failure awareness

### ✅ Data Enhancement
The food database was expanded to support:
- richer semantic search
- better cultural exploration
- stronger nutritional and dietary filtering
- more realistic user food queries

---

# 🍜 Enhanced Food Database

## 📊 Dataset Summary
The food dataset was expanded and enriched to improve retrieval quality and answer relevance.

### Database includes:
- Enhanced food database showcase (35 items) 15 in Week 2 and 20 in Week 3
- **20 newly added enhanced food items**
- Broader cuisine representation
- More health-conscious options
- More comfort food entries
- Improved metadata for semantic retrieval

---

## 🧩 Newly Added Dataset Categories

### 🌍 8 World Cuisine Items
Examples include:
- Shakshuka
- Ceviche
- Jerk Chicken
- Feijoada
- Bobotie
- Koshari
- Borscht
- Moussaka

### 🥗 6 Health-Conscious Items
Examples include:
- Quinoa Chickpea Buddha Bowl
- Grilled Salmon with Quinoa
- Lentil Spinach Soup
- Tofu Vegetable Stir Fry
- Greek Yogurt Berry Parfait
- Zucchini Turkey Meatballs

### 🍲 6 Comfort Food Dishes
Examples include:
- Chicken Noodle Soup
- Shepherd’s Pie
- Macaroni and Cheese
- Beef Stroganoff
- Arroz Caldo
- Baked Ziti

---

## 📌 Data Fields Included
Each enhanced food entry may include:

- `id`
- `name`
- `text`
- `region`
- `type`
- `ingredients`
- `cooking_method`
- `nutritional_benefits`
- `cultural_background`
- `regional_variations`
- `dietary_tags`
- `allergens`

This richer structure improves the system’s ability to answer:

- Cuisine-based questions
- Nutritional preference questions
- Dietary restriction queries
- Comfort food exploration
- Cooking method searches
- Ingredient-based discovery

---

# 🖥️ Local Version Setup (Week 2)

## 📁 Location

```
</> bash
local-version/
```

## Purpose
This is the original local implementation of the food RAG system using **ChromaDB**.

## Run the local version
From the root project folder:

```
</> bash
cd local-version
python rag_run.py
```

## Local Version Notes
- Uses local vector retrieval
- Represents the original Week 2 implementation
- Preserved for comparison against the cloud version

---

# ☁️ Cloud Version Setup (Week 3)

## 📁 Location

```
</> bash
cloud-version/
```

## Purpose
This is the migrated cloud implementation using:

- **Upstash Vector**
- **Groq API**

## Run the cloud version
From the root project folder:

```
</> bash
cd cloud-version
python rag_run.py
```

---

# 🔐 Environment Variables Configuration

The cloud version requires a `.env` file inside:

```
</> bash
cloud-version/
```

## Required variables

```env
UPSTASH_VECTOR_REST_URL=your_upstash_url_here
UPSTASH_VECTOR_REST_TOKEN=your_upstash_token_here
GROQ_API_KEY=your_groq_api_key_here
```

## Important
This `.env` file is **not uploaded publicly** for security reasons.

---

# 📦 Cloud Version Dependencies

Install dependencies inside the cloud version:

**Manually install core dependencies:**

```
</> bash
pip install python-dotenv upstash-vector groq
```

---

# 🧪 Testing and Query Validation

The cloud version was tested using a wide range of food-related natural language queries.

## Testing Evidence
Testing screenshots are stored in:

```
</> bash
cloud-version/docs/Week 3 Test Queries/
```

This includes **15 test query screenshots** used to validate retrieval quality and answer generation.

---

## Query Testing Categories

### Semantic Similarity Queries
Example:
- “I want something healthy and egg-based from North Africa, Any suggestion?”

### Multi-Criteria Queries
Example:
- “Which baked Mediterranean dish is made with eggplant and meat?”

### Nutritional Queries
Example:
- “I want plant-based bowl that's filling and nutritious”

### Cultural Exploration Queries
Example:
- “Which brazilian comfort food is known for black beans and meat”

### Cooking Method Queries
Example:
- “Which dish ”

---cooks eggs directly in tomato sauce?"

# 📈 Performance and Quality Assessment

Comparison and quality evaluation are documented in:

```bash
cloud-version/docs/Comparison and Quality Assesment.txt
```

This file includes:
- retrieval observations
- answer quality review
- response comparison
- cloud vs local performance discussion

---

# ⚖️ Local vs Cloud Comparison

| Category | Local Version | Cloud Version |
|---------|--------------|--------------|
| Vector Storage | ChromaDB | Upstash Vector |
| LLM / Generation | Local / Original Workflow | Groq API |
| Deployment Style | Local-only | Cloud-ready |
| Scalability | Limited | Better |
| Retrieval Workflow | Local database | Cloud vector retrieval |
| Setup Complexity | Moderate | Moderate with API setup |
| Speed | Slower / setup-heavy | Faster response generation |
| Portfolio Readiness | Basic | Professional / deployable |

# ⚡ High-Level Architecture Comparison

| Component | Previous Local Version | New Cloud Version | Reason for Change |
|----------|-------------------------|-------------------|------------------|
| Vector Database | ChromaDB | Upstash Vector Database | Managed cloud vector storage |
| Embeddings | Ollama local embeddings | Upstash vector search workflow | Removes local embedding dependency |
| LLM | Ollama (`llama3.2`) | Groq (`llama-3.1-8b-instant`) | Faster, cloud-based inference |
| Data Storage | Local JSON + local DB | Local JSON + cloud vector DB | More scalable retrieval layer |
| Deployment Style | Local-only | Cloud-ready | Better for real-world usage |

---

# 🧾 Example Comparison Summary

## Cloud Version Example
**Query:**  
> Which cheesy baked pasta dish is perfect for family meals?

### Top Retrieved Matches
- Baked Ziti
- Macaroni and Cheese
- Moussaka
- Beef Stroganoff

### Result
The cloud version successfully identified **Baked Ziti** as the most appropriate answer.

### Performance
**Retrieval + Generation Time:** ~1.18 seconds

### Quality
- **Accuracy:** High
- **Relevance:** High

---

## Local Version Example
**Query:**  
> What is Chicken Adobo?

### Top Retrieved Matches
- Chicken Adobo detailed description
- Adobo variant
- One less relevant result

### Result
The local version returned a correct explanation of Chicken Adobo.

### Performance
Slower overall due to more local processing and setup overhead.

### Quality
- **Accuracy:** Good
- **Relevance:** Mostly good, but with one unrelated retrieval

---

# 🧠 Migration Learnings

This migration project demonstrated several important practical lessons:

- Cloud vector databases simplify retrieval infrastructure
- Better metadata improves semantic search performance
- Cloud-hosted LLMs can significantly improve response speed
- Clean repository organization makes technical projects easier to present
- Testing is important not only for correctness, but also for relevance and usability

---

# 📂 Documentation Included

## Available documentation in this repository:

### Migration Planning
```
</> bash
cloud-version/docs/MIGRATION_PLAN.md
```

### Comparison and Quality Assessment
```
</> bash
cloud-version/docs/Comparison and Quality Assesment.txt
```

### Test Query Evidence
```
</> bash
cloud-version/docs/Week 3 Test Queries/
```

### Dependency Reference

```
</> bash
pip install python-dotenv upstash-vector groq
```

---

# 🛠️ Troubleshooting Guide

## 1. `ModuleNotFoundError`
### Cause:
A required package is not installed.

### Fix:
```
</> bash
pip install python-dotenv upstash-vector groq
```

---

## 2. `.env` variables not loading
### Cause:
The `.env` file is missing or placed in the wrong folder.

### Fix:
Make sure `.env` is inside:

```
</> bash
cloud-version/
```

and contains:

```env
UPSTASH_VECTOR_REST_URL=your_upstash_url_here
UPSTASH_VECTOR_REST_TOKEN=your_upstash_token_here
GROQ_API_KEY=your_groq_api_key_here
```

---

## 3. Upstash connection errors
### Cause:
Invalid URL or token.

### Fix:
Double-check your Upstash Vector credentials.

---

## 4. Groq API errors
### Cause:
Invalid or expired API key.

### Fix:
Generate a valid API key and update your `.env`.

---

## 5. Wrong folder when running files
### Cause:
Running `rag_run.py` from the wrong directory.

### Fix:
Use the correct folder:

### For local:
```
</> bash
cd local-version
python rag_run.py
```

### For cloud:
```
</> bash
cd cloud-version
python rag_run.py
```

---

# 🚀 Version Control and Development Workflow

## Branch Used
```
</> bash
cloud-migration
```

## Git Workflow Completed
- Created a dedicated migration branch
- Organized local and cloud implementations
- Documented migration and comparison
- Prepared the project for portfolio presentation

---

# 🏷️ Suggested Release Tags

Recommended tags for milestone tracking:

```
</> bash
v1.0  → local-only implementation
v2.0  → cloud-migration implementation
```

---

# 📚 Final Reflection
This project shows the complete transition from a **basic local RAG prototype** into a **more scalable and portfolio-ready cloud RAG system**.

It demonstrates not only code migration, but also:
- Retrieval design thinking
- Cloud integration
- Structured testing
- Documentation discipline
- Repository presentation skills

**The final result is a more complete and professional Retrieval-Augmented Generation project centered around food discovery, information retrieval, and semantic search.**
