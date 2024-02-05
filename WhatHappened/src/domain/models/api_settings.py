from dataclasses import dataclass, field
from typing import Dict

@dataclass
class ApiSettings:
    url: str
    headers: Dict[str, str] = field(default_factory=dict)
    params: Dict[str, str] = field(default_factory=dict)