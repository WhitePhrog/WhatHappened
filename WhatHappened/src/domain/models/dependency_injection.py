from dataclasses import dataclass

@dataclass
class DependencyInjection:
    article_factory: str
    fetch_api_settings_factory: str
    translation_controller: str