from tkinter import *
import pickle
tlist=[]  #global list
# defining person class
class person:
    def __init__(self,username,password,age,gender,department):
        self.un=username
        self.pd=password
        self.ag=age
        self.ge=gender
        self.dp=department
        
    def checkun(username):
        for i in tlist:
            if(i.un==username):
                return False
        return True
    
    
    def checkpd(password):
        a=0
        b=0
        c=0
        d=0
        if(len(password)>12 or len(password)<8):
           return False
        for i in password:
           if(i==' '):
            return False
           if(i.isupper()):
            a=a+1
           if(i.islower()):
            b=b+1
           if(i=='!' or i=='@' or i=='#' or i=='$' or i=='%' or i=='&' or i=='*'):  
            c=c+1
           if(i.isdigit()):
            d=d+1
        if(a==0 or b==0 or c==0 or d==0):
           return False
        else:
           return True
   
    
#defining teacher class
class teacher(person):  
    def __init__(self,username,password,age,gender,department):
      super().__init__(username,password,age,gender,department)
      self.type="Teacher"
      self.at=3
    
#defining student class 
class student(person):  
    def __init__(self,username,password,age,gender,department):
      super().__init__(username,password,age,gender,department)
#defining  ugstudent class  
class ugstudent(student):
    def __init__(self,username,password,age,gender,department):
      super().__init__(username,password,age,gender,department)
      self.type="Ugstudent" 
      self.at=3
#defining pgstudent class    
class pgstudent(student):
    def __init__(self,username,password,age,gender,department):
      super().__init__(username,password,age,gender,department)
      self.type="Pgstudent"
      self.at=3
#function to create an object             
def create(username,password,age,gender,department,var):    
         if(var==1):
          temp=teacher(username,password,age,gender,department)  
          tlist.append(temp)
        
         if(var==2):
          temp=ugstudent(username,password,age,gender,department)
          tlist.append(temp)  
         if(var==3):
          temp=pgstudent(username,password,age,gender,department)  
          tlist.append(temp)
#function to delete an object          
def delete(obj):
     for i in tlist:
         if(i.un==obj.un):
            tlist.remove(obj)
                  
           
#different fonts used in the code
font1 = ("Arial", 18, "bold")
font2=("Arial",12)
font3=("Arial",15)
# signin window
class signin:
   def __init__(self,wind):
      self.master=wind
      wind.geometry("1000x600")
      wind.configure(bg="lightgreen")
      f1=Frame(wind,bg="pale goldenrod",width=600,height=600)
      f1.place(relx=0.5,rely=0.5,anchor="center")
      f2=Frame(f1,bg="pale goldenrod",width=100,height=40)
      f2.place(in_=f1,relx=0.5,rely=0.1,anchor="center")
      f3=Frame(f1,bg="pale goldenrod",width=200,height=50)
      f3.place(in_=f1,relx=0.1,rely=0.3,anchor="w")
      f4=Frame(f1,bg="pale goldenrod",width=200,height=50)
      f4.place(in_=f1,relx=0.1,rely=0.5,anchor="w")
      f5=Frame(f1,bg="pale goldenrod",width=300,height=40)
      f5.place(in_=f1,relx=0.5,rely=0.86,anchor="center")
      
      label1=Label(f2,text="SIGN IN",font=font1,foreground="blue",background="pale goldenrod")
      label1.place(in_=f2,relx=0,rely=0)
      label2=Label(f3,text="USER NAME",font=font1,foreground="blue",background="pale goldenrod")
      label2.place(in_=f3,relx=0.1,rely=0.1)
      label3=Label(f4,text="PASSWORD",font=font1,foreground="blue",background="pale goldenrod")
      label3.place(in_=f4,relx=0.1,rely=0.1)
      label4=Label(f5,text="CREATE ACCOUNT",font=font1,foreground="blue",background="pale goldenrod")
      label4.place(in_=f5,relx=0,rely=0)
      entry1=Entry(f1,width=30,font=font1)
      entry1.place(in_=f1,relx=0.1,rely=0.35)
      entry2=Entry(f1,width=30,font=font1)
      entry2.place(in_=f1,relx=0.1,rely=0.55)
      mes=Message(f1,text="",font=font1,width=500,fg="blue",bg="pale goldenrod")
      mes.place(in_=f1,relx=0.45,rely=0.77,anchor="center")
      
      def clickb1():
          b=0
          for g in tlist:
              if(g.un==entry1.get()):
                b=1
                break
          if(b==0):
           mes.config(text="the username is not present")
          if(b==1):
              k=g
              if(k.pd!=entry2.get()):
                k.at=k.at-1
                if(k.at!=0):
                  mes.config(text=f"you have {k.at} attempts left")
                elif(k.at==0):
                  delete(k)
                  self.print_list()
                  mes.config(text="your account is deactivated")
              
              elif(k.un==entry1.get() and k.pd==entry2.get()):
                 k.at=3
                 for i in wind.winfo_children():
                  i.destroy()
                  user(wind,k)
              
      b1=Button(f1,text="sign in",font=font2,width=5,background="pale goldenrod",command=clickb1,foreground="blue")
      b1.place(in_=f1,relx=0.4,rely=0.65)
      
      def clickb2():
          for i in wind.winfo_children():
                i.destroy()
                signup(wind)
      
      
      b2=Button(f1,text="sign up",font=font2,width=5,background="pale goldenrod",command=clickb2,foreground="blue")
      b2.place(in_=f1,relx=0.4,rely=0.91)
      
   def print_list(self):
        print("User List:")
        for j in tlist:
            print(f"Username: {j.un}, Type: {j.type}")
        
        
          
