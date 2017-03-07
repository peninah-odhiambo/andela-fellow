class Car (object):
  def __init__(self, car_type = None, car_model = None, car_name = None):
    self.car_type = car_type
    self.speed = 0
    
    if car_model is None:
      self.car_model = "GM"
    else:
      self.car_model = car_model
    if car_name is None:
      self.car_name = "General"
    else:
      self.car_name = car_name
      
      #the method will return number of door for porche and koenigsegg.  it will terurn 4 else shoudl return 2
  
  def num_of_doors(self):
    if self.car_type != "porche" or "koenigsegg":
      return 4
      return 2
      
      #the method return number of wheels of the car type. trailer will return 10 else 8
   
  def num_of_wheels(self):
    if self.car_type != "trailer":
      return 10
      return 8
      
    # this method calculates speed the car passed
    
  def drive(self, speed):
    if self.v_type == 'trailer':
       speed_calc = str(speed) + str(speed)
       self.speed = int(speed_calc)
    else:
      speed_calc = speed * (3 * 100)
      self.speed = speed_calc + 100
      return self       

  def is_saloon(self):
    if self.car_type == "saloon":
       return True
       return False  
       