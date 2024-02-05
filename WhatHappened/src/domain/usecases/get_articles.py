from domain.models import Article
from domain.services.factories import ArticleFactory

class GetArticle:
    def __init__(
        self,
        article_factory: ArticleFactory,
    ):
        self.article_factory = article_factory
    
    def call(self,
             title: str,
             description: str,
             source: str,
             url: str,
             date: str,
             original_language: str,
    ) -> Article:
        return self.article_factory.call(title, description, source, url, date, original_language)