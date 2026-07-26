from langgraph.graph import StateGraph, END

from app.agents.state import AgentState
from app.agents.planner import planner
from app.agents.query_rewriter import rewrite
from app.agents.retriever_agent import retrieve
from app.agents.answer_agent import answer
from app.agents.critic_agent import critic


# ---------------------------
# Query Rewriter Node
# ---------------------------

def query_rewriter_node(state: AgentState):

    print("\n✍️ Query Rewriter Agent")

    rewritten_query = rewrite(
        state["question"],
        state.get("history", [])
    )

    state["rewritten_query"] = rewritten_query

    return state


# ---------------------------
# Build Graph
# ---------------------------

workflow = StateGraph(AgentState)

workflow.add_node("planner", planner)
workflow.add_node("query_rewriter", query_rewriter_node)
workflow.add_node("retriever", retrieve)
workflow.add_node("answer", answer)
workflow.add_node("critic", critic)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "query_rewriter")
workflow.add_edge("query_rewriter", "retriever")
workflow.add_edge("retriever", "answer")
workflow.add_edge("answer", "critic")
workflow.add_edge("critic", END)

graph = workflow.compile()