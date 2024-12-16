# Student class
class Student:
    def __init__(self, name, last_name, grade_point):
        self.name = str(name)
        self.last_name = str(last_name)
        self.grade_point = float(grade_point)

    def __repr__(self):
        return f"Student(name={self.name}, last_name={self.last_name}, grade_point={self.grade_point})"

# Infoeduka class without Strategy Pattern
class InfoEduka:
    def __init__(self, students):
        self.students = students

    def sort_students(self, criterion):
        if criterion == "lastname_asc":
            return sorted(self.students, key=lambda s: s.last_name)
        elif criterion == "lastname_desc":
            return sorted(self.students, key=lambda s: s.last_name, reverse=True)
        elif criterion == "grade_desc":
            return sorted(self.students, key=lambda s: s.grade_point, reverse=True)
        else:
            raise ValueError("Invalid sorting criterion!")

# Main program
if __name__ == "__main__":
    list_of_students = [
        Student("Boro", "Mrazić", 3.8),
        Student("Ina", "Plinković", 3.9),
        Student("Mili", "Mekin", 4.5),
        Student("Mikica", "Bjelavić", 4.0),
    ]

    info_eduka = InfoEduka(list_of_students)

    print("Lastname - ascending:")
    print(info_eduka.sort_students("lastname_asc"))

    print("\nLastname - descending:")
    print(info_eduka.sort_students("lastname_desc"))

    print("\nGrade point - descending:")
    print(info_eduka.sort_students("grade_desc"))
