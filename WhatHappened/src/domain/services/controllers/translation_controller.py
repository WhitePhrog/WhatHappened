from domain.models import Article
from domain.models import ApiSettings

class TranslationController:
    def translate_article(self,  api_settings: ApiSettings, article: Article, target_language: str,) -> Article:
        raise NotImplementedError
        