from infrastructure.article_factories import ArticleFactoryNewsApi
from infrastructure.fetch_api_settings_factories import FetchApiSettingsFactoryJson
from infrastructure.translation_controller_adapters import TranlationControllerRapidApi
from domain.models import DependencyInjection
from domain.models import Injection


class CoreBridgeAdapter:
    def __init__(self):
        self.adapters = {
            "article_factory_newsapi": ArticleFactoryNewsApi(),
            "fetch_api_settings_factory_json": FetchApiSettingsFactoryJson(),
            "translation_controller_rapidapi": TranlationControllerRapidApi(),
        }

    def get_injection(self, dependency_injection: DependencyInjection) -> Injection:
        return Injection(
            self.adapters[dependency_injection.article_factory],
            self.adapters[dependency_injection.fetch_api_settings_factory],
            self.adapters[dependency_injection.translation_controller],
        )