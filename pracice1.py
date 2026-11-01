class person:
    name = "huzefa"
    occupation= "Software Devloper"
    networth = 10 
    def info(self , account , father_name ):
        self.account = account
        self.father_name  = father_name
        print(self.account , self.father_name)


a = person()
print(a.name)
a.name = "shubham"
print(a.name)
a.info(120000 , "kali")