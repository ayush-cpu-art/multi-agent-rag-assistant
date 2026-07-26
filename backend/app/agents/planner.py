from app.agents.state import AgentState


def planner(state: AgentState):

    print("\n🧠 Planner Agent")

    question = state["question"].lower()

    if any(word in question for word in [
        "compare",
        "difference",
        "versus",
        "vs"
    ]):

        plan = (
            "Retrieve multiple relevant chunks and compare them "
            "before generating the answer."
        )

    else:

        plan = (
            "Retrieve the most relevant document chunks and answer "
            "using only the uploaded documents."
        )

    print("Plan:", plan)

    state["plan"] = plan

    return state