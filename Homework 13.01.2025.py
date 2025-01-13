class Student:
    def__init__(self, name, surname, gender):
        self.name = name
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"


    def __str__(self):
        avg_grade = self._calculate_avg_grade ()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f 'Имя: {self.name}\n'
                f 'Фамилия: {self.surname}\n'
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")


    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades list in self.grades.values() for grade in grades_list]
        return sum(all_grades) / len(all_grades)

    def __it__(self, other)
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return sum(all_grades) / len(all_grades)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades[course] += [grade]
            else:
                student.grades [course] = [grade]
        else:
            return "Ошибка"

    def average_student_grade(students, course):
        total_grades = []
        for student in students:
            if course in student.grades:
                total_grades.extend(student.grades[course])
        if total_grades:
            return sum(total_grades) / len(total_grades)
        return 0

    def average_lecturer_grade(lecturers, course):
        total_grades = []
        for lecturer in lecturers:
            if course in lecturer.grades:
                total_grades.extend(lecturer.grades[course])
        if total_grades:
            return sum(total_grades) / len(total_grades)
        return 0

    # Проверка
    student1 = Student('Ruoy', 'Eman', 'your_gender')
    student1.courses_in_progress += ['Python']
    student1.finished_courses += ['Введение в программирование']

    student2 = Student('Anna', 'Smith', 'female')
    student2.courses_in_progress += ['Python']
    student2.grades['Python'] = [7, 8, 9]

    lecturer1 = Lecturer('John', 'Doe')
    lecturer1.courses_attached += ['Python']
    lecturer1.grades['Python'] = [10, 9, 8]

    lecturer2 = Lecturer('Jane', 'Doe')
    lecturer2.courses_attached += ['Python']
    lecturer2.grades['Python'] = [9, 8, 9]

    reviewer1 = Reviewer('Some', 'Buddy')
    reviewer1.courses_attached += ['Python']

    reviewer1.rate_hw(student1, 'Python', 10)
    reviewer1.rate_hw(student1, 'Python', 8)
    reviewer1.rate_hw(student1, 'Python', 9)

    student1.rate_lecturer(lecturer1, 'Python', 10)
    student1.rate_lecturer(lecturer1, 'Python', 9)

    # Вывод
    print("Студенты:")
    print(student1)
    print(student2)

    print("\nЛекторы:")
    print(lecturer1)
    print(lecturer2)

    print("\nЭксперты:")
    print(reviewer1)

    print("\nСравнение студентов:")
    print(student1 > student2)

    print("\nСравнение лекторов:")
    print(lecturer1 > lecturer2)

    print("\nСредняя оценка за домашние задания по Python:")
    print(average_student_grade([student1, student2], 'Python'))

    print("\nСредняя оценка за лекции по Python:")
    print(average_lecturer_grade([lecturer1, lecturer2], 'Python'))
