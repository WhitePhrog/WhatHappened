from domain.services.controllers import *
from domain.services.factories import *
from dataclasses import dataclass

@dataclass
class Injection:
    article_factory: ArticleFactory
    fetch_api_settings_factory: FetchApiSettingsFactory
    translation_controller: TranslationController
