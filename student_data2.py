class student:
  def __init__ (self, name, course, gender):
    print "New student entry has been created"
    self.name = name
    self.course = course
    self.gender = gender
    
  def __str__ (self):
    return "% studies % and is %" % (self.name, self.course, self.gender)
    
  def __del__ (self):
    print "Student is nolonger in school"
    
Peninah = student ("Peninah", "Business infomatics", "Female")

print student
del student


