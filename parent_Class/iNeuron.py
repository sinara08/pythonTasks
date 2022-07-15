class iNeuron:
    def __init__(self):
        self.login = {}
    def __add_member(self,id,pswd):
         self.login[id] = pswd

    def login_validity(self, id, pswd):
        if self.login[id] == pswd:
            print("User has successfully logged in")