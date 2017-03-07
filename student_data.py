class student (object):
  # the class student will represent all students involved
  def __init__ (self, name, course):
    self.name = name
    self.course = course
    
  def getName (self):
    return self.name
    
  def getCourse (self):
    return self.course
    
  def __str__ (self):
    return "%s studies %s" % (self.name, self.course)
    
    Peninah = student ("Peninah","Business Infomatics" )
  
    print (Peninah.__str__())
  