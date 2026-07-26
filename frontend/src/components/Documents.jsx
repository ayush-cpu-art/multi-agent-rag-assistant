import { useEffect, useState } from "react";
import api from "../services/api";

function Documents() {

    const [documents, setDocuments] = useState([]);

    useEffect(() => {

        fetchDocuments();

    }, []);

    const fetchDocuments = async () => {

        try {

            const response = await api.get("/documents");

            console.log("📂 API Response:", response.data);

            if (response.data.documents) {

                setDocuments(response.data.documents);

            } else {

                setDocuments([]);

            }

        } catch (error) {

            console.error("❌ Failed to fetch documents:", error);

        }

    };

    const deleteDocument = async (documentName) => {

        const confirmed = window.confirm(
            `Delete "${documentName}"?`
        );

        if (!confirmed) return;

        const documentId = documentName
            .toLowerCase()
            .replace(".pdf", "")
            .split("(")[0]
            .trim();

        try {

            await api.delete(`/documents/${documentId}`);

            fetchDocuments();

        } catch (error) {

            console.error("❌ Delete failed:", error);

            alert("Failed to delete document.");

        }

    };

    return (

        <div className="documents">

            <h2>📂 Documents</h2>

            {

                documents.length === 0 ? (

                    <p>No documents uploaded.</p>

                ) : (

                    documents.map((doc) => (

                        <div
                            key={doc.name}
                            className="document-card"
                        >

                            <h4>📄 {doc.name}</h4>

                            <p>{doc.chunks} Chunks</p>

                            <button
                                onClick={() => deleteDocument(doc.name)}
                            >
                                🗑 Delete
                            </button>

                        </div>

                    ))

                )

            }

        </div>

    );

}

export default Documents;