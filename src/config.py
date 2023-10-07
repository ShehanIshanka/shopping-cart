import os
from dataclasses import dataclass


@dataclass
class Config:
    db_url: str = os.environ.get("DB_URL", "")
