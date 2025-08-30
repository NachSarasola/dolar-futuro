import random
from packages.shared import Quote
from .base import Feed


class DemoFeed(Feed):
  """Deterministic feed with noise for tests."""

  def __init__(self, seed: int = 42):
    self._rnd = random.Random(seed)

  def get_quote(self, symbol: str) -> Quote:
    price = 100 + self._rnd.random()
    return Quote(
      symbol=symbol,
      last=price,
      bid=price - 0.1,
      ask=price + 0.1,
      oi=1000,
      volume=500,
    )
