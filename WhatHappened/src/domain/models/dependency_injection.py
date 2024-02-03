from dataclasses import dataclass

@dataclass
class DependencyInjection:
    database_connection_factory: str
    database_controller_factory: str
    database_controller: str
    inventory_factory: str
    inventory_repository: str
    item_factory: str
    item_repository: str
     