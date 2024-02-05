import time
from logging_config import logger
from domain.models.article import Article
from domain.usecases.get_article import GetArticle
from domain.usecases.get_api_settings import GetApiSettings
from domain.usecases.get_injection import GetInjection
from domain.services.controllers.translation_controller import TranslationController
from infrastructure.core_bridge_adapters import CoreBridgeAdapter
from infrastructure.core_dependency_injection_factories import CoreDependencyInjectionFactoryJson

def TranslateArticleGroup(source_language, target_language) -> Article:
    start_time = time.time()
    
    core_dependency_injection_factory = CoreDependencyInjectionFactoryJson()
    core_bridge = CoreBridgeAdapter()
    get_injection = GetInjection(
        core_bridge, core_dependency_injection_factory
    )
    injection = get_injection.call()

    translation_path = r"C:\Users\Octávio\Desktop\WhatHappened\WhatHappened\utils\translation_api_settings.json"
    news_path = r"C:\Users\Octávio\Desktop\WhatHappened\WhatHappened\utils\news_api_settings.json"

    get_api_settings = GetApiSettings(
        injection.fetch_api_settings_factory
    )
    
    get_article = GetArticle(
        injection.article_factory
    )
    
    translation_controller = TranslationController(
        injection.translation_controller
    )
    
    settings_time_start = time.time()
    translation_settings = get_api_settings.call(translation_path)
    news_settings = get_api_settings.call(news_path)
    settings_time_end = time.time()
    
    logger.info(f"Time taken to fetch API settings: {settings_time_end - settings_time_start} seconds")
    
    getting_article_start = time.time()
    untranslated_article = get_article.call(news_settings, source_language)
    getting_article_end = time.time()
    
    logger.info(f"Time taken to fetch the article: {getting_article_end - getting_article_start} seconds")
    logger.info(f"Untranslated Article:\n{untranslated_article}")
    
    translating_article_start = time.time()
    translated_article = translation_controller.call(translation_settings, untranslated_article, target_language)
    translating_article_end = time.time()
    
    logger.info(f"Time taken for translation: {translating_article_end - translating_article_start} seconds")
    logger.info(f"Translated Article:\n{translated_article}")
    
    end_time = time.time()
    logger.info(f"Total time for translation process: {end_time - start_time} seconds")
    
    return translated_article