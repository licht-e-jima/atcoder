from datetime import datetime
from dataclasses import dataclass
from typing import List

@dataclass
class Query:
    time: datetime
    query_type: str
    arguments: List[str]
