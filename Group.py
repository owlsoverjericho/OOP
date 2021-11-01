class Student:
    classes = {};
    def __init__(self, name, surname, RBN):
        self.name = name;
        self.surname = surname;
        self.RBN = RBN;
    def gradeSetter(self, subject, grade):
        if subject not in self.classes:
            self.classes[subject] = [];
        self.classes[subject].append(grade);
    def averageClass(self, Class):
        sum = 0;
        for grade in self.classes[Class]:
            sum += grade;
        return sum / len(self.classes[Class]);
x = Student("Name", "Surname", 1488);

x.gradeSetter('Math', 88);
x.gradeSetter('Math', 143);
x.gradeSetter('Arts', 98);
x.gradeSetter('Arts', 43);

print(x.classes);

print(x.averageClass('Math'));
