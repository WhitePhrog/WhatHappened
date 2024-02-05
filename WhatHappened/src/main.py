from fastapi import FastAPI

from entrypoints.routes.translate_article import translation_router

app = FastAPI()

app.include_router(translation_router)