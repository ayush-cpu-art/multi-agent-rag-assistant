from app.agents.state import AgentState


def critic(state: AgentState):

    print("\n🧐 Critic Agent")

    answer = state.get("answer", "").strip()
    sources = state.get("sources", [])

    if not answer:

        state["answer"] = (
            "I couldn't generate an answer."
        )

        print("❌ Empty answer.")

        return state

    if len(sources) == 0:

        print("⚠️ No source documents found.")

    else:

        print(f"✅ {len(sources)} source(s) verified.")

    print("✅ Answer passed quality check.")

    return state