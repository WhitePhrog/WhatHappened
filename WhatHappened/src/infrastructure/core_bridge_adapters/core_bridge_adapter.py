from infrastructure.database_controller_factories.database_controller_factory_mysql import DatabaseControllerFactoryMySQL
from infrastructure.database_controllers.database_controller_mysql import DatabaseControllerMySQL
from infrastructure.database_connection_factories.database_connection_factory_mysql import DatabaseConnectionFactoryMySQL
from infrastructure.inventory_factories import InventoryFactoryFromInput
from infrastructure.inventory_repositories import InventoryRepositoryMySQL
from infrastructure.item_factories import ItemFactoryFromInput
from infrastructure.item_repositories import ItemRepositoryMySQL
from domain.models import DependencyInjection
from domain.models import Injection


class CoreBridgeAdapter:
    def __init__(self):
        self.adapters = {
            "database_connection_factory_mysql": DatabaseConnectionFactoryMySQL(),
            "database_controller_factory_mysql": DatabaseControllerFactoryMySQL(),
            "database_controller_mysql": DatabaseControllerMySQL(),
            "inventory_factory_input": InventoryFactoryFromInput(),
            "inventory_repository_mysql": InventoryRepositoryMySQL(),
            "item_factory_input": ItemFactoryFromInput(),
            "item_repository_mysql": ItemRepositoryMySQL(),
        }

    def get_injection(self, dependency_injection: DependencyInjection) -> Injection:
        return Injection(
            self.adapters[dependency_injection.database_connection_factory],
            self.adapters[dependency_injection.database_controller_factory],
            self.adapters[dependency_injection.database_controller],
            self.adapters[dependency_injection.inventory_factory],
            self.adapters[dependency_injection.inventory_repository],
            self.adapters[dependency_injection.item_factory],
            self.adapters[dependency_injection.item_repository],
        )