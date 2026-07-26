import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class GroqLLM:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.model = "llama-3.3-70b-versatile"

    def simple_generate(self, prompt):

        response = self.client.chat.completions.create(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0

        )

        return response.choices[0].message.content

    def stream_generate(self, prompt):

        stream = self.client.chat.completions.create(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0,

            stream=True

        )

        for chunk in stream:

            if (
                chunk.choices
                and chunk.choices[0].delta.content
            ):

                yield chunk.choices[0].delta.content

    def generate_answer(
        self,
        question,
        context,
        history=None
    ):

        if history is None:

            history = []

        conversation = ""

        for message in history:

            conversation += (
                f"{message.role.capitalize()}: "
                f"{message.content}\n"
            )

        prompt = f"""
You are an AI assistant.

Use the conversation history if it helps answer the user's latest question.

Answer ONLY using the context below.

=========================
Conversation History
=========================

{conversation}

=========================
Document Context
=========================

{context}

=========================
Current Question
=========================

{question}

If the answer is not present in the document context, reply exactly:

"I couldn't find that information in the uploaded documents."
"""

        return self.simple_generate(prompt)

    def stream_answer(
        self,
        question,
        context,
        history=None
    ):

        if history is None:

            history = []

        conversation = ""

        for message in history:

            conversation += (
                f"{message.role.capitalize()}: "
                f"{message.content}\n"
            )

        prompt = f"""
You are an AI assistant.

Use the conversation history if it helps answer the user's latest question.

Answer ONLY using the context below.

=========================
Conversation History
=========================

{conversation}

=========================
Document Context
=========================

{context}

=========================
Current Question
=========================

{question}

If the answer is not present in the document context, reply exactly:

"I couldn't find that information in the uploaded documents."
"""

        return self.stream_generate(prompt)