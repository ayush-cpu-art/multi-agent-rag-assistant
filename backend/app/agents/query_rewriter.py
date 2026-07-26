from app.services.llm import GroqLLM

llm = GroqLLM()


def rewrite(question, history):

    # No history -> use the original question
    if not history:
        print("\n[Query Rewriter] No history found.")
        print("Search Query:", question)
        return question

    conversation = ""

    for message in history:
        conversation += (
            f"{message.role.capitalize()}: {message.content}\n"
        )

    prompt = f"""
You are an expert query rewriting assistant.

Your task is to rewrite the latest user question into a complete,
standalone search query suitable for semantic vector search.

Conversation History:
{conversation}

Latest User Question:
{question}

Rules:
1. Resolve pronouns like "it", "they", "this", "that".
2. Preserve the original meaning.
3. Do NOT answer the question.
4. Return ONLY the rewritten query.
5. Do NOT add explanations, markdown, quotes, or extra text.

Rewritten Query:
"""

    try:

        rewritten_query = llm.simple_generate(prompt).strip()

        # Remove unwanted formatting if the LLM adds it
        rewritten_query = (
            rewritten_query
            .replace('"', "")
            .replace("Rewritten Query:", "")
            .replace("Query:", "")
            .strip()
        )

        print("\n==============================")
        print("🧠 QUERY REWRITER")
        print("==============================")
        print("Original Question :", question)
        print("Rewritten Query   :", rewritten_query)
        print("==============================\n")

        return rewritten_query

    except Exception as e:

        print("\nQuery Rewriter Error:", e)
        print("Falling back to original question.\n")

        return question