x=["lk","b","h","n","y"]
y=["a","b","c","d"]
name=''
def user():
   while True:
       print("Enter a user name")
       name=input()
       if name in x:
          password()
          break
def invalid_user():
   while name not in  x:
          print("enter a valid user name:\n")
          name=input()
          continue
          user()
     
pass_=''            
def password():
    for pass_ in y:
        pass_=input("enter a password:\n")
        if pass_ in y:
            print("login successfully")
            break
def invalid_password():
    while pass_ not in y:
            print("enter a valid password")
            break
user()
