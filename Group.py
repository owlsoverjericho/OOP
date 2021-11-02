class Group:
    def __init__(self, groupName, academicDepartment, faculty):
        self.groupName = groupName;
        self.academicDepartment = academicDepartment;
        self.faculty = faculty;
        self.students = [];
    def addStudent(self, Student):
        for student in self.students:
            if Student.RBN == student.RBN:
                return "Already added!";
            self.students.append(Student);
    
class Student:
    def __init__(self, name, surname, RBN):
        self.name = name;
        self.surname = surname;
        self.RBN = RBN;
        self.classes = {};
    def gradeSetter(self, subject, grade):
        if subject not in self.classes:
            self.classes[subject] = [];
        self.classes[subject].append(grade);
    def averageClass(self, Class):
        sum = 0;
        for grade in self.classes[Class]:
            sum += grade;
        return sum / len(self.classes[Class]);
        
x = Student("Name1", "Surname1", 1);
y = Student("Name1", "Surname1", 2);
z = Student("Name1", "Surname1", 3);
w = Student("Name1", "Surname1", 4);
TV = Group("TV-z01", "APEPS", "TEF");
TV.addStudent(x);
TV.addStudent(y);
TV.addStudent(z);
TV.addStudent(w);
TV.addStudent(w);