#signup window              
class signup: 
    def __init__(self,wind):
      self.master=wind
      wind.geometry("1000x600")
      wind.configure(bg="lightgreen")
      f1=Frame(wind,bg="pale turquoise",width=600,height=600)
      f1.place(relx=0.5,rely=0.5,anchor="center")
      Label(f1,text="sign up",font=font1,fg="blue",bg="pale turquoise").place(in_=f1,relx=0.5,rely=0.03,anchor="center")
      Label(f1,text = "Username",font="Arial 12",padx = 15,pady = 10,bg="pale turquoise",fg="blue").place(in_=f1,relx=0.1,rely=0.1)
      Label(f1,text = "Password",font="Arial 12",padx = 15,pady = 10,bg="pale turquoise",fg="blue").place(in_=f1,relx=0.1,rely=0.2)
      Label(f1,text = "Age",font="Arial 12",padx = 15,pady = 10,bg="pale turquoise",fg="blue").place(in_=f1,relx=0.1,rely=0.3)
      Label(f1,text = "Gender",font="Arial 12",padx = 15,pady = 10,bg="pale turquoise",fg="blue").place(in_=f1,relx=0.1,rely=0.4)
      Label(f1,text = "Department",font="Arial 12",padx = 15,pady = 10,bg="pale turquoise",fg="blue").place(in_=f1,relx=0.1,rely=0.5)
      Label(f1,text="Account type",font="Arial 12",padx = 15,pady = 10,bg="pale turquoise",fg="blue").place(in_=f1,relx=0.1,rely=0.6)
      mes=Message(f1,text="enter the details",font=font1,width=400,fg="blue",bg="pale turquoise")
      mes.place(in_=f1,relx=0.45,rely=0.95,anchor="center")
      eusername=Entry(f1,width=25,font=font1)
      eusername.place(in_=f1,relx=0.3,rely=0.1)
      epassword=Entry(f1,width=25,font=font1)
      epassword.place(in_=f1,relx=0.3,rely=0.2)
      eage=Entry(f1,width=25,font=font1)
      eage.place(in_=f1,relx=0.3,rely=0.3)
      egender=Entry(f1,width=25,font=font1)
      egender.place(in_=f1,relx=0.3,rely=0.4)
      edepartment=Entry(f1,width=25,font=font1)
      edepartment.place(in_=f1,relx=0.3,rely=0.5)
      
      def clickedb():
          
          if(person.checkun(eusername.get())==False):
                mes.config(text="Username is already present")
          elif(person.checkpd(epassword.get())==False):
                mes.config(text="Password is invalid")
          else:
                create(eusername.get(),epassword.get(),eage.get(),egender.get(),edepartment.get(),var.get())
                self.print_list()
                signin(wind)  
      def clickb1():
           signin(wind)          
            
      var = IntVar()
      Radiobutton(f1,text = "Teacher",variable = var,value = 1,font=font2,fg="blue",bg="pale turquoise").place(in_=f1,relx=0.1,rely=0.7)
      Radiobutton(f1,text = "UGstudent",variable = var,value = 2,font=font2,fg="blue",bg="pale turquoise").place(in_=f1,relx=0.3,rely=0.7)
      Radiobutton(f1,text = "PGstudent",variable = var,value = 3,font=font2,fg="blue",bg="pale turquoise").place(in_=f1,relx=0.5,rely=0.7)
      
      b=Button(f1,text="sign up",font=font2,width=5,background="pale turquoise",command=clickedb,foreground="blue")
      b.place(in_=f1,relx=0.4,rely=0.75)
      b1=Button(f1,text="goback",font=font2,width=5,background="pale turquoise",command=clickb1,foreground="blue")
      b1.place(in_=f1,relx=0.4,rely=0.85)
      
    def print_list(self):
        print("User List:")
        for j in tlist:
            print(f"Username: {j.un}, Type: {j.type}")  
      
      
