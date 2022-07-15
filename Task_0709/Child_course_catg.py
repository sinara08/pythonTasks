
from parent_Class.parent_course_catg import Courses
import logging

logging.basicConfig(filename='Course_category.log', level=logging.DEBUG,
                    format='%(levelname)s %(asctime)s %(message)s')


class Categories(Courses):
    def format_courses(self, crses):
        for i in crses:
            if i.ct.upper() != "DS" and i.ct.upper() != "MARKETING":
                raise Exception("Invalid category")
            else:
                self._Courses__add_course(i)

    def show_details(self, ct):
        # for i in self._Courses__ctg.keys():
        logging.info("Courses under %s are %s", ct, self._Courses__ctg[ct])


if __name__ == "__main__":
    while True:
        try:
            c = Categories()
            c.format_courses([Courses("DS", "FSDS"), Courses("DS", "NLP"), Courses("DS", "Python"),
                              Courses("Marketing", "Youtube Marketing"), Courses("Marketing", "Digital Marketing")])
            ctg = input("Please enter the category to know course details(DS, Marketing): ").strip()

            if ctg.upper() != "DS" and ctg.upper() != "MARKETING":
                raise Exception("Enter a valid Category from (DS, Marketing)")
            else:
                c.show_details(ctg)
                break
        except Exception as e:
            logging.info(e)
