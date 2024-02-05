from domain.models import Article
from domain.models import ApiSettings

class TranslationController:
    def translate_article(self, article: Article, target_language: str, api_settings: ApiSettings) -> Article:
        raise NotImplementedError
        