import { useEffect, useState } from "react";

import Upload from "./components/Upload";
import Chat from "./components/Chat";
import Documents from "./components/Documents";

import "./App.css";

function App() {

    const [theme, setTheme] = useState(

        localStorage.getItem("theme") || "dark"

    );

    useEffect(() => {

        document.body.className = theme;

        localStorage.setItem(
            "theme",
            theme
        );

    }, [theme]);

    const toggleTheme = () => {

        setTheme(

            theme === "dark"
                ? "light"
                : "dark"

        );

    };

    return (

        <div className="app">

            <aside className="sidebar">

                <Documents />

            </aside>

            <main className="main-content">

                <div className="header">

                    <div>

                        <h1>
                            🤖 Multi-Agent RAG Assistant
                        </h1>

                        <p className="subtitle">

                            AI-powered Multi-Document Assistant

                        </p>

                    </div>

                    <button

                        className="theme-btn"

                        onClick={toggleTheme}

                    >

                        {

                            theme === "dark"

                                ? "☀ Light"

                                : "🌙 Dark"

                        }

                    </button>

                </div>

                <Upload />

                <Chat />

            </main>

        </div>

    );

}

export default App;