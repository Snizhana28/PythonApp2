from Person import Person

class Student(Person):
   def __init__(self, name, age, gender, course):
      super().__init__(name, age, gender)
      self._course = None
      self.set_course(course)

   def get_course(self):
      return self._course

   def set_course(self, course):
      if not isinstance(course, int) or course < 1 or course > 5:
         raise ValueError("Course must be an integer between 1 and 5.")
      self._course = course

   def __str__(self):
      return f"Student {super().__str__()}, Course: {self._course}"
