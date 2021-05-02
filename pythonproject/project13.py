from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('database.db')
conn.execute("""CREATE TABLE IF NOT EXISTS ADM(NAME INT PRIMARY KEY NOT NULL,CITY CHAR(10) NOT NULL,STATE CHAR(10) NOT NULL,GENDER CHAR(10) NOT NULL,MOBILE CHAR(12) NOT NULL,EMAIL CHAR(50) NOT NULL,USERNAME CHAR(50) NOT NULL,PASSWORD CHAR(50) NOT NULL)""")
conn.commit()
conn.close()




def Base_Page():
    
    global root

    root = tk.Tk()
    root.title("Welcome Page Interface")
    root.minsize(width = 1370, height = 700)
    root.maxsize(width = 1370, height = 700)

    button2 = tk.Label(root, text = "UNIVERSITY ADMISSION MANAGEMENT SYSTEM",font=('courier',20,'bold'),fg='lime green',bg='Dodger Blue4', width = 1370, height = 10, relief=tk.GROOVE)
    button2.pack()
    about= tk.Button(root, text ="ABOUT US",width=15,height=1 ,activebackground='IndianRed1',fg='black',bg='dark goldenrod',bd=4,font=('timesnow',16,'bold'),command =aboutus)
    about.pack(pady=50)
    

    stlogin= tk.Button(root, text = "LOGIN", width = 15, height = 1,activebackground='IndianRed1',fg='black',bg='SpringGreen3',bd=4,font=('timesnow',16,'bold'),command=sLogin_Page)
    stlogin.pack()
    root.mainloop()


def sLogin_Page():
    root.destroy()
    global Login_GUI
    Login_GUI=Tk()
    Login_GUI.title("Login Page")
    w,h=Login_GUI.winfo_screenwidth(),Login_GUI.winfo_screenheight()
    Login_GUI.geometry("%dx%d+0+0" % (w,h))
    icon=PhotoImage(file="loggg.png")
    logo=Label(Login_GUI,image=icon)
    AMS=Label(Login_GUI,text="Student Login Page",font=("Times New Roman", 50))
    logo.grid(row=1,column=0)
    AMS.grid(row=1,column=1,columnspan=4)
    
    lab1=Label(Login_GUI,text="User Name",padx=20,pady=5,font=("Times New Roman",28))
    lab2=Label(Login_GUI,text="Password",padx=20,pady=5,font=("Times New Roman",28))
    lab3=Label(Login_GUI,text="\n",font=("Times New Roman",28))
    global name
    global pswd
    name=Entry(Login_GUI,font=("Times New Roman",28))
    pswd=Entry(Login_GUI,show="*",font=("Times New Roman",28))
    
    Login_Button=Button(Login_GUI,text=" Login  ",command=validate,font=("Times New Roman",32))
    NewUser_Button=Button(Login_GUI,text="New User",command=LptoNu,font=("Times New Roman",32))
    
    lab1.grid(row=2,column=1)
    lab2.grid(row=3,column=1)
    name.grid(row=2,column=2)
    pswd.grid(row=3,column=2)
    lab3.grid(row=4)
    Login_Button.grid(row=5,column=1)
    NewUser_Button.grid(row=5,column=2)
    Login_GUI.mainloop()




    

def LptoNu():
    Login_GUI.destroy()
    NewUser_Page()
    
def BptoNu():
    root.destroy()
    NewUser_Page()
    
def nutoLp():
    NewUser_GUI.destroy()
    Login_Page()

def validate():
    c=0
    conn = sqlite3.connect('database.db')
    cursor = conn.execute("SELECT USERNAME,PASSWORD FROM ADM")
    for row in cursor:
        if( (str(name.get())==row[0]) and (str(pswd.get())==row[1])):
            c=1
            break
        else:
            c=0
    if(c==1):
        messagebox.showinfo("Status", "Login Successful")
        User_Page()
    if(c==0):
        messagebox.showinfo("Status", "Login Failed.\nPlease Try Again")
    conn.commit()
        

