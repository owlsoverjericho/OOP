class Group:
    def __init__(self, groupName, academicDepartment, faculty):
        self.groupName = groupName;
        self.academicDepartment = academicDepartment;
        self.faculty = faculty;
        self.students = [];
    def addStudent(self, Student):
        if Student not in self.students:
            self.students.append(Student);

class Student:
    def __init__(self, name, surname, RBN):
        self.name = name;
        self.surname = surname;
        self.RBN = RBN;
        self.classes = {};
    def __eq__(self, other):
        return self.RBN == other.RBN;
    def gradeSetter(self, subject, grade):
        if subject not in self.classes:
            self.classes[subject] = [];
        self.classes[subject].append(grade);
    def averageClass(self, Class):
        sum = 0;
        for grade in self.classes[Class]:
            sum += grade;
        return sum / len(self.classes[Class]);
    def averageGrades(self):
        allGrades = [];
        for value in self.classes.values():
            allGrades += value;
        sum = 0;
        for grade in allGrades:
            sum += grade;
        return sum / len(allGrades);
            
x = Student("Name1", "Surname1", 12);
y = Student("Name1", "Surname1", 23);
z = Student("Name1", "Surname1", 34);
w = Student("Name1", "Surname1", 45);
a = Student("Name1", "Surname1", 45);
TV = Group("TV-z01", "APEPS", "TEF");
TV.addStudent(x);
TV.addStudent(y);
TV.addStudent(z);
TV.addStudent(w);

print(TV.students);

TV.students[0].gradeSetter('Math', 60);
TV.students[0].gradeSetter('Math', 100);
TV.students[0].gradeSetter('Arts', 70);
TV.students[0].gradeSetter('Arts', 90);
print(x.averageGrades());
