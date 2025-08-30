import math


def rc(fut: float, spot: float, days: int) -> float:
  """Continuous implied rate."""
  return math.log(fut / spot) * 365 / days


def tna(fut: float, spot: float, days: int) -> float:
  """Tasa nominal anual (lineal) en %."""
  return (fut / spot - 1) * (365 / days) * 100
