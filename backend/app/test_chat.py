from app.rag.retriever import Retriever
from app.services.llm import GroqLLM

retriever = Retriever()
llm = GroqLLM()

question = input("Ask a question: ")

chunks = retriever.retrieve(question)

context = "\n\n".join(chunks)

answer = llm.generate_answer(question, context)

print("\n")
print("=" * 60)
print(answer)