#user window     
class user:
    def __init__(self,wind,k):
      self.master=wind
      wind.geometry("1000x600")
      wind.configure(bg="lightgreen")
      f1=Frame(wind,bg="blanched almond",width=600,height=600)
      f1.place(relx=0.5,rely=0.5,anchor="center")   
      Label(f1,text=f"WELCOME {k.un}!",font=font1,bg="blanched almond",fg="blue").place(in_=f1,relx=0.5,rely=0.07,anchor="center")
      def clickb4():
        signin(wind)
      def clickb1():
        f2=Frame(f1,bg="blanched almond",width=400,height=500)
        f2.place(in_=f1,relx=0.25,rely=0.15)
        Label(f2,text=f"YOUR PROFILE",font=font1,bg="blanched almond",fg="red").place(in_=f2,relx=0,rely=0.1 )
        Label(f2,text=f"USER NAME : {k.un}",font=font1,bg="blanched almond",fg="blue").place(in_=f2,relx=0,rely=0.2)
        Label(f2,text=f"AGE : {k.ag}",font=font1,bg="blanched almond",fg="blue").place(in_=f2,relx=0,rely=0.3)
        Label(f2,text=f"GENDER : {k.ge}",font=font1,bg="blanched almond",fg="blue").place(in_=f2,relx=0,rely=0.4)
        Label(f2,text=f"DEPARTMENT : {k.dp}",font=font1,bg="blanched almond",fg="blue").place(in_=f2,relx=0,rely=0.5)
        Label(f2,text=f"ACCOUNT TYPE : {k.type}",font=font1,bg="blanched almond",fg="blue").place(in_=f2,relx=0,rely=0.6)
      def clicks1():
          delete(k)
          self.print_list()
          signin(wind)
      def clickb2():
         f2=Frame(f1,bg="blanched almond",width=430,height=500)
         f2.place(in_=f1,relx=0.25,rely=0.15)
         Label(f2,text = "Username",font="Arial 12",padx = 15,pady = 10,bg="blanched almond").place(in_=f2,relx=0.05,rely=0.1)
         Label(f2,text = "Password",font="Arial 12",padx = 15,pady = 10,bg="blanched almond").place(in_=f2,relx=0.05,rely=0.2)
         Label(f2,text = "Age",font="Arial 12",padx = 15,pady = 10,bg="blanched almond").place(in_=f2,relx=0.05,rely=0.3)
         Label(f2,text = "Gender",font="Arial 12",padx = 15,pady = 10,bg="blanched almond").place(in_=f2,relx=0.05,rely=0.4)
         Label(f2,text = "Department",font="Arial 11",padx = 15,pady = 10,bg="blanched almond").place(in_=f2,relx=0.05,rely=0.5)
         Label(f2,text="Account type",font="Arial 12",padx = 15,pady = 10,bg="blanched almond").place(in_=f2,relx=0.05,rely=0.6)
         mes=Message(f2,text="enter the details",font=font1,width=400,fg="blue")
         mes.place(in_=f2,relx=0.45,rely=0.95,anchor="center")
         eusername=Entry(f2,width=25,font=font1)
         eusername.place(in_=f2,relx=0.3,rely=0.11)
         epassword=Entry(f2,width=25,font=font1)
         epassword.place(in_=f2,relx=0.3,rely=0.21)
         eage=Entry(f2,width=25,font=font1)
         eage.place(in_=f2,relx=0.3,rely=0.31)
         egender=Entry(f2,width=25,font=font1)
         egender.place(in_=f2,relx=0.3,rely=0.41)
         edepartment=Entry(f2,width=25,font=font1)
         edepartment.place(in_=f2,relx=0.35,rely=0.51)
         
         def clickedb():
          if(person.checkun(eusername.get())==False):
             mes.config(text="Username is already present")
          elif(person.checkpd(epassword.get())==False):
             mes.config(text="Password is invalid")
          else:
            delete(k)
            self.print_list()
            create(eusername.get(),epassword.get(),eage.get(),egender.get(),edepartment.get(),var.get())
            self.print_list()
            user(wind,tlist[-1])  
            
         
         
         var = IntVar()
         Radiobutton(f2,text = "teacher",variable = var,value = 1,font="Arial,1",bg="blanched almond").place(in_=f2,relx=0.35,rely=0.61)
         Radiobutton(f2,text = "ugstudent",variable = var,value = 2,font="Arial,1",bg="blanched almond").place(in_=f2,relx=0.55,rely=0.61)
         Radiobutton(f2,text = "pgtudent",variable = var,value = 3,font="Arial,1",bg="blanched almond").place(in_=f2,relx=0.75,rely=0.61)
      
         b=Button(f2,text="update",font=font2,width=5,background="pale green",command=clickedb,foreground="blue")
         b.place(in_=f2,relx=0.4,rely=0.75)
         
         
         
      def clickb3():
         f2=Frame(f1,bg="blanched almond",width=500,height=500)
         f2.place(in_=f1,relx=0.25,rely=0.15)
         Label(f2,text="Are you sure want to delete the profile?",font=font3,bg="blanched almond",fg="red").place(in_=f2,relx=0,rely=0.3)
         s1=Button(f2,text="YES",font=font2,width=3,bg="brown",command=clicks1,fg="pale turquoise")
         s1.place(in_=f2,relx=0.2,rely=0.4)
         s2=Button(f2,text="NO",font=font2,width=3,bg="brown",command=clickb1,fg="pale turquoise")
         s2.place(in_=f2,relx=0.4,rely=0.4)
      Label(f1,text="MENU",font=font1,width=9,height=2,bg="blanched almond",fg="blue").place(in_=f1,relx=0,rely=0.2)   
      b1=Button(f1,text="Profile",font=font1,width=9,bg="blanched almond",command=clickb1,fg="blue")
      b1.place(in_=f1,relx=0,rely=0.3)
      b2=Button(f1,text="Update",font=font1,width=9,bg="blanched almond",command=clickb2,fg="blue")
      b2.place(in_=f1,relx=0,rely=0.4)
      b3=Button(f1,text="Deleteprofile",font=font1,width=9,bg="blanched almond",command=clickb3,fg="blue")
      b3.place(in_=f1,relx=0,rely=0.5)
      b4=Button(f1,text="logout",font=font1,width=9,command=clickb4,bg="blanched almond",fg="blue")
      b4.place(in_=f1,relx=0,rely=0.6)
    def print_list(self):
        print("User List:")
        for j in tlist:
            print(f"Username: {j.un}, Type: {j.type}")
#functions to save list    
def save_data():
    with open("user_data.pkl", "wb") as file:
        pickle.dump(tlist, file)

def load_data():
    global tlist
    try:
        with open("user_data.pkl", "rb") as file:
            tlist = pickle.load(file)
    except FileNotFoundError:
        tlist = []

def on_exit():
    save_data()
    root.destroy()     
#main function
root=Tk()
root.protocol("WM_DELETE_WINDOW", on_exit)
load_data()
signin(root)
root.mainloop()
 