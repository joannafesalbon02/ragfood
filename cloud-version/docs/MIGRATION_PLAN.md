</> Markdown

# **Migration Plan: Local RAG System to Cloud RAG System**

## **1. Project Overview**

This document outlines the migration of a **local Retrieval-Augmented Generation (RAG) system** into a **cloud-based implementation** using modern managed services. The original system was designed for local execution using **ChromaDB** for vector storage and **Ollama** for both embeddings and language generation. The new cloud version replaces those local components with **Upstash Vector Database** and **Groq Cloud API**.

The purpose of this migration is to improve:

- scalability
- maintainability
- cloud readiness
- deployment portability
- performance consistency

This migration preserves the original RAG workflow while modernizing the infrastructure to better reflect production-style system design.

---

## **2. Migration Goals**

The migration was planned to achieve the following technical goals:

- Replace **ChromaDB** with **Upstash Vector Database**
- Replace **local Ollama embeddings** with **Upstash cloud vector search workflow**
- Replace **local Ollama text generation** with **Groq Cloud API**
- Remove local-only dependencies that prevent cloud deployment
- Improve system portability and maintainability
- Keep the original RAG pipeline structure intact

---

## **3. High-Level Architecture Comparison**

| Component | Previous Local Version | New Cloud Version | Reason for Change |
|----------|-------------------------|-------------------|------------------|
| Vector Database | ChromaDB | Upstash Vector Database | Managed cloud vector storage |
| Embeddings | Ollama local embeddings | Upstash vector search workflow | Removes local embedding dependency |
| LLM | Ollama (`llama3.2`) | Groq (`llama-3.1-8b-instant`) | Faster, cloud-based inference |
| Data Storage | Local JSON + local DB | Local JSON + cloud vector DB | More scalable retrieval layer |
| Deployment Style | Local-only | Cloud-ready | Better for real-world usage |

---

## **4. Architecture Overview**

## **4.1 Before Migration: Local RAG Architecture**

The original system was built as a **fully local Retrieval-Augmented Generation (RAG) application**.  
All major components ran on the developer machine, including embeddings, vector storage, and language generation.

### **Workflow**

1. User enters a food-related question
2. The question is converted into an embedding using **Ollama**
3. The embedding is searched inside **ChromaDB**
4. Top matching food entries are retrieved
5. Retrieved food entries are used as context
6. Context + user question are sent to **Ollama**
7. Ollama generates the final answer
8. Answer is shown to the user

### **Local Architecture Diagram**

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

---

**Key Characteristics of the Local Architecture**

- Fully offline and local
- No external API usage
- No cloud deployment support
- Requires local installation of:
    - Ollama
    - ChromaDB
    - local models
- Suitable for prototyping but limited for production-style deployment

---

## **4.2 After Migration: Cloud RAG Architecture**

The migrated system transforms the project into a cloud-based RAG application by replacing local infrastructure with managed cloud services.

### **Workflow**

1. User enters a food-related question
2. The question is sent directly to Upstash Vector Database
3. Upstash retrieves the most semantically relevant food entries
4. Retrieved food entries are used as context
5. Context + user question are sent to Groq Cloud API
6. Groq generates the final answer
7. Answer is shown to the user

### **Cloud Architecture Diagram**


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

---

**Key Characteristics of the Cloud Architecture**

- Retrieval uses Upstash Vector Database
- Answer generation uses Groq Cloud API
- No local LLM runtime required
- No local vector database required
- More scalable and deployment-ready
- Better suited for cloud-hosted applications

---

## **4.3 Architecture Change Summary**

**Before Migration**

- Vector database: ChromaDB
- Embeddings: Ollama local embeddings
- LLM: Ollama local generation
- Infrastructure type: Fully local

**After Migration**

- Vector database: Upstash Vector Database
- Embeddings/search flow: Cloud-based vector retrieval
- LLM: Groq Cloud API
- Infrastructure type: Cloud-ready hybrid architecture

---

## **4.4 Why the New Architecture is Better**

**The cloud architecture is better suited for real-world deployment because it:**

- removes heavy local setup requirements
- improves maintainability
- supports cloud-based scaling
- separates retrieval and generation into modern managed services
- reflects a more production-ready AI application design

---

## **5. Original Local RAG Workflow**

**The original local system followed this process:**

- Load food data from foods.json
- Generate embeddings locally using Ollama
- Store vectors in ChromaDB
- Accept a user question
- Generate an embedding for the user query
- Retrieve top matching food entries from ChromaDB
- Build a context prompt from retrieved documents
- Send prompt to Ollama for answer generation
- Return answer to the user

