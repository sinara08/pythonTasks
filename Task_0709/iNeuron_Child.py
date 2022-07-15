from parent_Class.iNeuron import iNeuron
import logging

logging.basicConfig(filename="iNeuron.log",level=logging.DEBUG,
                    format='%(levelname)s %(asctime)s %(message)s')

#Please use id -sinara pswd - 123 to enter

class Hall_of_Fame(iNeuron):
    def show_details(self):
        logging.info("Welcome to Hall of Fame")

class affiliate(iNeuron):
    def show_details(self):
        logging.info("Welcome to Affiliate")




if __name__ == "__main__":
    try:
        id = input("Please enter your login id: ")
        pswd = input("Please enter your password: ")

        i = iNeuron()
        i._iNeuron__add_member("sinara","123")
        i.login_validity(id,pswd)

        print("Which option do you want to explore more?")
        print("1.Hall of Fame \n2.Become an affiliate")
        while True:
            ch = int(input("Please enter your choice: "))
            if ch == 1:
                h = Hall_of_Fame()
                h.show_details()
                break
            elif ch == 2:
                a = affiliate()
                a.show_details()
                break
            else:
                print("Entered wrong choice. Please select either 1 or 2")

        print("Explored all area.Visit us soon")
    except KeyError:
        logging.info("Either id or password is wrong.Try again later")
        exit(1)
    except Exception as e:
        print(e)