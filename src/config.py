from dataclasses import dataclass

@dataclass
class Settings:
    api_key: str
    api_url: str
    timeout: int
    debug: bool