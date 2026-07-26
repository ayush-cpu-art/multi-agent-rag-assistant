import { useState, useEffect, useRef } from "react";
import { jsPDF } from "jspdf";
import toast from "react-hot-toast";

import api from "../services/api";
import Message from "./Message";

function Chat() {

    const [question, setQuestion] = useState("");
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);

    const messagesEndRef = useRef(null);

    useEffect(() => {

        messagesEndRef.current?.scrollIntoView({
            behavior: "smooth"
        });

    }, [messages, loading]);

    const typeMessage = (fullText, callback) => {

        let index = 0;

        let current = "";

        const interval = setInterval(() => {

            current += fullText[index];

            callback(current);

            index++;

            if (index >= fullText.length) {

                clearInterval(interval);

            }

        }, 15);

    };

    const exportMarkdown = () => {

        if (messages.length === 0) {

            toast.error("No conversation to export.");

            return;

        }

        let markdown = "# Multi-Agent RAG Conversation\n\n";

        messages.forEach((msg) => {

            markdown += `## ${msg.sender === "user" ? "You" : "AI"}\n\n`;

            markdown += `${msg.text}\n\n`;

            if (msg.sources?.length) {

                markdown += "### Sources\n";

                msg.sources.forEach((source) => {

                    markdown += `- ${source}\n`;

                });

                markdown += "\n";

            }

        });

        const blob = new Blob(

            [markdown],

            {
                type: "text/markdown"
            }

        );

        const url = URL.createObjectURL(blob);

        const a = document.createElement("a");

        a.href = url;

        a.download = "conversation.md";

        a.click();

        URL.revokeObjectURL(url);

        toast.success("Markdown exported.");

    };

    const exportPDF = () => {

        if (messages.length === 0) {

            toast.error("No conversation to export.");

            return;

        }

        const pdf = new jsPDF();

        let y = 20;

        pdf.setFontSize(18);

        pdf.text("Multi-Agent RAG Conversation", 15, y);

        y += 15;

        pdf.setFontSize(12);

        messages.forEach((msg) => {

            pdf.setFont(undefined, "bold");

            pdf.text(

                msg.sender === "user"
                    ? "You"
                    : "AI",

                15,

                y

            );

            y += 8;

            pdf.setFont(undefined, "normal");

            const lines = pdf.splitTextToSize(

                msg.text,

                175

            );

            pdf.text(lines, 15, y);

            y += lines.length * 7 + 10;

            if (y > 270) {

                pdf.addPage();

                y = 20;

            }

        });

        pdf.save("conversation.pdf");

        toast.success("PDF exported.");

    };

    const sendQuestion = async () => {

        if (!question.trim() || loading) return;

        const currentQuestion = question;

        setQuestion("");

        const updatedMessages = [

            ...messages,

            {

                sender: "user",

                text: currentQuestion

            }

        ];

        setMessages(updatedMessages);

        setLoading(true);

        try {

            const history = updatedMessages.map((msg) => ({

                role: msg.sender === "user"
                    ? "user"
                    : "assistant",

                content: msg.text

            }));

            const res = await api.post("/chat", {

                question: currentQuestion,

                history

            });

            const aiIndex = updatedMessages.length;

            setMessages((prev) => [

                ...prev,

                {

                    sender: "ai",

                    text: "",

                    sources: res.data.sources || []

                }

            ]);

            typeMessage(

                res.data.answer,

                (text) => {

                    setMessages((prev) => {

                        const copy = [...prev];

                        copy[aiIndex] = {

                            ...copy[aiIndex],

                            text

                        };

                        return copy;

                    });

                }

            );

        }

        catch (error) {

            console.error(error);

            toast.error("Failed to generate response.");

            setMessages((prev) => [

                ...prev,

                {

                    sender: "ai",

                    text: "Something went wrong.",

                    sources: []

                }

            ]);

        }

        finally {

            setLoading(false);

        }

    };

    const handleKeyDown = (e) => {

        if (e.key === "Enter") {

            sendQuestion();

        }

    };

    return (

        <div className="chat">

            <div
                style={{
                    display: "flex",
                    justifyContent: "flex-end",
                    gap: "10px",
                    marginBottom: "15px"
                }}
            >

                <button
                    onClick={exportMarkdown}
                >
                    📄 Markdown
                </button>

                <button
                    onClick={exportPDF}
                >
                    📑 PDF
                </button>

            </div>

            <div className="messages">

                {

                    messages.map((msg, index) => (

                        <Message

                            key={index}

                            sender={msg.sender}

                            text={msg.text}

                            sources={msg.sources}

                        />

                    ))

                }

                {

                    loading && (

                        <Message

                            sender="ai"

                            text="🤖 Thinking..."

                            sources={[]}

                        />

                    )

                }

                <div ref={messagesEndRef}></div>

            </div>

            <div className="input-area">

                <input

                    value={question}

                    onChange={(e) =>
                        setQuestion(e.target.value)
                    }

                    onKeyDown={handleKeyDown}

                    placeholder="Ask anything about your document..."

                    disabled={loading}

                />

                <button

                    onClick={sendQuestion}

                    disabled={loading}

                >

                    {

                        loading

                            ? "Thinking..."

                            : "Send"

                    }

                </button>

            </div>

        </div>

    );

}

export default Chat;