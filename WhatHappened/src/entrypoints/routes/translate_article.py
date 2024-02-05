from dataclasses import asdict
from fastapi import APIRouter
from domain.groups.translate_article import TranslateArticleGroup

translation_router = APIRouter()

@translation_router.get("/translate-article/{source_language}/{target_language}")
def TranslateArticleRoute(source_language, target_language):
    translated_article = TranslateArticleGroup(source_language, target_language)
    return asdict(translated_article)
