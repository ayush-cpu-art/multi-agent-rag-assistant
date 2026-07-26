import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import { Toaster } from "react-hot-toast";

import "./index.css";
import App from "./App.jsx";

createRoot(
    document.getElementById("root")
).render(

    <StrictMode>

        <App />

        <Toaster

            position="top-right"

            reverseOrder={false}

            toastOptions={{

                duration: 3000,

                style: {

                    background: "#1f2937",

                    color: "#fff",

                    borderRadius: "12px",

                    padding: "12px"

                }

            }}

        />

    </StrictMode>

);