This workflow remains conceptually the same after migration. The major changes occur only in the infrastructure and API integrations.

---

## **6. Database Migration Plan: ChromaDB → Upstash Vector Database**

## **6.1 Objective**

The goal of this migration is to replace the local ChromaDB vector store used in the previous RAG implementation with Upstash Vector Database, a cloud-hosted vector database service. This improves scalability, cloud compatibility, and deployment readiness while preserving the same retrieval-based workflow.

---

## **6.2 Current Implementation (Local)**

The original RAG system used ChromaDB as a local vector database.

**Current setup:**

- Database type: local persistent vector store
- Storage path: chroma_db/
- Collection name: foods
- Embeddings: manually generated using Ollama embeddings API
- Similarity search: handled locally inside ChromaDB

**Current advantages:**

- Fully local and offline
- No cloud service dependency
- Easy for local prototyping

**Current limitations:**

- Requires local storage and environment setup
- Harder to deploy in cloud-based environments
- Embedding generation depends on local Ollama model availability
- Less suitable for scalable production use

---

## **6.3 Target Implementation (Cloud)**

The migrated system replaces local ChromaDB with Upstash Vector Database.

**Target setup:**

- Vector database: Upstash Vector
- Database type: cloud-hosted
- Index type: Dense
- Similarity function: Cosine
- Embedding model: bge-large-en-v1.5
- Authentication: REST URL and REST token stored in .env

**Expected benefits:**

- Managed cloud vector storage
- No local database setup required
- Easier production deployment
- Better architecture for cloud RAG workflows

---

## 6.4 Migration Strategy

The database migration preserves the original retrieval behavior while replacing the storage and embedding infrastructure.

**The retrieval flow remains:**

1. Load food data from JSON
2. Convert food entries into searchable vector records
3. Store entries in the vector database
4. Accept a user query
5. Retrieve the most relevant food entries
6. Pass retrieved context into the LLM

**The major changes are:**

- Before: ChromaDB local vector store
- After: Upstash Vector cloud database

And:

- Before: local manual embedding generation through Ollama
- After: Upstash-based semantic search using stored text data

---

## **6.5 Code Chages Required**

**Previous ChromaDB Setup**

```python
import chromadb

chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)
collection = chroma_client.get_or_create_collection(name=COLLECTION_NAME)
```

**Previous Local Embedding Logic**

```python
def get_embedding(text):
    response = requests.post("http://localhost:11434/api/embeddings", json={
        "model": EMBED_MODEL,
        "prompt": text
    })
    return response.json()["embedding"]
```

**Previous Add Logic**

```python
collection.add(
    documents=[item["text"]],
    embeddings=[emb],
    ids=[item["id"]]
)
```

**New Upstash Setup**

```python
from upstash_vector import Index

index = Index(url=UPSTASH_VECTOR_REST_URL, token=UPSTASH_VECTOR_REST_TOKEN)
```

**New Upsert Logic**

```python
vectors_to_upload.append({
    "id": str(item["id"]),
    "data": enriched_text,
    "metadata": {
        "raw_text": json.dumps(item)
    }
})
```

```python
index.upsert(vectors=vectors_to_upload)
```

**New Query Logic**

```python
results = index.query(data=question, top_k=3, include_metadata=True)
```

---
This removes the need for local embedding generation and simplifies the retrieval pipeline.
---

## **6.6 Environment Variable Update**

The Upstash Vector database requires secure credentials stored in the .env file.

**Required environment variables:**

```
</> env

UPSTASH_VECTOR_REST_URL=your_upstash_url_here
UPSTASH_VECTOR_REST_TOKEN=your_upstash_token_here
```

---

## ** 6.7 Data Storage Strategy**

To improve retrieval quality, each food entry is stored with enriched searchable text.

The searchable text is built from:

main food description
- region
- food type
- Example enrichment

**Original:**

“Lechon is a famous Filipino roasted pig dish…”

**Enriched:**

“Lechon is a famous Filipino roasted pig dish… This food is popular in the Philippines. It is a type of Main Course.”

This improves semantic retrieval without requiring a more complex schema.

---

## **6.8 Metadata Strategy**

Each vector record stores the original JSON entry inside metadata:

```python
"metadata": {
    "raw_text": json.dumps(item)
}
```

This allows the system to:

retrieve the original food content
display source entries
build the final LLM context dynamically

