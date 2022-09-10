import random, secrets
import bcrypt

class Password():
    def __init__(self):
        pass
        
    def purpose(self:any): 
        confirming = True
        while confirming:
            purpose = str(input("what do you need the password for (gmail account, email, etc.)? "))
            print(purpose)
            confirm = str(input("are you okay with this choice (y/n)? "))
            if confirm.lower() == "y":
                print("ok, confirming purpose as:", purpose)
                break
            else:
                print("ok, enter another purpose that the password will be created for..")
        return purpose
               
    def generate(self:any):
        lowers = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        uppers = list(map(lambda alpha: alpha.upper(), lowers))
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        symbols = ["!","@","#","$","%","&","*","?"]
        allContent = (lowers) + (uppers) + (numbers) + (symbols)
        minimumChar = 12
        maxChar = 32
        password = ""
        for char in range(minimumChar, maxChar):
            password += secrets.choice(allContent)
        return password
        
    def hash(self, pw:str):
        pwbytes = pw.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(pwbytes,salt)
        return hashed
    
    def check(self:any, pw:str, hash:str):
        encode = pw.encode("utf-8")
        check = bcrypt.checkpw(encode, hash)
        return check
        
        
        