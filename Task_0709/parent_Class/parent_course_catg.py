class Courses:
    def __init__(self,ctg="",crs=''):
        self.ct = ctg
        self.crs = crs
        self.__ctg = {}

    def __add_course(self,course):
        if course.ct not in self.__ctg:
            self.__ctg[course.ct] = list()
        self.__ctg[course.ct].append(course.crs)
