from stanfordkarel import *
from time import sleep


class ktools:
 def m(self):
  """Shorthand for Move"""
  move()

 def tl(self):
  """Turn left"""
  turn_left() 

 def tr(self):
  """Turn Right"""
  self.tl()
  self.tl()
  self.tl()

 def ta(self):
    """Turn around"""
    self.tl()
    self.tl()

 def pick(self):
      """Pickbeeper"""
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
      self.put2
      self.m()
      self.put()


  def h(self):
    
      def fic(self) -> bool:
        """Front is clear"""
      return front_is_clear()

  def fib(self) -> bool:
      """Front is Blocked"""
      return not self.fic()

  def ric(self) -> bool:
      """Right is Clear"""
      self.tr()
      if self.fic():
        self.tl()
        return True 
      self.tl()
      return False

  def rib(self) -> bool:
     """right is block"""
    return not self.ric()


  def mazemove(self):
      """Maze Move"""
    if self.fib():
      self.tf()
    else:
      self.m()
    if self.ric():
      self.tr()
      self.m()
    if self.ric():
      self.tr()
      self.m()
    pass

  def mm(self, num):
      """Move Multiple"""
      for number in range(0, num):
        self.m()


  def putm(self, num):
    """Put Multiple"""
    for i in range(num - 1):
      self.put()
      self.m()
      self.put()


  def pickm(self, num):
        """Pick Multiple"""
        for _ in range(num - 1):
          self.pick()
          self.m()
          self.pick()
          

  def SOB(self):
        """Standing on Beeper"""
        return beepers_present()
        

  def jump(self):
           """Jump for 510"""
           while self.fic():
             self.m()
           self.tl()
           while self.rib():
              self.m()
           self.tr()
           self.m()
           self.tr()
            while self.fic():
              self.m()
              self.tl()

  def find(self):
                """Find for 515"""
                while not facing_north():
                  self.tl()
                  self.m()
                  if not self.SOB():
                    self.tl()
                    self.m()
                    self.tl()
                    self.m()
                  for _ in range(2):
                    if not self.SOB():
                      self.m()
                      self.tl()
                      self.m()
                      
                  pass
      

 def main():
    """ Karel code goes here! """
   kt = ktools()
    kt.m()
    kt.tl()
    kt.m()
    kt.tr()
    kt.m() 
    while kt.SOB():
      kt.pick()
      kt.find()
    

    
    
    pass


if __name__ == "__main__":
    run_karel_program()