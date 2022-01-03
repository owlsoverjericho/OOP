''' A software academy teaches two types of courses: local courses that are held in some of the academy’s local labs and offsite courses held in some other town outside of the academy’s headquarters. Each course has a name, a teacher assigned to teach it and a course program (sequence of topics). Each teacher has a name and knows the courses he or she teaches. Both courses and teachers could be printed in human-readable text form. All your courses should implement ICourse. Teachers should implement ITeacher. Local and offsite courses should implement ILocalCourse and IOffsiteCourse respectively. Courses and teachers should be created only through the ICourseFactory interface implemented by a class named CourseFactory. Write a program that will form courses of software academy.

 '''


class ICourse():
    def __init__(self) -> None:
        self.__name = ''
        self.__teacher = ''
        self.__program = []


class ILocalCourse():
    def __init__(self) -> None:
        super().__init__


class IOffsiteCourse():
    def __init__(self) -> None:
        super().__init__


class ITeacher():
    def __init__(self) -> None:
        self.__name = ''
        self.__courses = []


class ICourseFactory():
    pass
