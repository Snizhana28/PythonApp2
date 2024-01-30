from Teacher import Teacher

class DepartmentHead(Teacher):
   def __init__(self, name, age, gender, experience, department):
      super().__init__(name, age, gender, experience)
      self.__department = None
      self.set_department(department)

   def get_department(self):
      return self.__department

   def set_department(self, department):
      if not isinstance(department, str) or department == "":
         raise ValueError("Department must be a non-empty string.")
      self.__department = department

   def showInfo(self):
      return f"{super().showInfo()}, Department: {self.__department}"