from Person import Person

class Teacher(Person):
   def __init__(self, name, age, gender, experience):
      super().__init__(name, age, gender)
      self._experience = None
      self.set_experience(experience)

   def get_experience(self):
      return self._experience

   def set_experience(self, experience):
      if not isinstance(experience, int) or experience < 1:
         raise ValueError("Experience must be an integer between 1.")
      self._experience = experience

   def __str__(self):
      return f"Teacher {super().__str__()}, Experience: {self._experience}"