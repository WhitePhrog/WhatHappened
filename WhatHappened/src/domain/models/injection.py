from domain.services.controllers import *
from domain.services.factories import *
from domain.services.repositories import *
from dataclasses import dataclass

@dataclass
class Injection:
    database_connection_factory: DatabaseConnectionFactory
    database_controller_factory: DatabaseControllerFactory
    database_controller: DatabaseController
    inventory_factory: InventoryFactory
    inventory_repository: InventoryRepository
    item_factory: ItemFactory
    item_repository: ItemRepository
    