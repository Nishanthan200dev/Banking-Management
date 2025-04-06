import os
import tkinter
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import webbrowser
import datetime
import csv
import random
import math



canvas_width = 1000
canvas_height =1000

date_object = datetime.date.today()



#second window
def Homepage():  
    web_window = tkinter.Tk()
    web_window.geometry("1366x768")
    web_window.resizable(0,0)
    web_window.title('Home Page')
    web_window.configure(bg="#12232E")
    name=str(Txt_box1.get())
    acc=str(Txt_box2.get())
    
    
    



    c = Canvas(web_window,width=1000,height=500,bg="#3F6BAA")
    c.create_rectangle(0, 0, 0, 0, fill="#3F6BAA")
    c.place(relx = 0.5,rely = 0.5,anchor=tkinter.CENTER)

    d = Canvas(web_window,width=1366,height=50,bg="#3F6BAA")
    d.create_rectangle(0, 0, 0, 0, fill="#3F6BAA")
    d.place(relx = 0.5,rely = 0.05,anchor=tkinter.CENTER)



    
    web_y= Label(web_window,text = "@", font=("Garamond", 27),background="#007CC7")
    web_y.place(relx = 0.5, rely = 0.05, anchor = tkinter.CENTER)

    web_y= Label(web_window,text =name, font=("Garamond", 27),background="#007CC7")
    web_y.place(relx = 0.9, rely = 0.05, anchor = tkinter.CENTER)

    Button1 = tkinter.Button(web_window,text = "ENTER",command = web2,fg = "white", bg = "pale green4", height=2,width= 12)
    Button1.place(relx = 0.5,rely = 0.72, anchor = tkinter.W)

    web_window.mainloop()


    


def created():
    created_window= tkinter.Tk()
    created_window.geometry("1600x900")
    created_window.resizable(0,0)
    created_window.title('Verify')
    created_window.configure(bg="#3F6BAA")
    with open("details.csv",mode='a') as filede:
                writer=csv.writer(filede)
                print(de)
                writer.writerow(de)
    
    Label1 = Label(created_window, text = "YOUR ACCOUNT CREATED SUCCESSFULY", font=("Bahnschrift Semibold", 30),background="#3F6BAA")
    Label1.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)
    ok_button = tk.Button(created_window, text="Login Page", command=main,height=1,width= 10)
    ok_button.place(relx = 0.8,rely = 0.5, anchor = tkinter.W)


    
    created_window.mainloop()

def create_username():
    def check3():
        
        pas=str(Txt_box2.get())
        repas=str(Txt_box3.get())

        if pas==repas:
            created()
        else:
            pop_up = tk.Toplevel()
            pop_up.title("Not Match")
            message = tk.Label(pop_up, text="Your Password Doesn't match. TRY AGAIN", padx=200, pady=2005)
            message.pack()
            ok_button = tk.Button(pop_up, text="SignUp", command=Signup,height=1,width= 10)
            ok_button.place(relx = 0.6,rely = 0.5, anchor = tkinter.W)

            ok_button.pack()
        
    user_window = tkinter.Tk()
    user_window.geometry("1600x900")
    user_window.resizable(0,0)
    user_window.title('Verify')
    user_window.configure(bg="#3F6BAA")
    
    Label1 = Label(user_window, text = "Enter USERNAME:", font=("Bahnschrift Semibold", 15),background="#3F6BAA")
    Label1.place(relx = 0.3, rely = 0.237, anchor = tkinter.CENTER)
    Txt_box1=  ttk.Entry(user_window, width= 30,font= ("DM Sans",20))   #text box
    Txt_box1.grid(row=1, column=4)
    Txt_box1.place(relx = 0.4, rely = 0.237)


    Label2= Label(user_window, text = "Enter PASSWORD:", font=("Bahnschrift Semibold", 15),background="#3F6BAA")
    Label2.place(relx = 0.3, rely = 0.337, anchor = tkinter.CENTER)
    Txt_box2=  ttk.Entry(user_window, width= 30,font= ("DM Sans",20))   #text box
    Txt_box2.grid(row=1, column=4)
    Txt_box2.place(relx = 0.4, rely = 0.337)


    Label3= Label(user_window, text = "ReEnter PASSWORD:", font=("Bahnschrift Semibold", 15),background="#3F6BAA")
    Label3.place(relx = 0.3, rely = 0.437, anchor = tkinter.CENTER)
    Txt_box3=  ttk.Entry(user_window, width= 30,font= ("DM Sans",20))   #text box
    Txt_box3.grid(row=1, column=4)
    Txt_box3.place(relx = 0.4, rely = 0.437)
    
    ok_button = tk.Button(user_window, text="Procced", command=check3,height=1,width= 10)
    ok_button.place(relx = 0.8,rely = 0.5, anchor = tkinter.W)


    
    
    user_window.mainloop()

