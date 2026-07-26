from app.rag.retriever import Retriever
from app.agents.state import AgentState


def retrieve(state: AgentState):

    print("\n📚 Retriever Agent")

    # Create Retriever only when this function is called
    retriever = Retriever()

    query = state.get("rewritten_query") or state["question"]

    documents = retriever.retrieve(query)

    print(f"Retrieved {len(documents)} document(s)")

    context = "\n\n".join(
        doc["text"]
        for doc in documents
    )

    sources = []

    seen = set()

    for doc in documents:

        key = (
            doc["document"],
            doc["chunk_id"]
        )

        if key not in seen:

            seen.add(key)

            sources.append(
                f'{doc["document"]} (Chunk {doc["chunk_id"]})'
            )

    state["documents"] = documents
    state["context"] = context
    state["sources"] = sources

    return state