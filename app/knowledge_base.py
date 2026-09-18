from pathlib import Path
from typing import List, Dict


KNOWLEDGE_BASE = Path("knowledge_base")


def load_documents() -> List[Dict[str, str]]:
    documents = []

    for file in KNOWLEDGE_BASE.rglob("*.md"):
        documents.append({
            "name": file.name,
            "path": str(file),
            "content": file.read_text(encoding="utf-8")
        })

    return documents


def search_knowledge_base(query: str) -> List[Dict[str, str]]:
    documents = load_documents()

    query_words = set(query.lower().split())
    results = []

    for document in documents:
        content = document["content"].lower()

        score = sum(
            1 for word in query_words
            if len(word) > 2 and word in content
        )

        if score > 0:
            results.append({
                **document,
                "score": score
            })

    return sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )