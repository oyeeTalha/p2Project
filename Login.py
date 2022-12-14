class Login():
    def __init__(self,id,password):
        self.ID = id
        self.Password = password

    def Validation(self):
        file = open("Data.txt",'r')
        for i in file:
            i=i.split(',')
            if i[0]==self.ID and i[1]==self.Password:
                file.close()
                return True
            
        file.close()
        return False




login = Login('Zeeshan0','1234')
print(login.Validation())
