from abc import ABC, abstractmethod
from packages.shared import Quote


class Feed(ABC):
  @abstractmethod
  def get_quote(self, symbol: str) -> Quote:
    """Return latest quote for symbol."""
    raise NotImplementedError
