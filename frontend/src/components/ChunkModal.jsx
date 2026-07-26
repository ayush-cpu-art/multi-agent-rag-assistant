import "./ChunkModal.css";

function ChunkModal({ open, onClose, chunk }) {

    if (!open) return null;

    return (

        <div
            className="modal-overlay"
            onClick={onClose}
        >

            <div
                className="modal"
                onClick={(e) => e.stopPropagation()}
            >

                <div className="modal-header">

                    <h2>📄 {chunk.document}</h2>

                    <button
                        className="close-btn"
                        onClick={onClose}
                    >
                        ✖
                    </button>

                </div>

                <p>

                    <strong>Chunk:</strong> {chunk.chunk_id}

                </p>

                <hr />

                <div className="chunk-content">

                    {chunk.text}

                </div>

            </div>

        </div>

    );

}

export default ChunkModal;