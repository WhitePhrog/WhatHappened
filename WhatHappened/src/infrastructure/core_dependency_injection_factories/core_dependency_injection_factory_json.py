from domain.models import DependencyInjection
from domain.services.factories import CoreDependencyInjectionFactory
import json


class CoreDependencyInjectionFactoryJson(CoreDependencyInjectionFactory):
    def call(self) -> DependencyInjection:
        with open(
            "C:\Users\Octávio\Desktop\TermInv\TermInv\utils\dependency_injections.json",
            "r",
        ) as f:
            dependency_injections = json.load(f)
            return DependencyInjection(
                dependency_injections["database_connection_factory"],
                dependency_injections["database_controller_factory"],
                dependency_injections["database_controller"],
                dependency_injections["inventory_factory"],
                dependency_injections["inventory_repository"],
                dependency_injections["item_factory"],
                dependency_injections["item_repository_mysql"],
            )