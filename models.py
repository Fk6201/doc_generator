from dataclasses import dataclass
from typing import Optional

@dataclass
class ReportItem:
    title: str
    summary: str
    value: Optional[float] = None
