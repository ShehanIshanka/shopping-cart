from typing import Optional

from src.base.infra.http import Request


class CreatProductPostRequestSchema(Request):
    name: str
    amount: float
    description: Optional[str] = None
