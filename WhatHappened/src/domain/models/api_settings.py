from dataclasses import dataclass

@dataclass
class ApiSettings:
    url: str
    headers: dict
    params: dict = {}