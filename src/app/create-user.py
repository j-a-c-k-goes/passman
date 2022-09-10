import random
import bcrypt
import secrets
import getpass
import time

class User():
    def __init__(self:any):
        self.lowers = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.uppers = list(map(lambda alpha: alpha.upper(), self.lowers))
        self.numbers = ["0","1","2","3","4","5","6","7","8","9"]
        self.symbols = ["!","@","#","$","%","&","*","?"]
        self.minchars = 12
        self.maxchars = 32

    def name(self:any):
        enteringName = True
        nameNotValid = True
        min = 2
        while enteringName and nameNotValid:
            name = str(input("enter a user name: "))
            if len(name) < min:
                print("invalid. user name must be longer than: ", self.minchars)          
            elif len(name) > self.maxchars:
                print("invalid! user name must be shorter than: ", self.maxchars) 
            for symbol in self.symbols:
                if symbol in name:
                    print("invalid. user name cannot contain symbol. try something without symbols") 
                    reentry = str(input("enter a user name: "))
                    name = reentry
            else: 
                nameNotValid = False        
                confirm = str(input(f"are you okay with [name] as a name (y/n)? "))
                if confirm.lower() == "y":
                    print("ok, confirming name as: ", name)
                    enteringName = False
                    break
                else:
                    print("ok, enter another potential username..")
        return name
    
    def password(self:any):
        enteringPassword = True
        passwordNotValid = True
        checkingPassword = True
        numInPw = False
        symInPw = False
        upperInPw = False
        lowerInPw = False
        passLengthValid = False
        while enteringPassword and passwordNotValid and checkingPassword:
            notification = "password: at least 12 character string containing uppercase, lowercase, symbolic, and numeric characters."
            print(notification)
            password = getpass.getpass()
            modified = ""
            for char in password:
                modified += "*"
            print(modified)
            if len(password) > self.minchars and len(password) < self.maxchars:
                passLengthValid = True
            for num in self.numbers:
                if num in password: numInPw = True
            for symbol in self.symbols:
                if symbol in password: symInPw = True
            for upper in self.uppers:
                if upper in password: upperInPw = True
            for lower in self.lowers:
                if lower in password: lowerInPw = True
            if numInPw and symInPw and upperInPw and lowerInPw and passLengthValid:
                enteringPassword = False
                passwordNotValid = False
                notification = "prepare to re-enter your password."
                print(notification)
                check = getpass.getpass()
                while check != password:
                    print("invalid re-entry. please retype your password.")
                    if check == password:
                        print("re-entry matches original. password confirmed!")
                        checkingPassword = False
                        break
               
        return password
    
    def email(self:any):
        print("your email will be used to notify you when passwords are updated.")
        email = str(input("what is your email address? "))
        return email
          
    def user(self:any, name:str, password:str, email:str):
        user = { "username":name, "password": password, "email": email }
        return user
    
    def forgot(self:any, credentialType="password"):
        pass
    
    def notify(self:any, user:object):
        pass
            