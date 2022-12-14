class SignUp():
    def __init__(self,name,email,phno,id,password):
        self.Name = name
        self.Email = email
        self.PhoneNo = phno
        self.ID = id
        self.Password = password

    def SimiIDCheck(self,id):
        file = open("Data.txt",'r')
        for i in file:
            i=i.replace('\n','')
            i=i.split(',')
            if i[0]==id:
                file.close()
                return True
            
        file.close()
        return False         

    def Storage(self):
        i=self.SimiIDCheck(self.ID)
        if i == False:
            file = open("Data.txt",'a')
            data = self.ID+','+self.Password+','+self.Name+','+self.Email+','+self.PhoneNo+'\n'
            file.write(data)
            file.close()
            return "Done"
        else:
            return "This ID is already registered please use a Different one"














new_signUP = SignUp('zeeshan','lidhjee@gmail.com','090078601','Zeeshan00','1234')
print(new_signUP.Storage())