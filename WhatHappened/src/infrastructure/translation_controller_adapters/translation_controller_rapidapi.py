from domain.models import Article
from domain.models import ApiSettings
from domain.services.controllers import TranslationController
import requests


class TranlationControllerRapidApi(TranslationController):
    def call(self,
             api_settings: ApiSettings,
             article: Article,
             target_language: str,
             ) -> Article:
        
        self.article = article
        self.api_settings = api_settings
        url = api_settings.url
        headers = api_settings.headers
        
        translation_target = f"{article.title}!@#${article.description}"
        
        payload = {
            "source_language": "auto",
            "target_language": target_language,
            "text": translation_target
        }
        
        raw = requests.post(url, headers=headers, payload=payload)
        raw_json = raw.json()
        
        title, description = raw_json['data']['translatedText'].split("!@#$", 1)
        
        return Article(
            title,
            description,
            article.source,
            article.url,
            article.date,
            article.language,
        )