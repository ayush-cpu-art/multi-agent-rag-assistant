function AgentStatus({ loading }) {

    if (!loading) return null;

    return (

        <div className="agent-panel">

            <div className="agent-item">
                🧠 <strong>Planner</strong>
                <span>Understanding question...</span>
            </div>

            <div className="agent-item">
                📚 <strong>Retriever</strong>
                <span>Searching documents...</span>
            </div>

            <div className="agent-item">
                🤖 <strong>LLM</strong>
                <span>Generating answer...</span>
            </div>

            <div className="agent-item">
                🧐 <strong>Critic</strong>
                <span>Reviewing response...</span>
            </div>

        </div>

    );

}

export default AgentStatus;