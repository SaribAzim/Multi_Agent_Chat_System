from dataclasses import dataclass
from datetime import datetime

@dataclass
class MemoryRecord:
    timestamp: str
    topic: str
    content: str
    source: str
    agent: str
    confidence: float
