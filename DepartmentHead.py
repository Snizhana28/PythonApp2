from Teacher import Teacher

class DepartmentHead(Teacher):
   def __init__(self, name, age, gender, experience, department):
      super().__init__(name, age, gender, experience)
      self._department = None
      self.set_department(department)

   def get_department(self):
      return self._department

   def set_department(self, department):
      if not isinstance(department, str) or department == "":
         raise ValueError("Department must be a non-empty string.")
      self._department = department

   def __str__(self):
      return f"DepartmentHead {super().__str__()}, Department: {self._department}"