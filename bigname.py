from stanfordkarel import *


class ktools:
  def m(self):
    """Shorthand for Move"""
    move()

  def tl(self):
    """Turn Left"""
    turn_left()

  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """Turn Around"""
    self.tl()
    self.tl()

  def pick(self):
    """Pick Beeper"""
    pick_beeper()

  def put(self):
    """Put Beeper"""
    put_beeper()

  def put2(self):
    """Put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """Put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def h(self):
    """Print H using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()

  def fic(self) -> bool:
    """Front is Clear"""
    return front_is_clear()

  def fib(self) -> bool:
    """Front is Blocked"""
    return not self.fic()

  def ric(self) -> bool:
    """Right is Clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True  # Immediately exit the function
    self.tl()
    return False

  def rib(self) -> bool:
    """Right is Blocked"""
    return not self.ric()

  def mazemove(self):
    """Maze Move"""
    if self.fib():
      self.tl()
    else:  # Otherwise...
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr()
          self.m()

  def g(self):
      self.m()
      self.put2()
      self.m()
      self.tl()
      self.m()
      self.put()
      self.m()
      self.tl()
      self.m()
      self.put()
      self.m()
      self.tl()
      self.m()
      self.tr()
      self.m()
      self.put()
      self.tr()
      self.m()
      self.put()
      self.m()
      self.put()
      self.m()
      self.tr()
      self.m()
      self.put()
      self.m()
      self.put()
      self.m()
      self.m()
      self.tr()
      self.m()
      self.m()
      self.m()
      self.m()
      self.tl()
      self.m()
      
  def a(self):
      self.tl()
      self.put5()
      self.tr()
      self.m()
      self.put()
      self.m()
      self.put()
      self.m()
      self.tr()
      self.put2()
      self.m()
      self.put()
      self.tr()
      self.m()
      self.put()
      self.m()
      self.put()
      self.tl()
      self.m()
      self.tl()
      self.m()
      self.m()
      self.put()
      self.tr()
      self.m()
      self.put()
      self.tl()
      self.m()
      self.m()
      
  def v(self):
    self.tl()
    self.m()
    self.m()
    self.m()
    self.put()
    self.tr()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.tl()
    self.m()
    self.tr()
    self.m()
    self.put()

def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.g()
    kt.a()
    kt.v()
    pass


if __name__ == "__main__":
    run_karel_program()