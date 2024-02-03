from domain.models.api_settings import ApiSettings

class FetchApiSettingsFactory:
    def call(
        self,
        api_settings: ApiSettings
    ) -> ApiSettings:
        raise NotImplementedError