def NewUser_Page():
    
    global NewUser_GUI
    NewUser_GUI=Tk()
    NewUser_GUI.title("New user Page")
    w,h=NewUser_GUI.winfo_screenwidth(),NewUser_GUI.winfo_screenheight()
    NewUser_GUI.geometry("%dx%d+0+0" % (w,h))
    icon=PhotoImage(file="newuse.png",width=250)
    logo=Label(NewUser_GUI,image=icon)
    PMS=Label(NewUser_GUI,text="    New user Page",font=("Helvetica", 70))
    logo.grid(row=1,column=0)
    PMS.grid(row=1,column=1,columnspan=3)
    
    lab1=Label(NewUser_GUI,text="Name",padx=20,pady=5,font=("Times New Roman",23))
    lab2=Label(NewUser_GUI,text="State",padx=20,pady=5,font=("Times New Roman",23))
    lab3=Label(NewUser_GUI,text="City",padx=20,pady=5,font=("Times New Roman",23))
    lab4=Label(NewUser_GUI,text="Gender",padx=20,pady=5,font=("Times New Roman",23))
    lab5=Label(NewUser_GUI,text="Mobile",padx=20,pady=5,font=("Times New Roman",23))
    lab6=Label(NewUser_GUI,text="Email ID",padx=20,pady=5,font=("Times New Roman",23))
    lab7=Label(NewUser_GUI,text="User Name",padx=20,pady=5,font=("Times New Roman",23))
    lab8=Label(NewUser_GUI,text="Password",padx=20,pady=5,font=("Times New Roman",23))
    global Name
    global State
    global City
    global Mobile
    global Email
    global UserName
    global Pass
    Name=Entry(NewUser_GUI,font=("Times New Roman",23))
    State=Entry(NewUser_GUI,font=("Times New Roman",23))
    City=Entry(NewUser_GUI,font=("Times New Roman",23))
    global Gender
    Gender = StringVar()
    G1 = Radiobutton(NewUser_GUI, text="Male", variable=Gender, value="Male",font=("Times New Roman",23))
    G2 = Radiobutton(NewUser_GUI, text="Female", variable=Gender, value="Female",font=("Times New Roman",23))
    Mobile=Entry(NewUser_GUI,font=("Times New Roman",23))
    Email=Entry(NewUser_GUI,font=("Times New Roman",23))
    UserName=Entry(NewUser_GUI,font=("Times New Roman",23))
    Pass=Entry(NewUser_GUI,font=("Times New Roman",23))
    lab1.grid(row=2,column=0)
    lab2.grid(row=3,column=0)
    lab3.grid(row=4,column=0)
    lab4.grid(row=5,column=0)
    lab5.grid(row=6,column=0)
    lab6.grid(row=7,column=0)
    lab7.grid(row=8,column=0)
    lab8.grid(row=9,column=0)
    Name.grid(row=2,column=1)
    State.grid(row=3,column=1)
    City.grid(row=4,column=1)
    G1.grid(row=5,column=1)
    G2.grid(row=5,column=2)
    Mobile.grid(row=6,column=1)
    Email.grid(row=7,column=1)
    UserName.grid(row=8,column=1)
    Pass.grid(row=9,column=1)

    lab10=Label(NewUser_GUI,text="",font=("Times New Roman",28))
    lab10.grid(row=9)
    Submit_Button=Button(NewUser_GUI,text="Submit",command=DB_Reg,font=("Times New Roman",25),bd=3)
    Submit_Button.grid(row=10,column=1)
    NewUser_GUI.mainloop()

def DB_Reg():


    dbName=str(Name.get())
    dbCity=str(City.get())
    dbState=str(State.get())
    dbMobile=str(Mobile.get())
    dbGender=str(Gender.get())
    dbEmail=str(Email.get())
    dbUserName=str(UserName.get())
    dbPass=str(Pass.get())
    
    conn = sqlite3.connect('database.db')
    cursor=conn.execute("INSERT INTO ADM (NAME,CITY,STATE,MOBILE,GENDER,EMAIL,USERNAME,PASSWORD) VALUES (?,?,?,?,?,?,?,?)",(dbName,dbCity,dbState,dbMobile,dbGender,dbEmail,dbUserName,dbPass))
    conn.commit()
    messagebox.showinfo("Status", "Successfully Registered\nUse the User Name & Password to Login")
    NewUser_GUI.destroy()
    Base_Page()

def User_Page():
    Login_GUI.destroy()
    global User_GUI
    User_GUI=Tk()
    w,h=User_GUI.winfo_screenwidth(),User_GUI.winfo_screenheight()
    User_GUI.geometry("%dx%d+0+0" % (w,h))
    icon=PhotoImage(file="imagess.png",width=250,height=230)
    logo=Label(User_GUI,image=icon)
    AMS=Label(User_GUI,text="Admission Management System",font=("Helvetica", 50))
    logo.grid(row=0,column=0)
    AMS.grid(row=0,column=1,columnspan=3)

    icon1=PhotoImage(file="apply.png")
    Book=Label(User_GUI,image=icon1)
    applyButton=Button(User_GUI,text="Apply Now",font=("Times New Roman",32),bd=3,command=apply_Page)

    icon2=PhotoImage(file="photoo.png")
    Policy=Label(User_GUI,image=icon2)
    Policy_Button=Button(User_GUI,text="Eligibility ",font=("Times New Roman",32),bd=3,command=eligibility)

    icon3=PhotoImage(file="Logout.png")
    Logout=Label(User_GUI,image=icon3)
    Logout_Button=Button(User_GUI,text="Logout",font=("Times New Roman",32),bd=3,command=UptoBp)

    icon4=PhotoImage(file="add.png")
    Y=Label(User_GUI,text="NAME",font=("Times New Roman",18),bd=2,padx=10,pady=1)
    global Z
    Z=Entry(User_GUI,font=("Times New Roman",28))
    Details=Label(User_GUI,image=icon4)
    Details_Button=Button(User_GUI,text="Details",font=("Times New Roman",20),bd=2,command=De)
    
    Book.grid(row=1)
    applyButton.grid(row=2,column=0)
    Policy.grid(row=1,column=1)
    Policy_Button.grid(row=2,column=1)
    Logout.grid(row=1,column=2)
    Logout_Button.grid(row=2,column=2)
    Details.grid(row=1,column=3)
    Y.grid(row=2,column=3)
    Z.grid(row=3,column=3)
    Details_Button.grid(row=4,column=3)
    User_GUI.mainloop()
    