def verify():
    verify_window = tkinter.Tk()
    verify_window.geometry("1600x900")
    verify_window.resizable(0,0)
    verify_window.title('Verify')
    verify_window.configure(bg="#3F6BAA")
    print(de)
    otp=[]

    def check2():
        otpin=str(Txt_box1.get())
        otpout=otp[0]
        if otpin == otpout:
            create_username()
        else:
            pop_up = tk.Toplevel()
            pop_up.title("Error")
            message = tk.Label(pop_up, text="OTP ENTERED IS NOT SAME", padx=500, pady=300)
            message.pack()
            otp.pop()
            ok_button.pack()
            
    
    def verifypopup():
        digits="0123456789"
        OTP=""
        for i in range(6):
            OTP+=digits[math.floor(random.random()*10)]
        
        otp.append(OTP)
        
            
        
        verifyc = tk.Toplevel()
        
        verifyc.title("OTP")
        message = tk.Label(verifyc,text=OTP, padx=200, pady=200)
        message.pack()
        

        ok_button.pack()



        
    Label1 = Label(verify_window, text = "To Verify enter OTP", font=("Bahnschrift Semibold", 15),background="#3F6BAA")
    Label1.place(relx = 0.3, rely = 0.237, anchor = tkinter.CENTER)
    
    Txt_box1=  ttk.Entry(verify_window, width= 30,font= ("DM Sans",20))   #text box
    Txt_box1.grid(row=1, column=4)
    Txt_box1.place(relx = 0.4, rely = 0.412)

    
    ok_button3= tk.Button(verify_window, text="Send OTP", command=verifypopup,fg = "white", font="Bahnschrift", bg = "pale green4", height=1,width= 10)
    ok_button3.place(relx = 0.6,rely = 0.5, anchor = tkinter.W)

    ok_button2 = tk.Button(verify_window, text="Procced", command=check2,fg = "white", font="Bahnschrift", bg = "pale green4", height=1,width= 10)
    ok_button2.place(relx = 0.8,rely = 0.5, anchor = tkinter.W)


    verify_window.mainloop()

    




