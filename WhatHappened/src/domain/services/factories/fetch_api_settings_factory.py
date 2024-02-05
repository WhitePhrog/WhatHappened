from domain.models import ApiSettings

class FetchApiSettingsFactory:
    def call(
        self,
        path
    ) -> ApiSettings:
        raise NotImplementedError