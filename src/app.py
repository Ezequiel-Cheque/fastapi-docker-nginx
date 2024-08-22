import logging
from os import getenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from .controller.main_controller import main_controller

load_dotenv()

def app() -> FastAPI:
    
    app = FastAPI(
        redoc_url=None,
        title="Example App",
        description="Example app to test jenkins",
        version=getenv("VERSION"),
        openapi_url='/openapi.json',
        docs_url="/swagger",
        root_path="/api"
    )

    app.include_router(main_controller)

    return app


create_app = app()