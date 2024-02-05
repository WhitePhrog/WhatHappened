from domain.models import Article
from domain.services.factories import ArticleFactory

class GetArticle:
    def __init__(
        self,
        article_factory: ArticleFactory,
    ):
        self.article_factory = article_factory
    
    def call(self,
             api_settings,
             language
    ) -> Article:
        return self.article_factory.call(api_settings, language)