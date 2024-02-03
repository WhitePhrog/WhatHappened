from dataclasses import dataclass

@dataclass
class Article:
    title: str
    description: str
    source: str
    url: str
    date: str
    original_language: str
     