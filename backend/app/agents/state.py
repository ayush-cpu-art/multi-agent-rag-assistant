from typing import TypedDict, List


class AgentState(TypedDict):

    question: str

    history: list

    plan: str

    rewritten_query: str

    documents: List[dict]

    context: str

    answer: str

    sources: List[str]