This preserves the RAG design from the local system while improving cloud retrieval flexibility.

---

## **6.9 Error Handling Plan**

Because Upstash is a cloud service, the database layer now depends on external availability.

**Planned safeguards:**

- catch invalid REST token or REST URL issues
- catch upsert failures
- catch query failures
- prevent application crashes during retrieval

**Fallback behavior:**

- if upsert fails, display an upload error
- if query fails, show a retrieval error
- continue program safely when possible

**Example fallback message:**

“The cloud vector database is temporarily unavailable. Please try again later.”

---

## **6.10 Data Migration Considerations**

The migration does not require preserving the original ChromaDB vector files.

**Instead, migration is handled by:**

- Loading the existing foods.json
- Re-uploading all items into Upstash Vector
- Allowing Upstash-based retrieval for future queries

This is a re-indexing migration, not a direct database export/import process.

**This is acceptable because:**

- the JSON dataset remains the source of truth
- the vector database can be rebuilt anytime
- the data is fully reproducible

---

## **6.11 Testing Approach

The vector migration should be validated using realistic semantic search queries.

**Testing goals:**

- confirm food entries upload successfully
- confirm relevant foods are retrieved
- compare retrieval quality against ChromaDB version
- confirm metadata is preserved and usable

**Example test queries:**

- “What is lechon?”
- “Healthy Mediterranean food”
- “Spicy vegetarian Asian dishes”
- “Foods that can be grilled”
- “Traditional comfort food”

**Validation criteria:**

- relevant retrieval results
- correct food context displayed
- stable query execution
- no crashes during repeated use

---

## **6.12 Performance Comparison Expectations**

The migration is expected to improve maintainability and deployment readiness more than raw local speed.

**Expected improvements:**

- cloud-based accessibility
- no local database dependency
- easier integration with production environments
- simplified retrieval workflow

**Expected trade-offs:**

- internet connection required
- external service dependency
- possible network latency

These trade-offs are acceptable for a cloud-ready RAG architecture.

---

## **6.13 Final Database Migration Decision**

The migration from ChromaDB to Upstash Vector Database is justified because it improves:

- cloud deployment readiness
- maintainability
- architecture simplicity
- compatibility with cloud-hosted RAG systems

This modernizes the retrieval layer while preserving the original RAG workflow.

---

## **7. LLM Migration Plan: Ollama → Groq Cloud API**

## **7.1 Objective**

The goal of this migration is to replace the local Ollama-based LLM inference used in the original RAG system with Groq Cloud API for faster, cloud-based text generation. This change supports better scalability, reduced local dependency, and easier deployment in a production-ready environment.

---

## **7.2 Current Implementation (Local)**

The original local RAG system used Ollama running on the developer machine.

**Current setup:**

- Model: llama3.2
- Endpoint: http://localhost:11434/api/generate
- Request type: direct HTTP POST using requests
- Streaming: disabled
- Inference: fully local
- Cost: no external API charges

**Current advantages:**

- No API costs
- Simple offline testing
- No internet dependency

**Current limitations:**

- Requires Ollama installation and local model download
- Limited portability across systems
- Slower on low-resource machines
- Difficult to deploy in cloud or production environments

---

7.3 Target Implementation (Cloud)

The migrated system replaces local Ollama inference with Groq Cloud API.

**Target setup:**

- Model: llama-3.1-8b-instant
- API Provider: Groq Cloud
- Authentication: GROQ_API_KEY stored in .env
- Request method: Groq Python SDK
- Inference: cloud-hosted
- Cost model: usage-based

**Expected benefits:**

- Faster inference performance
- Easier deployment across environments
- No need to install local LLM runtime
- Cleaner production-ready architecture

---

## **7.4 Migration Strategy**

The migration focuses only on the generation layer of the RAG system.

**The retrieval flow remains the same:**

- User enters a question
- Relevant food entries are retrieved from vector database
- Retrieved context is inserted into a prompt
- Prompt is sent to the LLM
- Final answer is returned to the user

**The only major change is the LLM backend:**

- Before: Ollama local API
- After: Groq Cloud API

---

## **7.5 Code Changes Required**

**Previous Ollama Generation Logic**

```python
response = requests.post("http://localhost:11434/api/generate", json={
    "model": LLM_MODEL,
    "prompt": prompt,
    "stream": False
})

return response.json()["response"].strip()
```

**New Groq Cloud Logic**

