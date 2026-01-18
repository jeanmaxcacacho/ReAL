"""
This file contains the most basic scripts to implement
naive retrieval augmented generation (RAG).

1. Receiving and chunking external data from user
2. Connecting to HuggingFace and obtaining embeddings
3. Performing RAG task and generating quiz items

In further iterations of this project, I intend to
turn this into a proper backend with FastAPI.
"""

from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ["HF_TOKEN"],
)

result = client.sentence_similarity(
    "Are you excited to study?",
    [
        "I want to prepare better for tests.",
        "I want to develop good study habits.",
        "I want to re-invent my perception of classroom lectures.",
    ],
    model="sentence-transformers/all-MiniLM-L6-v2",
)

print(result)