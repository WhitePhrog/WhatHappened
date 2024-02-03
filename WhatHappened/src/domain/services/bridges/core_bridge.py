from domain.models import DependencyInjection
from domain.models import Injection

class CoreBridge:
    def get_injection(self, dependency_injection: DependencyInjection) -> Injection:
        raise NotImplementedError()