de=[]
#third window
def details():
    details_window = tkinter.Tk()
    details_window.geometry("1600x900")
    details_window.resizable(0,0)
    details_window.title('Details')
    details_window.configure(bg="#3F6BAA")
    def write2():
        dob=str(Txt_box3.get())
        aadhar=str(Txt_box4.get())
        pan=str(Txt_box5.get())
        mob=str(Txt_box6.get())
        name=namesi[0]
        acc=accsi[0]
        de.extend([name,acc,dob,aadhar,pan,mob])
        details=[name,acc,dob,aadhar,pan,mob]
       
        verify()
        
        
    def data():
        named=namesi[0]
        accd=accsi[0]
        Label11.config(text=f"{named}")
        Label21.config(text=f"{accd}")
    Label1 = Label(details_window, text = "Name:", font=("Bahnschrift Semibold", 15),background="#3F6BAA")
    Label1.place(relx = 0.3, rely = 0.237, anchor = tkinter.CENTER)
    Label11 = Label(details_window, text = " ", font=("Bahnschrift Semibold", 15),background="#3F6BAA")
    Label11.place(relx = 0.41,rely = 0.237, anchor = tkinter.CENTER)
    
    
    Label2 = Label(details_window, text = "Account Number:", font=("Bahnschrift Semibold", 15),background="#3F6BAA")
    Label2.place(relx = 0.3, rely = 0.337, anchor = tkinter.CENTER)
    Label21 = Label(details_window, text = " ", font=("Bahnschrift Semibold", 15),background="#3F6BAA")
    Label21.place(relx = 0.45, rely = 0.337, anchor = tkinter.CENTER)
    

    
    Label3 = Label(details_window, text = "D.O.B:", font=("Bahnschrift Semibold", 15),background="#3F6BAA")
    Label3.place(relx = 0.3, rely = 0.437, anchor = tkinter.CENTER)
    Txt_box3=  ttk.Entry(details_window, width= 30,font= ("DM Sans",20))   #text box
    Txt_box3.grid(row=1, column=4)
    Txt_box3.place(relx = 0.4, rely = 0.412)

    
    Label4 = Label(details_window, text = " Aadhar Number:", font=("Bahnschrift Semibold", 15),background="#3F6BAA")
    Label4.place(relx = 0.3, rely = 0.537, anchor = tkinter.CENTER)
    Txt_box4 =  ttk.Entry(details_window, width= 30,font= ("DM Sans",20))   #text box
    Txt_box4.grid(row=1, column=4)
    Txt_box4.place(relx = 0.4, rely = 0.512)

    
    Label5 = Label(details_window, text = "PAN:", font=("Bahnschrift Semibold", 15),background="#3F6BAA")
    Label5.place(relx = 0.3, rely = 0.637, anchor = tkinter.CENTER)
    Txt_box5=  ttk.Entry(details_window, width= 30,font= ("DM Sans",20))   #text box
    Txt_box5.grid(row=1, column=4)
    Txt_box5.place(relx = 0.4, rely = 0.612)

    
    Label6 = Label(details_window, text = "Mobile Number:", font=("Bahnschrift Semibold", 15),background="#3F6BAA")
    Label6.place(relx = 0.3, rely = 0.737, anchor = tkinter.CENTER)
    Txt_box6=  ttk.Entry(details_window, width= 30,font= ("DM Sans",20))   #text box
    Txt_box6.grid(row=1, column=4)
    Txt_box6.place(relx = 0.4, rely = 0.712)
    
    data()
    Button1 = tkinter.Button(details_window,text = "Proceed",command =write2,fg = "white", font="Bahnschrift", bg = "pale green4", height=1,width= 10)    #enter button
    Button1.place(relx = 0.5,rely = 0.812, anchor = tkinter.W)
    details_window.mainloop()



namesi=[]
accsi=[]  
def Signup():
    
    Signup_window = tkinter.Tk()
    Signup_window.geometry("1600x900")
    Signup_window.resizable(0,0)
    Signup_window.title('SignUp')
    Signup_window.configure(bg="#3F6BAA")


    
    def account_number():
        acc=' '.join(str(random.randint(0,9))for _ in range (12))
        Label4.config(text=f"{acc}")
        return acc
    def write1():
        name=str(Txt_box3.get())
        namesi.append(name)
        acc=accsi[0]
        datawr=[name,acc]
        with open("data.csv",mode='a') as filew:
                    writer=csv.writer(filew)
                    print(datawr)
                    writer.writerow(datawr)
        details()
    Label1 = Label(Signup_window, text = "CREATE ACCOUNT", font=("Bahnschrift Bold", 35),background="#3F6BAA")
    Label1.place(relx = 0.5, rely = 0.3, anchor = tkinter.CENTER)



    Label2 = Label(Signup_window, text = "Enter Name:", font=("Bahnschrift Semibold", 15),background="#3F6BAA")
    Label2.place(relx = 0.3, rely = 0.437, anchor = tkinter.CENTER)


    Txt_box3 =  ttk.Entry(Signup_window, width= 30,font= ("DM Sans",20))   #text box
    Txt_box3.grid(row=1, column=4)
    Txt_box3.place(relx = 0.36, rely = 0.412)

        
        
    Label3 = Label(Signup_window, text = "Account Number:", font=("Bahnschrift Semibold", 15),background="#3F6BAA")
    Label3.place(relx = 0.3, rely = 0.5, anchor = tkinter.CENTER)
    
    Label4= Label(Signup_window, text = " ",font=("Bahnschrift Semibold", 20),background="#3F6BAA")
    Label4.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)
    
    
    Button1 = tkinter.Button(Signup_window,text = "Done",command =write1,fg = "white", font="Bahnschrift", bg = "pale green4", height=1,width= 10)    #enter button
    Button1.place(relx = 0.5,rely = 0.72, anchor = tkinter.W)





   

        
    accnumber=account_number()
    accsi.append(accnumber)
    print(accsi)
    print(accnumber)



                                                                                                  


        
    Signup_window.mainloop()


    