```python
from groq import Groq

client = Groq(api_key=GROQ_API_KEY)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.7,
    max_completion_tokens=700,
    top_p=1,
    stream=False
)

return response.choices[0].message.content.strip()
```
---

## **7.6 Environment Variable Update**

The Groq API requires authentication through an API key stored in the .env file.

**Required environment variable**

```
</> env
GROQ_API_KEY=your_actual_groq_api_key_here
```
This allows the application to securely access Groq Cloud without hardcoding credentials.

---

## **7.7 Error Handling Plan**

The migration introduces an external API dependency, so error handling becomes more important.

**Planned safeguards:**

- catch invalid API key errors
- catch model request failures
- catch network connectivity issues
- catch empty or malformed response objects

**Handling approach:**

- wrap Groq generation call in try/except
- return a user-friendly fallback message if generation fails
- prevent system crash during query loop

**Example fallback response:**

“The cloud language model is currently unavailable. Please try again later.”

---

## **7.8 Rate Limiting Considerations**

Because Groq is a cloud API, requests may be subject to usage limits.

**Considerations:**

- avoid unnecessary repeated requests
- limit completion length using max_completion_tokens
- use moderate temperature for efficient generation
- use only one completion call per user query

**Mitigation:**

- keep prompts concise
- send only top retrieved food entries as context
- avoid large irrelevant context blocks

---

## **7.9 Cost Implications and Usage Monitoring**

Unlike local Ollama, Groq Cloud introduces usage-based cost considerations.

**Local Ollama:**

- no API billing
- requires local compute resources

**Groq Cloud:**

- API-based usage
- easier deployment
- better performance, but must be monitored

**Recommended monitoring approach:**

- track number of queries tested
- keep prompts efficient
- use reasonable token limits
- review Groq dashboard for request usage if needed

## **7.10 Fallback Strategy**

If Groq Cloud fails temporarily, the system should remain stable.

**Planned fallback behavior:**

- catch exception during API call
- display clear error message
- continue the RAG loop without terminating the program

**Optional future fallback:**

- reconnect to local Ollama if cloud inference is unavailable
- add retry logic for temporary failures

**For this implementation, the primary fallback is:**

- graceful failure without crashing the app

---

## **7.11 Testing Approach**

The LLM migration should be validated using the same RAG queries previously used in the local version.

**Testing goals:**

- confirm Groq returns valid generated answers
- compare answer clarity against local Ollama
- check prompt formatting compatibility
- confirm no crashes occur during repeated queries

**Example test prompts:**

- “What is lechon?”
- “Suggest a healthy Asian dish.”
- “What are traditional Filipino comfort foods?”
- “Which foods are high in protein?”
- “What food is best for rainy weather?”

**Validation criteria:**

- correct response generation
- clear use of retrieved context
- stable output formatting
- no API-related crashes

---

## **7.12 Performance Comparison Expectations**

**The migration is expected to improve:**

- response speed
- deployment readiness
- system portability

**Expected improvements:**

- faster answer generation than local Ollama on low-spec machines
- more consistent output quality
- reduced setup dependency for end users

**Expected trade-offs:**

- internet connection required
- external API dependency
- usage-based billing instead of fully local inference

---

## **7.13 Final LLM Migration Decision**

**The migration from local Ollama to Groq Cloud API is justified because it improves:**

- deployment readiness
- cloud compatibility
- performance consistency
- maintainability for future development

This change aligns the RAG system with a more realistic production environment while preserving the same retrieval-augmented workflow from the local implementation.

---

## **8. Risk and Mitigation**

| Risk | Impact | Mitigation |
|------|--------|------------|
| Invalid API key | LLM/database connection fails | Validate .env configuration before execution |
| Internet connection issues | Retrieval or generation fails | Add try/except handling and graceful fallback |
| Cloud API downtime | Query response unavailable | Show user-friendly error messages |
| Incorrect data formatting | Retrieval quality decreases | Validate JSON structure before upload |
| Token usage growth | Higher API usage costs | Limit prompt size and completion length |


---

## **9. Implementation Decision Summary**

The cloud migration preserves the same RAG workflow from the local version while replacing local infrastructure components with managed cloud services.

**Preserved:**

- same dataset-driven retrieval logic
- same user interaction flow
- same prompt-building workflow
- same RAG architecture

**Migrated:**

- ChromaDB → Upstash Vector
- Ollama embeddings → Upstash-based vector workflow
- Ollama generation → Groq Cloud API

This migration demonstrates a practical transition from a local prototype into a more scalable and deployment-ready cloud architecture.




















