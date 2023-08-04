def add():
        st_id=input("Enter student ID- ")
        st_name=input("Enter studnet name- ")
        with open(r'D:\2nd Year summer internship\1st project\Student.txt','a') as f:
            f.writelines(st_id+' '+st_name+'\n')

def view():
    with open(r'D:\2nd Year summer internship\1st project\Student.txt','r') as f:
        for line in f:
            print(line)

def delete_r():
    with open(r'D:\2nd Year summer internship\1st project\Student.txt', 'r') as f:
        lines = f.readlines()
        st_id=input("Enter id to be deleted- ")
    with open(r'D:\2nd Year summer internship\1st project\Student.txt', 'w') as f:
        for line in lines:
            words = line.split()
            if st_id not in words:
                f.write(line)

def Mark_attendence():
    with open(r'D:\2nd Year summer internship\1st project\Student.txt', 'r') as f:
        lines = f.readlines()
        date=input("please Enter a today's date dd-mm-yyyy format ")
        print("write P for present and A for absent")
        
        for word in lines:
            string=word.strip()
            attend=input(string+" ")
            with open(r'D:\2nd Year summer internship\1st project\attendece.txt', 'a') as f:
                f.writelines(date+" "+string+" "+attend+"\n")

def view_attendence():
    with open(r'D:\2nd Year summer internship\1st project\attendece.txt', 'r') as f:
        lines = f.readlines()
        st_id=input("Enter id to be searched ")
        for line in lines:
            for x in line.split():
                if(x==st_id):
                    print(line)

User=('Lokesh',2345)
access=False

ch=input("Enter y to Login n to Exit ")
attempts=3
while(ch!='n'):
    attempts-=1
    User_name=input("Enter your name- ")
    User_pass=int(input("Enter your password- "))
    if(User_name==User[0] and User_pass==User[1]):
        print("Welcome",User_name)
        access=True
        break        
    else:
        print('Failed to login, please try again')
        if(attempts==0):
            print("failed to login 3 times")
            break

if(access==True):
    while True:
        choice=int(input("Enter your choice \n 1:Add\n 2:view\n 3:delete\n 4:Mark_Attendence\n anything else to Exit\n"))
        if(choice==1):
            add()
        elif(choice==2):
            view()
        elif(choice==3):
            delete_r()
        elif(choice==4):
            Mark_attendence()
        elif(choice==5):
            view_attendence()
        else:
            print('Exiting...')
            break