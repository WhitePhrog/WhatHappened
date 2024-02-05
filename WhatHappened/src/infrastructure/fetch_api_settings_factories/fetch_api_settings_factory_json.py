from domain.models import ApiSettings
from domain.services.factories import FetchApiSettingsFactory
import json

class FetchApiSettingsFactoryJson(FetchApiSettingsFactory):
    def call(self, path) -> ApiSettings:
        file = open(path, "r",)
        api_settings = json.load(file)
        return ApiSettings(
            api_settings["url"],
            api_settings["headers"],
            api_settings["params"],
        )