import { useState } from "react";
import api from "../services/api";

function Upload() {

    const [file, setFile] = useState(null);
    const [status, setStatus] = useState("");

    const uploadFile = async () => {

        if (!file) {
            alert("Select a file first");
            return;
        }

        const formData = new FormData();

        formData.append("file", file);

        try {

            const res = await api.post(
                "/upload",
                formData
            );

            setStatus(res.data.message);

        } catch (err) {

            console.log(err);

            setStatus("Upload Failed");

        }

    };

    return (

        <div>

            <input
                type="file"
                onChange={(e) =>
                    setFile(e.target.files[0])
                }
            />

            <button onClick={uploadFile}>
                Upload
            </button>

            <p>{status}</p>

        </div>

    );

}

export default Upload;