from app.services.llm import GroqLLM

llm = GroqLLM()


def rewrite(question, history):

    if not history:
        return question

    conversation = ""

    for message in history:
        conversation += (
            f"{message.role}: {message.content}\n"
        )

    prompt = f"""
You are a query rewriting assistant.

Given the conversation below, rewrite ONLY the latest user question into a
standalone search query.

Conversation:

{conversation}

Latest Question:
{question}

Return ONLY the rewritten query.
"""

    return llm.simple_generate(prompt).strip()