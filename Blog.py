# from parent_Class.parent_course_catg import Courses
import logging

logging.basicConfig(filename='InBlog.log', level=logging.DEBUG,
                    format='%(levelname)s %(asctime)s %(message)s')


class Data_Science:
    def get_popular(self):
        logging.info("\nPopular Topics in Data Science are :\n"
                     "01. Data Visualization with plotly and cufflinks \n"
                     "02. EDA : THE HIDDEN SECRET OF DATA \n"
                     "03. Fast Your Task With Dask \n"
                     "04. Data manipulation with Dask dataframe \n")


class BigData:
    def get_popular(self):
        logging.info("\nPopular Topics in BigData are :\n"
                     "01. How to read a dataset and write in a SQL Database: Using MySql And Python \n"
                     "02. Install Spark(PySpark) to run in Jupyter Notebook on Windows \n"
                     "03. MySql CheatSheet \n"
                     "04. Learn NO-SQL Database (MongoDB)")


class Aug_Reality:
    def get_popular(self):
        logging.info("\nPopular Topics in Augmented Reality are :\n"
                     "01. How to read a dataset and write in a SQL Database: Using MySql And Python \n"
                     "02. EDA : THE HIDDEN SECRET OF DATA \n"
                     "03. Fast Your Task With Dask \n"
                     "04. Data manipulation with Dask dataframe \n")


class Blog(Aug_Reality, BigData, Data_Science):
    def __init__(self):
        self.choice = 0

    def Intro(self):
        print("InBlog, quench your knowledge thirst here")
        print("Below are available categories.Select any one")
        print("1. Augmented Reality")
        print("2. BigData")
        print("3. Data Science")
        self.choice = input("Enter your choice: ")

    def get_popular(self):
        logging.info("\nPopular Topics in Blog are :\n"
                     "01. Deploy a Go/Golang Web App to Heroku \n"
                     "02. Data Visualization with plotly and cufflinks \n"
                     "03. EDA : THE HIDDEN SECRET OF DATA \n"
                     "04. Neural Machine Translation - A beginning to Attention \n")

    def decision(self, ar, bd, ds):
        if self.choice == "1":
            ar.get_popular()
        elif self.choice == "2":
            bd.get_popular()
        elif self.choice == "3":
            ds.get_popular()
        else:
            print("Entered a wrong choice. Rerun and the program and try again")


if __name__ == "__main__":
    d = Data_Science()
    a = Aug_Reality()
    bd = BigData()
    b = Blog()

    b.Intro()
    b.decision(a, bd, d)
