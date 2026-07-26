from app.agents.state import AgentState
from app.services.llm import GroqLLM

llm = GroqLLM()


def answer(state: AgentState):

    print("\n🤖 Answer Agent")
    print(f"Context Length: {len(state['context'])} characters")

    response = llm.generate_answer(
        question=state["question"],
        context=state["context"],
        history=state.get("history", [])
    )

    state["answer"] = response

    print("✅ Answer generated.")

    return state