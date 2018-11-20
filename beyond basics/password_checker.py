correct_password = "python123"
name = input("Enter name : ")
surname = input("enter surname : ")
password= input("Enter password : ")
while correct_password != password :
    password= input("Wrong Password! Enter password : ")
print("Hi %s %s , you are Logged In! " %(name , surname))
