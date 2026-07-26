import os
import fitz
from docx import Document


class DocumentLoader:

    @staticmethod
    def load_pdf(file_path):

        text = ""

        with fitz.open(file_path) as pdf:

            for page in pdf:
                page_text = page.get_text()

                if page_text:
                    text += page_text + "\n"

        return text.strip()

    @staticmethod
    def load_docx(file_path):

        document = Document(file_path)

        text = "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
            if paragraph.text.strip()
        )

        return text.strip()

    @staticmethod
    def load_txt(file_path):

        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            return file.read().strip()

    @staticmethod
    def load_document(file_path):

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":

            text = DocumentLoader.load_pdf(file_path)

        elif extension == ".docx":

            text = DocumentLoader.load_docx(file_path)

        elif extension == ".txt":

            text = DocumentLoader.load_txt(file_path)

        else:

            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        print("\n" + "=" * 60)
        print("📄 DOCUMENT LOADED")
        print("=" * 60)
        print("File :", os.path.basename(file_path))
        print("Characters :", len(text))
        print("\nFirst 500 characters:\n")
        print(text[:500])
        print("=" * 60 + "\n")

        return text