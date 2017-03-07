class student (object):
  """the class student represents all the student entries"""
  def __init__ (self,name, course, fee_balance):
    self.name = name
    """the name is a public entry"""
    
    self.course = course
    """the course is a public entry"""
    
    self.__fee_balance = fee_balance
    """the fee balance is a prive entry"""
    
  def getName (self):
    return self.name
    
  def getCourse (self):
    return self.name
    
  def getFee_balance (self):
    return __fee_balance
    """this remains a private entry unless one specifies it's visibility during printing"""
  def __str__ (self):
    return "% studies %s and has a fee balance of %s" % (self.name, self.course, self.__fee_balance)

Peninah = student ("Peninah", "Business Infomatics", 20000)
    
 
print (Peninah.__str__())
  