from pydantic import BaseModel
from typing import List

class TransactionData(BaseModel):
    features: List[float]
