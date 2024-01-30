class Person:
   def __init__(self, name, age, gender):
      if not isinstance(name, str) or not isinstance(age, int) or not isinstance(gender, bool):
         raise TypeError("Invalid types for one or more fields.")

      self._name = name
      self._age = None
      self.set_age(age)
      self._gender = gender
   
   def get_name(self):
      return self._name
   
   def set_name(self, name):
      self._name = name

   def get_age(self):
      return self._age

   def set_age(self, age):      
      if 16 <= age <= 55:
         self._age = age
      else:
         raise ValueError("Age must be between 16 and 55.")
      
   def get_gender(self):
      return self._gender

   def set_gender(self, gender):
      self._gender = gender
   
   def showInfo(self):
      return f"\nName: {self._name}, Age: {self._age}, Gender: {'M' if self._gender else 'W'}"


