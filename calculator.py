import json

class GPA_Calculator:
    def __init__(self):
        self.grades = []

    def get_user_grades(self):
        try:
          num_grades = int(input("Enter the number of classes: "))
          for i in range(1, num_grades + 1):
            grade = float(input(f"Enter grade #{i}: "))
            while (grade > 100 or grade < 0):
              grade = float(input(f"Re-enter grade #{i}: "))
            self.grades.append(grade)
        except:
          print("Please enter a valid number\n------------------------")
          self.get_user_grades()


    def calculate_gpa(self):
        print("\nGPA REPORT\n-------------")
        total_grades = sum(self.grades)
        num_grades = len(self.grades)
        average_grade = total_grades / num_grades
        failing_grades = sum(grade < 65 for grade in self.grades)
        grade_conversion = self.get_gpa_info(average_grade)
        color = grade_conversion[3]

        print(f"Average grade: {self.color(color)} {average_grade:.2f} {self.color('w')}")
        print(f"Letter scale: {self.color(color)} {grade_conversion[0]} {self.color('w')}")
        print(f"4.0 scale: {self.color(color)} {grade_conversion[1]} {self.color('w')}")
        print(f"Failing grades: {failing_grades}")
      
        color = self.color(grade_conversion[2][1]['color'])
        to_next = round((grade_conversion[2][1]['percent'][0] - average_grade), 2)
        print(f"{to_next} points required to reach a grade of {color} {grade_conversion[2][0]} {self.color('w')} /{self.color('w')} {color} {grade_conversion[2][1]['4.0_scale']} {self.color('w')}")

    @staticmethod
    def get_gpa_info(value):
      with open('gpa_scale.json', 'r') as file:
            gpa_scale = json.load(file)

      next_upgrade = ["A+"] 
      for grade, info in gpa_scale.items():
        if value >= info['percent'][0]:
          return [grade, info['4.0_scale'], next_upgrade, info['color']]
        next_upgrade = [grade, info]
  

    def start(self):
      self.get_user_grades()
      self.calculate_gpa()

    def color(self, color):
      color_dict = {
        "w": '\033[0;37;5m',
        "b": '\033[1;34;40m',
        "g": '\033[1;32;40m',
        "y": '\033[1;33;40m',
        "r": '\033[1;31;40m'
      }
      return color_dict[color]
