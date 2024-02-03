from domain.models.api_settings import ApiSettings
from domain.services.factories.fetch_api_settings_factory import FetchApiSettingsFactory

class GetApiSettings:
    def __init__(self, fetch_api_settings_factory:FetchApiSettingsFactory):
        self.fetch_api_settings_factory = fetch_api_settings_factory
        
    def call(self, path) -> ApiSettings: