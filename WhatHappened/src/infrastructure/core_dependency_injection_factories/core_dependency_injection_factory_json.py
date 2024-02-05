from domain.models import DependencyInjection
from domain.services.factories import CoreDependencyInjectionFactory
import json


class CoreDependencyInjectionFactoryJson(CoreDependencyInjectionFactory):
    def call(self) -> DependencyInjection:
        with open(
            "C:\Users\Octávio\Desktop\WhatHappened\WhatHappened\utils\dependency_injections.json",
            "r",
        ) as f:
            dependency_injections = json.load(f)
            return DependencyInjection(
                dependency_injections["article_factory"],
                dependency_injections["fetch_api_settings_factory"],
                dependency_injections["translation_controller"],
            )