def De():
    zz=str(Z.get())
    conn = sqlite3.connect('database.db')
    cursor = conn.execute("SELECT NAME,CITY,STATE,MOBILE,GENDER,EMAIL  FROM ADM")
    for row in cursor:
        if(row[0]==zz):
            S="STUDENT DETAILS : \nNAME = "+str(row[0])+"\nCITY = "+row[1]+"\nMOBILE = "+row[2]+"\nGENDER = "+row[4]+"\nEMAIL = "+row[3]+"\nEMAIL = "+row[5]+"\n\n"
            messagebox.showinfo("Details",S)
    conn.commit()
    
def eligibility():
     messagebox.showinfo("ELIGIBILITY", "NOTE : \nAll students wishing to take admission in our college should have atleast 70% overall percentage in intermmediate....\n   ≥60% marks or equivalent in Class X in five subjects (Compulsory subjects - English, Mathematics, Science and Social Studies. The fifth can be a subject of Applicant's choice). The board can be CBSE/ICSE/any other board in India or an equivalent board if from a country outside India≥60% marks in Class XII in five subjects (Compulsory subjects - Physics, Chemistry, Mathematics or Biology (PCM/PCB) & English. The fifth can be a subject of Applicant's choice). The board can be any recognized board in India or an equivalent board if from a country outside India. In case you are from ISC board or have taken four subjects, aggregate of four subjects will be considered.≥60% marks in PCM in Class XII if you are opting for CSE or ECE streams and in PCB, PCM or PCMB if you are choosing BT stream.Should be appearing in the board examination in March/April 2020 or should have the necessary mark sheets if you have appeared in 2018 or 2019.Should have JEE Main/BITSAT/SAT/NEET/Any other State Engineering Entrance Examination's rank/score otherwise Applicant will be required to appeared in the NIIT University Engineering Test (NUET).Applicant should have scored ≥ Grade 4 in IB Board or minimum grade C in Cambridge IGCSE Board.....")

def aboutus():
     messagebox.showinfo("ABOUT US", " College is a sister concern of Aditya Education Society (AES), a charitable trust dedicated to the noble cause of spreading education in society. Imparting education, for this trust, does not mean furnishing truckloads of information to the learners and adorning them with some ornaments of academic degree; on the contrary, it believes that education is meant for igniting the minds of learners with inquisitiveness, inculcating ethical values in them and developing in them some mental faculties so that they can observe, analyse and understand anything that comes their way.Aditya College, keen on rendering the ideal of AES into reality, is committed to the two-fold achievement of quality and excellence. The institute has made an effective combination of excellent academic coaching and superb life skills training. While the academic mentoring equips every student for careers in academic, administrative, industrial and corporate sectors, the training in life skills adds a new dimension to their personality.We at Aditya not only tread the beaten track, but also break new grounds at every possible step. Keeping pace with the processes of globalization and glocalization, we encourage a free flow of ideas and always attempt a synthesis of the global and the local, the traditional and the trendy, of the ongoing and the upcoming. We aspire to be a trailblazer in the field of education in the 21st century. ")
def UptoBp():
    messagebox.showinfo("Status","Successfully Logged Off")
    User_GUI.destroy()
    Base_Page()

def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   prog=var1.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,Programming) VALUES(?,?,?,?,?)',(name1,email,gender,country,prog,))
   conn.commit()
   CalPrice2()
   
   

def apply_Page():
    global Fullname
    Fullname=StringVar()
    
    Email=StringVar()
    var = IntVar()
    c=StringVar()
    var1= IntVar()

    root = Tk()
    root.geometry('500x500')
    root.title("Registration Form")            
    label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
    label_0.place(x=90,y=53)


    label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)

    entry_1 = Entry(root,textvar=Fullname)
    entry_1.place(x=240,y=130)

    label_2 = Label(root, text="Email",width=20,font=("bold", 10))
    label_2.place(x=68,y=180)

    entry_2 = Entry(root,textvar=Email)
    entry_2.place(x=240,y=180)

    label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
    label_3.place(x=70,y=230)

    Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
    Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

    label_4 = Label(root, text="country",width=20,font=("bold", 10))
    label_4.place(x=70,y=280)

    list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

    droplist=OptionMenu(root,c, *list1)
    droplist.config(width=15)
    c.set('select your country') 
    droplist.place(x=240,y=280)

    label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
    label_4.place(x=85,y=330)
    var2= IntVar()
    Checkbutton(root, text="java", variable=var1).place(x=235,y=330)

    Checkbutton(root, text="python", variable=var2).place(x=290,y=330)

    Button(root, text='Submit',width=20,bg='brown',fg='white',command=CalPrice2).place(x=180,y=380)
    database()

    root.mainloop()



def CalPrice2():
    messagebox.showinfo("Thank You..! " ,"We will Notify You within 24 hours")
            


Base_Page()











   
   




























































