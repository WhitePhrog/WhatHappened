from domain.models.article import Article

class ArticleFactory:
    def call(
        self,
        article: Article
    ) -> Article:
        raise NotImplementedError
