import { useState } from "react";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

import toast from "react-hot-toast";

import api from "../services/api";
import ChunkModal from "./ChunkModal";

function Message({ sender, text, sources = [] }) {

    const [open, setOpen] = useState(false);

    const [chunk, setChunk] = useState({});

    const copyMessage = async () => {

        try {

            await navigator.clipboard.writeText(text);

            toast.success("Copied to clipboard!");

        }

        catch (error) {

            console.error(error);

            toast.error("Failed to copy.");

        }

    };

    const openSource = async (source) => {

        try {

            const match = source.match(
                /(.*)\s+\(Chunk\s+(\d+)\)/i
            );

            if (!match) {

                toast.error("Invalid source.");

                return;

            }

            const document = match[1];

            const chunkId = match[2];

            const response = await api.get(

                `/documents/${encodeURIComponent(document)}/chunk/${chunkId}`

            );

            setChunk(response.data);

            setOpen(true);

        }

        catch (error) {

            console.error(error);

            toast.error("Unable to load source.");

        }

    };

    return (

        <>

            <div
                className={
                    sender === "user"
                        ? "user-msg"
                        : "ai-msg"
                }
            >

                <div className="message-header">

                    <h3>

                        {
                            sender === "user"
                                ? "🧑 You"
                                : "🤖 AI"
                        }

                    </h3>

                    {

                        sender === "ai" && (

                            <button
                                className="copy-btn"
                                onClick={copyMessage}
                            >

                                📋 Copy

                            </button>

                        )

                    }

                </div>

                <div className="message-content">

                    <ReactMarkdown
                        remarkPlugins={[remarkGfm]}
                    >

                        {text}

                    </ReactMarkdown>

                </div>

                {

                    sender === "ai" &&
                    sources.length > 0 && (

                        <div className="sources">

                            <h4>📄 Sources</h4>

                            {

                                sources.map((source, index) => (

                                    <div

                                        key={index}

                                        className="source-card"

                                        onClick={() => openSource(source)}

                                    >

                                        {source}

                                    </div>

                                ))

                            }

                        </div>

                    )

                }

            </div>

            <ChunkModal

                open={open}

                onClose={() => setOpen(false)}

                chunk={chunk}

            />

        </>

    );

}

export default Message;