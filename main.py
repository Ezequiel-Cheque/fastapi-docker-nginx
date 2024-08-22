import os
import logging
import uvicorn
from pathlib import Path
from dotenv import load_dotenv
from src.app import *

load_dotenv()

if __name__ == "__main__":
    uvicorn.run(
        f"{Path(__file__).stem}:app",
        host=str(os.getenv("HOST", "0.0.0.0")),
        port=int(os.getenv("PORT", "4000")),
        reload=bool(os.getenv("RELOAD", False)),
        log_level="info",
        workers=int(os.getenv("WORKERS")),
        factory=False,
    )