def main():
    def check():

        namech=str(Txt_box1.get())
        accch=str(Txt_box2.get())

        with open('data.csv',mode='w+') as filer:
         read=csv.reader(filer,delimiter=',')
         for words in read:
                print(words)
                for ch in words:
                    print(ch)
                    if namech == ch:
                        Homepage()
         else:
            pop_up = tk.Toplevel()
            pop_up.title("NOT EXIST")
            message = tk.Label(pop_up, text="User ID is NOT EXIST. Try Again or Create new Account", padx=500, pady=300)
            message.pack()
            ok_button = tk.Button(pop_up, text="SignUp", command=Signup,height=1,width= 10)
            ok_button.place(relx = 0.6,rely = 0.5, anchor = tkinter.W)

            ok_button.pack()


     
    #main page
    main_window = tkinter.Tk()
    main_window.geometry("1366x768")
    main_window.title('Login Page')  #title
    main_window.resizable(0,0)
    main_window.configure(bg="#12232E")


    a = Canvas(main_window,width=900,height=500,bg="#3F6BAA")
    a.create_rectangle(0, 0, 0, 0, fill="#3F6BAA")
    a.place(relx = 0.5,rely = 0.5,anchor=tkinter.CENTER)



    #front end
    Label1 = Label(main_window, text = date_object, font=("Bahnschrift Bold", 20),background="#12232E",fg="#EEFBFB")   #date
    Label1.place(relx = 0.06, rely = 0.1, anchor = tkinter.CENTER)

    Label1 = Label(main_window, text = "OBLIVION BANK", font=("Bahnschrift Bold", 27),background="#3F6BAA")
    Label1.place(relx = 0.5, rely = 0.3, anchor = tkinter.CENTER)

    Label1 = Label(main_window, text = "User ID:", font=("Bahnschrift Semibold", 15),background="#3F6BAA")
    Label1.place(relx = 0.33, rely = 0.437, anchor = tkinter.CENTER)

    Label1 = Label(main_window, text = "Account Number:", font=("Bahnschrift Semibold", 15),background="#3F6BAA")
    Label1.place(relx = 0.3, rely = 0.537, anchor = tkinter.CENTER)




    Txt_box1 =  ttk.Entry(main_window, width= 30,font= ("DM Sans",20))   #text box
    Txt_box1.grid(row=1, column=4)
    Txt_box1.place(relx = 0.36, rely = 0.412)


    Txt_box2 = ttk.Entry(main_window, width=30,font= ("DM Sans",20))
    Txt_box2.grid(row=2, column=4)
    Txt_box2.place(relx = 0.36, rely = 0.512)


         
    Button1 = tkinter.Button(main_window,text = "Login",command =check,fg = "white", font="Bahnschrift", bg = "pale green4", height=1,width= 10)    #enter button
    Button1.place(relx = 0.37,rely = 0.72, anchor = tkinter.W)

         
    Button2 = tkinter.Button(main_window,text = "SignUp",command = Signup,height = 1,width= 10,bg = "tomato4", font="Bahnschrift", fg = 'white')
    Button2.place(relx = 0.59,rely = 0.72, anchor=tkinter.E)


    main_window.mainloop()
main()

