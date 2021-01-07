x=["lk","b","h","n","y"]
y=["a","b","c","d"]
def user():
    name=input("enter a name:\n")
    for i in x:
        if i not in name:
            continue
             print("entr a valid user name")
            
        if name in i:
            password()
            break
            
def password():
    pass_=input("enter a password:\n")
    for j in y:
        if pass_ in j:
            print("login successfully")
            break
        else:
            print("enter a valid password")
            break
user()


    









