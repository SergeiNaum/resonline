import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / "docker" / "env" / ".env"
load_dotenv(dotenv_path=env_path)

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
REDIS_DB = None if os.getenv("REDIS_DB") == "null" else os.getenv("REDIS_DB")
REDIS_CLIENT = (
    None if os.getenv("REDIS_CLIENT") == "null" else os.getenv("REDIS_CLIENT")
)
