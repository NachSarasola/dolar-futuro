import math
from apps.backend.utils.rates import rc, tna


def test_rc_tna():
  f = 110.0
  s = 100.0
  d = 30
  assert rc(f, s, d) == math.log(f / s) * 365 / d
  assert tna(f, s, d) == (f / s - 1) * (365 / d) * 100
