import axios from "axios";

const api = axios.create({
    baseURL: "https://multi-agent-rag-assistant-v2.onrender.com",
});

export default api;