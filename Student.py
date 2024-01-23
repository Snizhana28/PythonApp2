from Person import Person

class Student(Person):
   def __init__(self, name, age, gender, course):
      super().__init__(name, age, gender)
      self.__course = None
      self.set_course(course)

   def get_course(self):
      return self.__course

   def set_course(self, course):
      if not isinstance(course, int) or course < 1 or course > 5:
         raise ValueError("Course must be an integer between 1 and 5.")
      self.__course = course

   def __str__(self):
      return f"{super().__str__()}, Course: {self.__course}"
