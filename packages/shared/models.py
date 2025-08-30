from typing import List, Optional
from pydantic import BaseModel


class Quote(BaseModel):
  symbol: str
  last: float
  bid: Optional[float] = None
  ask: Optional[float] = None
  oi: Optional[int] = None
  volume: Optional[int] = None


class Signal(BaseModel):
  symbol: str
  score: float
  rc: float
  tna: float
  basis: Optional[float] = None
  flags: List[str] = []


class Sizing(BaseModel):
  symbol: str
  qty: int
  margin: float


class OrderTicket(BaseModel):
  symbol: str
  side: str
  qty: int
  price: float
  tif: str = "DAY"
  dry_run: bool = True
