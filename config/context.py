import os

from dotenv import load_dotenv

context = os.getenv("CONTEXT", "bstack")

load_dotenv(f".env.{context}")
load_dotenv(".env.credentials")