from qdrant_client import QdrantClient
from promptflow import tool
from sentence_transformers import SentenceTransformer

@tool
def qdrant_doc_lookup(query: str) -> str:
    client = QdrantClient(host="localhost", port="6333")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    embeddings = model.encode([query])

    search_result = client.search(
        collection_name="documentation",
        query_vector=embeddings[0],
        limit=3
    )

    results = []
    for r in search_result:
        results.append({
            "id": r.id,
            "score": r.score,
            "text": r.payload["text"],
            "url": r.payload["url"],
            "titles": r.payload["titles"]
        })
    return results