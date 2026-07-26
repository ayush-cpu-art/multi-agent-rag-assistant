import os

from qdrant_client import QdrantClient


ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

DB_PATH = os.path.join(
    ROOT_DIR,
    "qdrant_db"
)


client = QdrantClient(
    path=DB_PATH
)