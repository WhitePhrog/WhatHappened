from domain.models import Article
from domain.models import ApiSettings

class ArticleFactory:
    def call(
        self,
        api_settings: ApiSettings,
        language: str
    ) -> Article:
        raise NotImplementedError
