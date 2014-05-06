class NegativeInfinity(object):
  def __eq__(self, other):
    return (type(other) == NegativeInfinity)

  def __lt__(self, other):
    if self == other:
      return False
    return True

  def __le__(self, other):
    return True

  def __gt__(self, other):
    return False

  def __ge__(self, other):
    return False

  def __hash__(self):
    return id(self)

class Infinity(object):
  def __eq__(self, other):
    return (type(other) == Infinity)

  def __lt__(self, other):
    return False

  def __le__(self, other):
    return False

  def __gt__(self, other):
    if other == self:
      return False
    return True

  def __ge__(self, other):
    return True

  def __hash__(self):
    return id(self)
