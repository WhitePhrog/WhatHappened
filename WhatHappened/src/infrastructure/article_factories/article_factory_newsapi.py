from domain.models import Article
from domain.models import ApiSettings
from domain.services.factories import ArticleFactory
import requests


class ArticleFactoryNewsApi(ArticleFactory):
    def call(self,
             api_settings: ApiSettings,
             language: str,
             ) -> Article:
        
        self.api_settings = api_settings
        url = api_settings.url
        headers = api_settings.headers
        params = {
            "q": '',
            'language': f'{language}',
            'pageSize': 1
        }
        
        raw = requests.get(url, headers=headers, params=params)
        raw_json = raw.json()
        
        url = raw_json['articles'][0]['title']
        if raw_json['articles'][0]['description'] != None:
            description = raw_json['articles'][0]['description']    
        else:
            description = "None"
        source = raw_json['articles']['0']['source']['name']
        title = raw_json['articles']['0']['title']
        date = raw_json['articles']['0']['publishedAt']
        
        
        return Article(
            title,
            description,
            source,
            url,
            date,
            language,
        )