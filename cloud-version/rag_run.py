import os
import json
import time

try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: python-dotenv module not found. Install it with: pip install python-dotenv")
    exit(1)

try:
    import upstash_vector # type: ignore
except ImportError:
    print("Error: upstash_vector module not found. Install it with: pip install upstash-vector")
    exit(1)

try:
    from groq import Groq # type: ignore
except ImportError:
    print("Error: groq module not found. Install it with: pip install groq")
    exit(1)

load_dotenv()

UPSTASH_URL = os.getenv("UPSTASH_VECTOR_REST_URL")
UPSTASH_TOKEN = os.getenv("UPSTASH_VECTOR_REST_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

JSON_FILE = os.path.join("data", "foods.json")
LLM_MODEL = "llama-3.1-8b-instant"

if not UPSTASH_URL or not UPSTASH_TOKEN:
    print("Error: Missing Upstash credentials in .env file.")
    exit(1)

if not GROQ_API_KEY:
    print("Error: Missing GROQ_API_KEY in .env file.")
    exit(1)

if not os.path.exists(JSON_FILE):
    print(f"Error: File not found -> {JSON_FILE}")
    exit(1)

index = upstash_vector.Index(url=UPSTASH_URL, token=UPSTASH_TOKEN)
groq_client = Groq(api_key=GROQ_API_KEY)

try:
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        food_data = json.load(f)
except Exception as e:
    print(f"Error loading foods.json: {e}")
    exit(1)

def upload_data():
    vectors_to_upload = []

    for item in food_data:
        enriched_text = item.get("text", "")

        if item.get("region"):
            enriched_text += f" This food is popular in {item['region']}."
        if item.get("type"):
            enriched_text += f" It is a type of {item['type']}."

        vectors_to_upload.append({
            "id": str(item.get("id", "")),
            "data": enriched_text,
            "metadata": {
                "raw_text": json.dumps(item)
            }
        })

    try:
        index.upsert(vectors=vectors_to_upload)
        print(f"Uploaded {len(vectors_to_upload)} food items to Upstash! 🟢")
    except Exception as e:
        print(f"Error uploading data to Upstash: {e}")
        exit(1)

def rag_query(question):
    start_time = time.time()

    try:
        results = index.query(data=question, top_k=5, include_metadata=True)
    except Exception as e:
        return f"Error retrieving data from Upstash: {e}"

    top_docs = []
    top_matches = []

    print("\nTop matches from database:")

    for match in results:
        raw = ""
        if hasattr(match, "metadata") and match.metadata:
            raw = match.metadata.get("raw_text", "")

        if not raw:
            continue

        try:
            food_item = json.loads(raw)
            doc = food_item.get("text", "")
            food_name = food_item.get("name", "Unknown Food")
            food_region = food_item.get("region", "Unknown Region")
            food_type = food_item.get("type", "Unknown Type")

            if doc:
                top_docs.append(doc)
                top_matches.append({
                    "name": food_name,
                    "region": food_region,
                    "type": food_type,
                    "text": doc,
                })
                print(f"- {food_name} (Region: {food_region}, Type: {food_type})")
        except Exception:
            continue

    if not top_docs:
        return "I could not find relevant food information in the database."

    context = "\n".join(top_docs)

    prompt = f"""Use the following context to answer the question.

Context:
{context}

Question: {question}

Answer clearly and naturally based only on the retrieved food information.
"""

    try:
        response = groq_client.chat.completions.create(
            model=LLM_MODEL,
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

        answer = response.choices[0].message.content.strip()
        elapsed = time.time() - start_time
        print(f"\nRetrieval + generation time: {elapsed:.2f} seconds")
        return answer

    except Exception as e:
        return f"Error generating answer from Groq: {e}"

upload_data()

print("\nStarting Cloud RAG System — 🧠 RAG ready, 🤖 AI ready...\n")

while True:
    question = input("Ask a question (or type 'exit'): ").strip()

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    if not question:
        print("Please enter a valid question.\n")
        continue

    answer = rag_query(question)
    print("\nAnswer from LLM 🤖:")
    print(answer)
    print()