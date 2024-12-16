from abc import ABC, abstractmethod

# Student class
class Student:
    def __init__(self, name, last_name, grade_point):
        self.name = str(name)
        self.last_name = str(last_name)
        self.grade_point = float(grade_point)

    def __repr__(self):
        return f"Student(name={self.name}, last_name={self.last_name}, grade_point={self.grade_point})"

# Strategy interface
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, students):
        pass

# Concrete implementation of a SortStrategy using lambdas
class SortByLastNameAscending(SortStrategy):
    def sort(self, students):
        return sorted(students, key=lambda s: s.last_name)

class SortByLastNameDescending(SortStrategy):
    def sort(self, students):
        return sorted(students, key=lambda s: s.last_name, reverse=True)

class SortByGradePointDescending(SortStrategy):
    def sort(self, students):
        return sorted(students, key=lambda s: s.grade_point, reverse=True)

# Infoeduka class
class InfoEduka:
    def __init__(self, students):
        self.students = students
        self.sort_strategy = None

    def set_sort_strategy(self, strategy: SortStrategy):
        self.sort_strategy = strategy

    def sort_students(self):
        if not self.sort_strategy:
            raise ValueError("Sorting strategy not set!")
        return self.sort_strategy.sort(self.students)

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
    info_eduka.set_sort_strategy(SortByLastNameAscending())
    print(info_eduka.sort_students())

    print("\nLastname - descending:")
    info_eduka.set_sort_strategy(SortByLastNameDescending())
    print(info_eduka.sort_students())

    print("\nGrade point - descending:")
    info_eduka.set_sort_strategy(SortByGradePointDescending())
    print(info_eduka.sort_students())