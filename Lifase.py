#importing required modules
import tkinter as tk1
from tkvideo import tkvideo #pip install tkvideo and tkscrollfrme
from tkscrolledframe import ScrolledFrame
import tkinter.ttk as tk2
#establishing database connectivity
import mysql.connector as sql
con=sql.connect(host='localhost',
                user='root',
                password='xyzabc',
                database='lifase')
cur=con.cursor()

#establishing verification code for admin
adminverification='0000'

#renaming frequently used images/colors
mybgcol="#604c8d"
mybgimage1="assets/Lifase 1.gif"
mybgimage2="assets/Lifase 2.gif"
mybgimage3="assets/Lifase 3.gif"
mybgimage4="assets/Lifase 4.gif"

#creating window
window1=tk1.Tk()
window1.title("Lifase-Catalyzing Organization")

#creating a function to clear widgets from a frame
def clearwid(frame):
    for widget in frame.winfo_children():
            widget.destroy()

#creating required frames
frame0=tk1.Frame(window1)  
frame1=tk1.Frame(window1)
frame2=tk1.Frame(window1)
frame3=tk1.Frame(window1)
frame4=tk1.Frame(window1)
frame5=tk1.Frame(window1)
frame6=tk1.Frame(window1)
frame7=tk1.Frame(window1)
frame8=tk1.Frame(window1)
frame9=tk1.Frame(window1)
frame10=tk1.Frame(window1)
frame11=tk1.Frame(window1)
frame12=tk1.Frame(window1)
frame13=tk1.Frame(window1)
frame14=tk1.Frame(window1)
frame15=tk1.Frame(window1)
frame16=tk1.Frame(window1)
frame17=tk1.Frame(window1)
frame18=tk1.Frame(window1)
frame19=tk1.Frame(window1)
frame20=tk1.Frame(window1)
frame21=tk1.Frame(window1)
frame22=tk1.Frame(window1)
frame23=tk1.Frame(window1)
frame24=tk1.Frame(window1)
frame25=tk1.Frame(window1)
frame26=tk1.Frame(window1)
frame27=tk1.Frame(window1)
frame28=tk1.Frame(window1)
frame29=tk1.Frame(window1)
frame30=tk1.Frame(window1)
frame31=tk1.Frame(window1)
frame32=tk1.Frame(window1)
frame33=tk1.Frame(window1)
frame34=tk1.Frame(window1)
frame35=tk1.Frame(window1)
frame36=tk1.Frame(window1)
frame37=tk1.Frame(window1)
frame38=tk1.Frame(window1)
frame39=tk1.Frame(window1)
frame40=tk1.Frame(window1)
frame41=tk1.Frame(window1)
frame42=tk1.Frame(window1)
newframe=tk1.Frame(window1)

#placing the frames on the window
for frame in (frame0,newframe,frame1,frame2,frame3,frame4,frame5,frame6,frame7,frame8,
              frame9,frame10,frame11,frame12,frame13,frame14,frame15,frame16,
              frame17,frame18,frame19,frame20,frame21,frame22,frame23,frame24,
              frame25,frame26,frame27,frame28,frame29,frame30,frame31,frame32,
              frame33,frame34,frame35,frame36,frame37,frame38,frame39,frame40,
              frame41,frame42):
    frame.grid(row=0,column=0)

#creating frame0, which contains the introductory video
def loadframe0():
    if cur.rowcount>0:
        cur.fetchall()
    my_label = tk1.Label(frame0)
    my_label.grid(rowspan=10,columnspan=15)
    player = tkvideo("assets/Load Lifase.mp4",
                     my_label, loop = 0, size = (1180,650))
    player.play()
    my_label.after(8000,loadnewframe)

def loadnewframe():
    clearwid(frame0)
    newframe.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage1)
    widge=tk1.Label(newframe,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    tk1.Label(newframe,text='WELCOME TO LIFASE!',font=("Arial",35),bg="white",foreground=mybgcol).place(x=330,y=210)
    tk1.Label(newframe,text="",borderwidth=5,relief='solid',anchor='nw',width=25,
                  font=("Arial",15),bg=mybgcol,foreground="white").place(x=180,y=350)
    tk1.Label(newframe,text="USERNAME",borderwidth=5,relief='solid',anchor='nw',width=25,
                  font=("Arial",15),bg=mybgcol,foreground="white").place(x=360,y=350)
    tk1.Label(newframe,text="PASSWORD",borderwidth=5,relief='solid',anchor='nw',width=25,
                  font=("Arial",15),bg=mybgcol,foreground="white").place(x=640,y=350)
    tk1.Label(newframe,text='FOR THE PURPOSE OF THIS DEMONSTRATION,PLEASE USE THE FOLLOWING USERNAME AND PASSWORDS',
              font=("Arial",14),bg="white",foreground=mybgcol).place(x=60,y=310)
    tk1.Label(newframe,text='ADMIN',borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=180,y=380)
    tk1.Label(newframe,text='XYZ',borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=360,y=380)
    tk1.Label(newframe,text='1234',borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=640,y=380)
    tk1.Label(newframe,text='DOCTOR',borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=180,y=410)
    tk1.Label(newframe,text='ABC',borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=360,y=410)
    tk1.Label(newframe,text='123456',borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=640,y=410)
    tk1.Button(newframe,text="PROCEED",font=("Arial",15),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=loadframe1).place(x=500,y=580)
    
    
    

#creating frame1, which contains the first login screen
def loadframe1():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(newframe)
    clearwid(frame2)
    clearwid(frame3)
    frame1.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage1)
    widge=tk1.Label(frame1,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    tk1.Label(frame1,text='LOGIN',font=("Arial",30),bg="white",foreground=mybgcol).place(x=530,y=210)
    b1=tk1.Button(frame1,text="DOCTOR",font=("Arial",19),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=loadframe3)
    b1.place(x=535,y=305)
    b2=tk1.Button(frame1,text="ADMIN",font=("Arial",19),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=loadframe2)
    b2.place(x=545,y=390)

#frame2 is an admin frame and hence has been clubbed along with other admin frames for better comprehension of the code    
#creating frame3, which contains the doctor login page
def loadframe3():
    if cur.rowcount>0:
        cur.fetchall()
    frame3.tkraise()
    clearwid(frame1)
    photo1=tk1.PhotoImage(file=mybgimage1)
    widge=tk1.Label(frame3,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    tk1.Label(frame3,text='DOCTOR LOGIN',bg="white",font=("Arial",30),foreground=mybgcol).place(x=460,y=210)
    tk1.Label(frame3,text='USERNAME',bg="white",font=("Calibri",20),foreground=mybgcol).place(x=300,y=300)
    E1=tk1.Entry(frame3,font=('Times',20),bg=mybgcol,fg="white",cursor="hand2")
    E1.place(x=470,y=300)
    tk1.Label(frame3,text='PASSWORD',bg="white",font=("Calibri",20),foreground=mybgcol).place(x=300,y=400)
    E2=tk1.Entry(frame3,font=('Times',20),show='*',bg=mybgcol,fg="white",cursor="hand2")
    E2.place(x=470,y=400)
    def submitsignin():
        global userforprofile
        user=E1.get()
        userforprofile=user
        psw=E2.get()
        query="select * from logind where Username='{}'".format(user)
        cur.execute(query)
        k=cur.fetchone()
        if cur.rowcount==0:
            tk1.Label(frame3,text="USER NOT FOUND",width=20,bg="white",font=("Arial",18),foreground=mybgcol).place(x=480,y=520)
            E1.delete(0,tk1.END)
            E2.delete(0,tk1.END)
        else:
            a,b=k[0],k[1]
            if psw==k[1]:
                loadframe5()
            else:
                tk1.Label(frame3,text="INCORRECT PASSWORD",width=20,bg="white",font=("Arial",18),foreground=mybgcol).place(x=480,y=520)
                E2.delete(0,tk1.END)
    b1=tk1.Button(frame3,text="SUBMIT",font=("Arial",18),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,width=12,activeforeground="white",command=submitsignin)
    b1.place(x=512,y=460)
    b2=tk1.Button(frame3,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe1)
    b2.place(x=575,y=590)

#frame4 is an admin frame and hence has been clubbed along with other admin frames for better comprehension of the code
#frame5, which contains the doctor dashboard
def loadframe5():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame5)
    clearwid(frame8)
    clearwid(frame9)
    clearwid(frame3)
    clearwid(frame6)
    clearwid(frame7)
    clearwid(frame11)
    clearwid(frame13)
    frame5.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage3)
    widge=tk1.Label(frame5,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    b1=tk1.Button(frame5,text="DASHBOARD",font=("Arial",18),height=1,width=11,background="white",foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=loadframe5)
    b1.place(x=0,y=150)
    b2=tk1.Button(frame5,text="MY PROFILE",font=("Arial",18),height=1,width=11,background="white",foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=loadframe6)
    b2.place(x=0,y=200)
    b3=tk1.Button(frame5,text="MY PATIENTS",font=("Arial",18),height=1,width=11,background="white",foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=loadframe7)
    b3.place(x=0,y=250)
    b4=tk1.Button(frame5,text="EXIT APP",font=("Arial",18),height=1,width=11,background="white",foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=window1.destroy)
    b4.place(x=0,y=300)
    global image1
    global image2
    global image3
    global image4
    global image5
    image1=tk1.PhotoImage(file="assets/Schedule.gif").subsample(5,5)
    tk1.Button(frame5,image=image1,borderwidth=0,cursor="hand2",command=loadframe13).place(x=300,y=10)
    tk1.Label(frame5,text='SCHEDULE',font=("Arial",12),bg="white",foreground=mybgcol).place(x=350,y=230)
    image2=tk1.PhotoImage(file="assets/Circulars.gif").subsample(5,5)
    tk1.Button(frame5,image=image2,borderwidth=0,cursor="hand2",command=loadframe9).place(x=900,y=410)
    tk1.Label(frame5,text='CIRCULARS',font=("Arial",12),bg="white",foreground=mybgcol).place(x=960,y=380)
    image3=tk1.PhotoImage(file="assets/Events.gif").subsample(5,5)
    tk1.Button(frame5,image=image3,borderwidth=0,cursor="hand2",command=loadframe11).place(x=300,y=410)
    tk1.Label(frame5,text='EVENTS',font=("Arial",12),bg="white",foreground=mybgcol).place(x=350,y=380)
    image4=tk1.PhotoImage(file="assets/Bed Status.gif").subsample(5,5)
    tk1.Button(frame5,image=image4,borderwidth=0,cursor="hand2",command=loadframe8).place(x=900,y=10)
    tk1.Label(frame5,text='BED STATUS',font=("Arial",12),bg="white",foreground=mybgcol).place(x=960,y=230)
    tk1.Label(frame5,text='DASHBOARD',font=("Arial",50),foreground="white",bg=mybgcol).place(x=480,y=280)

#frame6, which contains the doctor my profile page
def loadframe6():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame5)
    clearwid(frame6)
    clearwid(frame7)
    frame6.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage3)
    widge=tk1.Label(frame6,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    b1=tk1.Button(frame6,text="DASHBOARD",font=("Arial",18),height=1,width=11,background="white",foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=loadframe5)
    b1.place(x=0,y=150)
    b2=tk1.Button(frame6,text="MY PROFILE",font=("Arial",18),height=1,width=11,background="white",foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=loadframe6)
    b2.place(x=0,y=200)
    b3=tk1.Button(frame6,text="MY PATIENTS",font=("Arial",18),height=1,width=11,background="white",foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=loadframe7)
    b3.place(x=0,y=250)
    b4=tk1.Button(frame6,text="EXIT APP",font=("Arial",18),height=1,width=11,background="white",foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=window1.destroy)
    b4.place(x=0,y=300)
    global userforprofile
    query="select * from doctors where username='{}';".format(userforprofile)
    cur.execute(query)
    z=cur.fetchall()
    for x in z:
        a,b,c,d,e,f,g,h,i,j=x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9]
    tk1.Label( frame6 , text = a,borderwidth=5,relief='ridge',bg="white",anchor='w',font=("Arial",15),foreground="black",width=60
               ).place(x=480,y=220)
    tk1.Label( frame6 , text = b,bg="white",font=("Arial",15),foreground="black",anchor='w',borderwidth=5,relief='ridge',width=60
               ).place(x=480,y=252)
    tk1.Label( frame6 , text = c,bg="white",font=("Arial",15),foreground="black",anchor='w',borderwidth=5,relief='ridge',width=60
               ).place(x=480,y=284)
    tk1.Label( frame6 , text = d,bg="white",font=("Arial",15),foreground="black",anchor='w' ,borderwidth=5,relief='ridge',width=60
               ).place(x=480,y=316)
    tk1.Label( frame6 , text = e,bg="white",font=("Arial",15),foreground="black",anchor='w',borderwidth=5,relief='ridge',width=60
               ).place(x=480,y=348)
    tk1.Label( frame6 , text = f,bg="white",font=("Arial",15),foreground="black",anchor='w',borderwidth=5,relief='ridge',width=60
               ).place(x=480,y=380)
    tk1.Label( frame6 , text = g,bg="white",font=("Arial",15),foreground="black",anchor='w',borderwidth=5,relief='ridge',width=60
               ).place(x=480,y=412)
    tk1.Label( frame6 , text = h,bg="white",font=("Arial",15),foreground="black",anchor='w',borderwidth=5,relief='ridge',width=60
               ).place(x=480,y=444)
    tk1.Label( frame6 , text = i,bg="white",font=("Arial",15),foreground="black",anchor='w',borderwidth=5,relief='ridge',width=60
               ).place(x=480,y=476)
    tk1.Label( frame6 , text = j,bg="white",font=("Arial",15),foreground="black",anchor='w',borderwidth=5,relief='ridge',width=60
               ).place(x=480,y=508)
    tk1.Label( frame6 , text = "DOCTOR ID",borderwidth=5,relief='ridge',bg="white",font=("Arial",15),anchor='w',
               foreground="black",width=25).place(x=200,y=220)
    tk1.Label( frame6 , text = "NAME",borderwidth=5,relief='ridge',bg="white",font=("Arial",15),anchor='w',
               foreground="black",width=25).place(x=200,y=252)
    tk1.Label( frame6 , text = "USERNAME",borderwidth=5,relief='ridge',bg="white",font=("Arial",15),anchor='w',
               foreground="black",width=25).place(x=200,y=284)
    tk1.Label( frame6 , text = "PHONE",borderwidth=5,relief='ridge',bg="white",font=("Arial",15),anchor='w',
               foreground="black",width=25).place(x=200,y=316)
    tk1.Label( frame6 , text = "EMAIL",borderwidth=5,relief='ridge',bg="white",font=("Arial",15),anchor='w',
               foreground="black",width=25).place(x=200,y=348)
    tk1.Label( frame6 , text = "ADDRESS",borderwidth=5,relief='ridge',bg="white",font=("Arial",15),anchor='w',
               foreground="black",width=25).place(x=200,y=380)
    tk1.Label( frame6 , text = "DATE OF BIRTH",borderwidth=5,relief='ridge',bg="white",font=("Arial",15),anchor='w',
               foreground="black",width=25).place(x=200,y=412)
    tk1.Label( frame6 , text = "DATE OF JOINING",borderwidth=5,relief='ridge',bg="white",font=("Arial",15),anchor='w',
               foreground="black",width=25).place(x=200,y=444)
    tk1.Label( frame6 , text = "DEPARTMENT",borderwidth=5,relief='ridge',bg="white",font=("Arial",15),anchor='w',
               foreground="black",width=25).place(x=200,y=476)
    tk1.Label( frame6 , text = "QUALIFICATION",borderwidth=5,relief='ridge',bg="white",font=("Arial",15),anchor='w',
               foreground="black",width=25).place(x=200,y=508)
    tk1.Label(frame6,text='MY PROFILE',font=("Arial",50),bg=mybgcol,foreground="white").place(x=480,y=100)
    
#creating frame7,which contains the my patients page, frame15(conatins patient reort) and frame39(edit patient report)is defined under frame7
def loadframe7():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame5)
    clearwid(frame6)
    clearwid(frame7)
    clearwid(frame15)
    clearwid(frame39)
    frame7.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage3)
    widge=tk1.Label(frame7,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    b1=tk1.Button(frame7,text="DASHBOARD",font=("Arial",18),height=1,width=11,background="white",foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=loadframe5)
    b1.place(x=0,y=150)
    b2=tk1.Button(frame7,text="MY PROFILE",font=("Arial",18),height=1,width=11,background="white",foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=loadframe6)
    b2.place(x=0,y=200)
    b3=tk1.Button(frame7,text="MY PATIENTS",font=("Arial",18),height=1,width=11,background="white",foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=loadframe7)
    b3.place(x=0,y=250)
    b4=tk1.Button(frame7,text="EXIT APP",font=("Arial",18),height=1,width=11,background="white",foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=window1.destroy)
    b4.place(x=0,y=300)
    tk1.Label(frame7,text='MY PATIENTS',font=("Arial",50),bg=mybgcol,foreground="white").place(x=480,y=100)
    sf = ScrolledFrame(frame7,height=360,width=900)
    sf.grid(row=7,column=8)
    sf.bind_arrow_keys(window1)
    sf.bind_scroll_wheel(window1)
    innerframe = sf.display_widget(tk1.Frame)
    global userforprofile
    query1="select Name from doctors where username='{}';".format(userforprofile)
    cur.execute(query1)
    z=cur.fetchone()
    k=z[0]
    query="select * from patient where doctor='{}' order by Doadmsn desc;".format(k)
    cur.execute(query)
    t=cur.fetchall()

    #frame39 edit patient report
    def loadframe39(x):
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame15)
        frame39.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame39,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        tk1.Label(frame39,text='EDIT REPORT',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
        tk1.Label(frame39,text='ENTER EDITED REPORT',anchor='w',font=("Calibri",30),bg="white",foreground=mybgcol,width=25).place(x=105,y=210)
        E1=tk1.Text(frame39,font=('Times',14),borderwidth=1,relief='solid',bg="white",fg="black",cursor="hand2",width=110,height=13)
        E1.place(x=110,y=260)
        def editrep():
            content=E1.get("1.0",tk1.END)
            query="update patient set remarks='{}' where remarks='{}'".format(content,x)
            cur.execute(query)
            con.commit()
            E1.delete("1.0",tk1.END)
            tk1.Label(frame39,text='REPORT UPDATED',anchor='w',font=("Calibri",14),bg="white",foreground=mybgcol,width=20).place(x=205,y=550)
        tk1.Button( frame39, text = "SUBMIT" ,font=("Arial",12),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white" ,command = editrep).place(x=550,y=550)
        tk1.Button(frame39,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe7).place(x=555,y=590)

    #frame15 which shows patient reports
    def loadframe15(x):
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame7)
        frame15.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame15,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        tk1.Label(frame15,text='REPORT',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
        b3=tk1.Button(frame15,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe7)
        b3.place(x=555,y=590)
        tk1.Label(frame15,text=x,borderwidth=5,relief='solid',anchor='nw',width=90,height=15, font=("Arial",15),
                  bg="white",foreground=mybgcol).place(x=120,y=200)
        b4=tk1.Button(frame15,text="EDIT",font=("Arial",12),foreground="white",bg=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=lambda: loadframe39(x))
        b4.place(x=1000,y=50)
        
    tk1.Label(innerframe,anchor='nw',text="P.ID",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=8).grid(row=1,column=0)
    tk1.Label(innerframe,anchor='nw',text="NAME",font=("Arial",14),borderwidth=5,relief='solid',bg=mybgcol,
              foreground="white",width=29).grid(row=1,column=3)
    tk1.Label(innerframe,anchor='nw',text="AGE",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=15).grid(row=1,column=5)
    tk1.Label(innerframe,anchor='nw',text="BLOOD GROUP",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=14).grid(row=1,column=7)
    tk1.Label(innerframe,anchor='nw',text="DOA",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=10).grid(row=1,column=9)

    global count
    count=2
    for x in t:
        a,b,c,d,e,f,g=x[0],x[1],x[2],x[3],x[4],x[5],x[6]
        tk1.Label(innerframe,anchor='nw',text=a,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=8).grid(row=count,column=0)
        tk1.Button(innerframe,anchor='nw',text=b,font=("Arial",12),borderwidth=4,relief='solid',cursor="hand2",bg="white",activebackground=mybgcol,
                   foreground="black",activeforeground="white",command=lambda tempf=f:loadframe15(tempf),width=35).grid(row=count,column=3)
        tk1.Label(innerframe,anchor='nw',text=c,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=15).grid(row=count,column=5)
        tk1.Label(innerframe,anchor='nw',text=d,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=14).grid(row=count,column=7)
        tk1.Label(innerframe,anchor='nw',text=g,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=10).grid(row=count,column=9)
        count+=1

#creating frame8, which contains the bed status
def loadframe8():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame5)
    frame8.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage2)
    widge=tk1.Label(frame8,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    
    def show():
       department=clicked.get()
       query="select * from beds where Department='{}';".format(department)
       cur.execute(query)  
       z=cur.fetchall()
       for i in z:
        a=i[0]
        b=i[1]
        c=i[2]
        
       tk1.Label( frame8 , text = "DEPARTMENT",bg="white",font=("Arial",15),
                  foreground=mybgcol ).place(x=180,y=370)
       tk1.Label( frame8 , text = "TOTAL BEDS",bg="white",font=("Arial",15),
                  foreground=mybgcol ).place(x=485,y=370)
       tk1.Label( frame8 , text = "AVAILABLE BEDS",bg="white",font=("Arial",15),
                  foreground=mybgcol ).place(x=685,y=370)
       tk1.Label( frame8 , text = department,width=40,bg="white",font=("Arial",15),
                  foreground="black",anchor='w' ).place(x=180,y=400)
       tk1.Label( frame8 , text = b,bg="white",font=("Arial",15),
                  foreground="black" ).place(x=520,y=400)
       tk1.Label( frame8 , text = c,bg="white",font=("Arial",15),
                  foreground="black" ).place(x=730,y=400)

       
    options = ['ICU','HDU','Cardiac Care Unit(CCU)', 'Intensive Cardiac Care Unit(ICCU)', 'Trauma Unit(ITU)'
               ,'OPS', 'Pediatrics','Surgical', 'General Medicine']
    clicked = tk1.StringVar()
    clicked.set( "ICU")
    tk1.Label( frame8 , text = "SELECT DEPARTMENT",bg="white",font=("Arial",15),foreground=mybgcol ).place(x=375,y=220)
    drop = tk1.OptionMenu( frame8 , clicked , *options )
    drop.config(width=40,font=("Times",15))
    drop.place(x=370,y=260)
    button = tk1.Button( frame8, text = "ENTER" ,font=("Arial",15),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white" ,command = show ).place(x=550,y=310)
    tk1.Label(frame8,text='BED STATUS',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
    b3=tk1.Button(frame8,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe5)
    b3.place(x=565,y=490)

#creating frame9, which contains circulars, there is also a frame 10(which shows circular details) defined inside frame 9
def loadframe9():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame5)
    clearwid(frame10)
    frame9.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage2)
    widge=tk1.Label(frame9,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    tk1.Label(frame9,text='CIRCULARS',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
    sf = ScrolledFrame(frame9,height=360,width=900)
    sf.grid(row=7,column=4)
    sf.bind_arrow_keys(window1)
    sf.bind_scroll_wheel(window1)
    inner_frame = sf.display_widget(tk1.Frame)
    query='select * from circulars order by DateOfIssue desc;'
    cur.execute(query)
    k=cur.rowcount
    z=cur.fetchall()

    #creating frame 10 whichshows circular details
    def loadframe10(x):
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame9)
        frame10.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame10,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        tk1.Label(frame10,text='CIRCULARS',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
        b3=tk1.Button(frame10,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe9)
        b3.place(x=555,y=590)
        tk1.Label(frame10,text=x,borderwidth=5,relief='solid',anchor='nw',width=90,height=15, font=("Arial",15),bg="white",foreground=mybgcol).place(x=120,y=200)
        
        
    tk1.Label(inner_frame,anchor='nw',text="DATE",font=("Arial",14),bg=mybgcol,borderwidth=3,relief='solid',foreground="white",width=10).grid(row=1,column=0)
    tk1.Label(inner_frame,anchor='nw',text="TITLE",font=("Arial",14),borderwidth=3,relief='solid',bg=mybgcol,foreground="white",width=52).grid(row=1,column=3)
    tk1.Label(inner_frame,anchor='nw',text="ISSUED BY",font=("Arial",14),bg=mybgcol,borderwidth=3,relief='solid',foreground="white",width=17).grid(row=1,column=5)

    global count
    count=2
    for x in z:
        a,b,c,d=x[0],x[1],x[2],x[3]
        tk1.Label(inner_frame,anchor='nw',text=a,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=10).grid(row=count,column=0)
        tk1.Button(inner_frame,anchor='nw',text=b,font=("Arial",12),borderwidth=3,relief='solid',cursor="hand2",bg="white",activebackground=mybgcol,
                   foreground="black",activeforeground="white",command=lambda tempc=c:loadframe10(tempc),width=63).grid(row=count,column=3)
        tk1.Label(inner_frame,anchor='nw',text=d,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=17).grid(row=count,column=5)
        count+=1
    b3=tk1.Button(frame9,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe5)
    b3.place(x=555,y=590)

#creating frame11 which contains events, frame12(which shows event details) is defined under frame11
def loadframe11():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame5)
    clearwid(frame12)
    frame11.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage2)
    widge=tk1.Label(frame11,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    tk1.Label(frame11,text='EVENTS',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
    sf = ScrolledFrame(frame11,height=360,width=900)
    sf.grid(row=7,column=4)
    sf.bind_arrow_keys(window1)
    sf.bind_scroll_wheel(window1)
    innerframe = sf.display_widget(tk1.Frame)
    query='select * from events order by DateOfIssue desc;'
    cur.execute(query)
    k=cur.rowcount
    z=cur.fetchall()

    #frame12 shows event details
    def loadframe12(x):
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame11)
        frame12.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame12,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        tk1.Label(frame12,text='EVENTS',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
        b3=tk1.Button(frame12,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe11)
        b3.place(x=555,y=590)
        tk1.Label(frame12,text=x,borderwidth=5,relief='solid',anchor='nw',width=90,height=15, font=("Arial",15),bg="white",foreground=mybgcol).place(x=120,y=200)
        
        
    tk1.Label(innerframe,anchor='nw',text="EVENT DATE",font=("Arial",14),bg=mybgcol,borderwidth=4,relief='solid',foreground="white",width=12).grid(row=1,column=0)
    tk1.Label(innerframe,anchor='nw',text="EVENT NAME",font=("Arial",14),borderwidth=4,relief='solid',bg=mybgcol,foreground="white",width=50).grid(row=1,column=3)
    tk1.Label(innerframe,anchor='nw',text="DATE OF ISSUE",font=("Arial",14),bg=mybgcol,borderwidth=4,relief='solid',foreground="white",width=16).grid(row=1,column=5)

    global count
    count=2
    for x in z:
        a,b,c,d=x[0],x[1],x[2],x[3]
        tk1.Label(innerframe,anchor='nw',text=a,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=12).grid(row=count,column=0)
        tk1.Button(innerframe,anchor='nw',text=b,font=("Arial",12),borderwidth=3,relief='solid',cursor="hand2",bg="white",activebackground=mybgcol,
                   foreground="black",activeforeground="white",command=lambda tempd=d:loadframe12(tempd),width=61).grid(row=count,column=3)
        tk1.Label(innerframe,anchor='nw',text=c,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=16).grid(row=count,column=5)
        count+=1
    b3=tk1.Button(frame11,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe5)
    b3.place(x=555,y=590)


#creating frame13, which contains schedules, frame14(which shows day wise shift allotment) is defined under frame13
def loadframe13():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame5)
    clearwid(frame14)
    frame13.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage2)
    widge=tk1.Label(frame13,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    tk1.Label(frame13,text='SCHEDULE',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
    sf = ScrolledFrame(frame13,height=360,width=900)
    sf.grid(row=7,column=4)
    sf.bind_arrow_keys(window1)
    sf.bind_scroll_wheel(window1)
    innerframe1 = sf.display_widget(tk1.Frame)
    query='select distinct weekstart,week_end from schedule order by weekstart desc;'
    cur.execute(query)
    z=cur.fetchall()

    #frame14 which shows day-wise shift allotment
    def loadframe14(x):
        clearwid(frame13)
        if cur.rowcount>0:
            cur.fetchall()
        frame14.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame14,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        tk1.Label(frame14,text='SCHEDULE',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
        global userforprofile
        query1="select docid from doctors where username='{}';".format(userforprofile)
        cur.execute(query1)
        z=cur.fetchone()
        query="select day,shift from schedule where weekstart='{}' and docid='{}';".format(x,z[0])
        cur.execute(query)
        k=cur.fetchall()
        
        tk1.Label(frame14,text="DAY",borderwidth=5,relief='solid',anchor='nw',width=25,
                  font=("Arial",15),bg=mybgcol,foreground="white").place(x=300,y=200)
        tk1.Label(frame14,text="SHIFT",borderwidth=5,relief='solid',anchor='nw',width=25,
                  font=("Arial",15),bg=mybgcol,foreground="white").place(x=580,y=200)
        days=('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
        check=[]
        for x in days:
            for y in k:
                if y[0]==x:
                    check=check+[y[0]]
        for x in days:
            if x not in check:
                k=k+[(x,"NO SHIFT")]
        t=['','','','','','','']
        for x in k:
            if x[0]=='Monday':
                t[0]=x
            if x[0]=='Tuesday':
                t[1]=x
            if x[0]=='Wednesday':
                t[2]=x
            if x[0]=='Thursday':
                t[3]=x
            if x[0]=='Friday':
                t[4]=x
            if x[0]=='Saturday':
                t[5]=x
            if x[0]=='Sunday':
                t[6]=x
            
        tk1.Label(frame14,text=t[0][0],borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=300,y=232)
        tk1.Label(frame14,text=t[0][1],borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=580,y=232)
        tk1.Label(frame14,text=t[1][0],borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=300,y=264)
        tk1.Label(frame14,text=t[1][1],borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=580,y=264)
        tk1.Label(frame14,text=t[2][0],borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=300,y=296)
        tk1.Label(frame14,text=t[2][1],borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=580,y=296)
        tk1.Label(frame14,text=t[3][0],borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=300,y=326)
        tk1.Label(frame14,text=t[3][1],borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=580,y=326)
        tk1.Label(frame14,text=t[4][0],borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=300,y=358)
        tk1.Label(frame14,text=t[4][1],borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=580,y=358)
        tk1.Label(frame14,text=t[5][0],borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=300,y=390)
        tk1.Label(frame14,text=t[5][1],borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=580,y=390)
        tk1.Label(frame14,text=t[6][0],borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=300,y=422)
        tk1.Label(frame14,text=t[6][1],borderwidth=5,relief='solid',anchor='nw',width=25,
                font=("Arial",15),bg="white",foreground="black").place(x=580,y=422)
        b3=tk1.Button(frame14,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe13)
        b3.place(x=555,y=590)
        
        
        
    tk1.Label(innerframe1,anchor='nw',text="WEEK START",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',foreground="white",width=15).grid(row=1,column=0)
    tk1.Label(innerframe1,anchor='nw',text="WEEK END",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',foreground="white",width=15).grid(row=1,column=1)
    tk1.Label(innerframe1,anchor='nw',text="TITLE",font=("Arial",14),borderwidth=5,relief='solid',bg=mybgcol,
              foreground="white",width=48).grid(row=1,column=2)
    
    global count
    count=2
    for x in z:
        a,b=x[0],x[1]
        tk1.Label(innerframe1,anchor='nw',text=a,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=15).grid(row=count,column=0)
        tk1.Label(innerframe1,anchor='nw',text=b,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=15).grid(row=count,column=1)
        tk1.Button(innerframe1,anchor='nw',text="Weekly Schedule",font=("Arial",12),borderwidth=3,relief='solid',cursor="hand2",bg="white",activebackground=mybgcol,
                   foreground="black",activeforeground="white",command=lambda tempa=a:loadframe14(tempa),width=59).grid(row=count,column=2)
        count+=1
    b3=tk1.Button(frame13,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe5)
    b3.place(x=555,y=590)

#coding for the admin side begins here
    
#frame2, containing the admin sign in sign up page
def loadframe2():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame1)
    clearwid(frame4)
    clearwid(frame16)
    frame2.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage1)
    widge=tk1.Label(frame2,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    b1=tk1.Button(frame2,text="SIGN IN",font=("Arial",15),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=loadframe4)
    b1.place(x=543,y=340)
    b2=tk1.Button(frame2,text="SIGN UP",font=("Arial",15),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=loadframe16)
    b2.place(x=540,y=390)
    tk1.Label(frame2,text='ADMIN LOGIN',font=("Arial",30),bg="white",foreground=mybgcol).place(x=460,y=210)
    b3=tk1.Button(frame2,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe1)
    b3.place(x=555,y=490)

#frame4, containing the admin sign in page
def loadframe4():
    if cur.rowcount>0:
        cur.fetchall()
    frame4.tkraise()
    clearwid(frame2)
    photo1=tk1.PhotoImage(file=mybgimage1)
    widge=tk1.Label(frame4,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    tk1.Label(frame4,text='ADMIN SIGN IN',bg="white",font=("Arial",30),foreground=mybgcol).place(x=460,y=210)
    tk1.Label(frame4,text='USERNAME',bg="white",font=("Calibri",20),foreground=mybgcol).place(x=300,y=300)
    E1=tk1.Entry(frame4,font=('Times',20),bg=mybgcol,fg="white",cursor="hand2")
    E1.place(x=470,y=300)
    tk1.Label(frame4,text='PASSWORD',bg="white",font=("Calibri",20),foreground=mybgcol).place(x=300,y=400)
    E2=tk1.Entry(frame4,font=('Times',20),show='*',bg=mybgcol,fg="white",cursor="hand2")
    E2.place(x=470,y=400)
    
    def submitsignin():
        global userforadmin
        user=E1.get()
        userforadmin=user
        psw=E2.get()
        query="select password ,name from admin where Username='{}'".format(user)
        cur.execute(query)
        k=cur.fetchone()
        if cur.rowcount==0:
            tk1.Label(frame4,text="USER NOT FOUND",width=20,bg="white",font=("Arial",18),foreground=mybgcol).place(x=480,y=520)
            E1.delete(0,tk1.END)
            E2.delete(0,tk1.END)
        else:
            a=k[0]
            global adminname
            adminname=k[1]
            if psw==a:
                loadframe17()
            else:
                tk1.Label(frame4,text="INCORRECT PASSWORD",width=20,bg="white",font=("Arial",18),foreground=mybgcol).place(x=480,y=520)
                E2.delete(0,tk1.END)
        cur.fetchall()
    b1=tk1.Button(frame4,text="SUBMIT",font=("Arial",18),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,width=12,activeforeground="white",command=submitsignin)
    b1.place(x=512,y=460)
    b2=tk1.Button(frame4,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe2)
    b2.place(x=575,y=590)

#frame16,the admin sign up screen
def loadframe16():
    if cur.rowcount>0:
        cur.fetchall()
    frame16.tkraise()
    clearwid(frame2)
    photo1=tk1.PhotoImage(file=mybgimage1)
    widge=tk1.Label(frame16,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    tk1.Label(frame16,text='ADMIN SIGN UP',anchor='w',bg="white",font=("Arial",30),foreground=mybgcol).place(x=460,y=210)
    tk1.Label(frame16,text='ADMIN VERIFICATION CODE',borderwidth=2,relief='solid',anchor='w',
              bg=mybgcol,font=("Calibri",15),foreground="white",width=25).place(x=305,y=280)
    E7=tk1.Entry(frame16,font=('Times',17),show='*',borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
    E7.place(x=560,y=458)
    tk1.Label(frame16,text='NAME',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
              font=("Calibri",15),foreground="white",width=25).place(x=305,y=310)
    E1=tk1.Entry(frame16,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
    E1.place(x=560,y=280)
    tk1.Label(frame16,text='PHONE',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
              font=("Calibri",15),foreground="white",width=25).place(x=305,y=340)
    E2=tk1.Entry(frame16,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
    E2.place(x=560,y=310)
    tk1.Label(frame16,text='EMAIL',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
              font=("Calibri",15),foreground="white",width=25).place(x=305,y=370)
    E3=tk1.Entry(frame16,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
    E3.place(x=560,y=340)
    tk1.Label(frame16,text='USERNAME',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
              font=("Calibri",15),foreground="white",width=25).place(x=305,y=400)
    E4=tk1.Entry(frame16,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
    E4.place(x=560,y=370)
    tk1.Label(frame16,text='PASSWORD',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
              font=("Calibri",15),foreground="white",width=25).place(x=305,y=430)
    E5=tk1.Entry(frame16,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
    E5.place(x=560,y=400)
    tk1.Label(frame16,text='CONFIRM PASSWORD',anchor='w',borderwidth=2,relief='solid',
              bg=mybgcol,font=("Calibri",15),foreground="white",width=25).place(x=305,y=460)
    E6=tk1.Entry(frame16,font=('Times',17),borderwidth=2,relief='solid',show='*',bg="white",fg="black",cursor="hand2",width=30)
    E6.place(x=560,y=430)
    
    def submitsignin():
        global adminverification
        verify=E1.get()
        password=E6.get()
        passwordcheck=E7.get()
        name=E2.get()
        phone=E3.get()
        email=E4.get()
        username=E5.get()
        if verify==adminverification:
            query="select ID,username from admin;"
            cur.execute(query)
            k=cur.fetchall()
            userfound=False
            for x in k:
                if x[1]==username:
                    userfound=True
            if userfound==False:
                if password==passwordcheck:
                    for x in range(1,1000):
                        tempid='A'+str(x)
                        found=False
                        for y in k:
                            if y[0]==tempid:
                                found=True
                        if found==False:
                            adminid=tempid
                            break
                    query1="insert into admin values('{}','{}','{}','{}','{}','{}');".format(adminid,name,phone,email,username,password)
                    cur.execute(query1)
                    con.commit()
                    tk1.Label(frame16,text="SIGN UP SUCCESFUL",width=40,bg="white",font=("Arial",12),foreground=mybgcol).place(x=460,y=550)
                    b2=tk1.Button(frame16,text="PROCEED",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                    activebackground=mybgcol,activeforeground="white",command=loadframe4)
                    b2.place(x=565,y=590)
                else:
                    tk1.Label(frame16,text="PASSWORD DOES NOT MATCH",width=40,bg="white",font=("Arial",12),foreground=mybgcol).place(x=460,y=550)
            else:
                tk1.Label(frame16,text="USERNAME ALREADY EXISTS",width=40,bg="white",font=("Arial",12),foreground=mybgcol).place(x=460,y=550)
        else:
            tk1.Label(frame16,text="INCORRECT VERIFICATION CODE",width=40,bg="white",font=("Arial",12),foreground=mybgcol).place(x=460,y=550)
    b1=tk1.Button(frame16,text="SUBMIT",font=("Arial",16),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,width=16,activeforeground="white",command=submitsignin)
    b1.place(x=500,y=500)
    b2=tk1.Button(frame16,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe2)
    b2.place(x=565,y=590)

#creating frame17, the admin dashboard
def loadframe17():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame22)
    clearwid(frame19)
    clearwid(frame18)
    clearwid(frame27)
    clearwid(frame29)
    clearwid(frame31)
    clearwid(frame36)
    clearwid(frame41)
    frame17.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage4)
    widge=tk1.Label(frame17,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    global sphoto
    global cphoto
    global ephoto
    global bphoto
    global dphoto
    global iphoto
    global pphoto
    global blank
    global fphoto
    global pfphoto
    blank=tk1.PhotoImage(file="assets/Blank.gif").subsample(6,6)
    tk1.Button(frame17,image=blank,borderwidth=0).place(x=532,y=270)
    pfphoto=tk1.PhotoImage(file="assets/ProfileAdmin.gif").subsample(20,20)
    tk1.Button(frame17,image=pfphoto,borderwidth=0,highlightthickness=0,cursor="hand2",command=loadframe43).place(x=1030,y=8)
    fphoto=tk1.PhotoImage(file="assets/Finance.gif").subsample(6,6)
    tk1.Button(frame17,image=fphoto,borderwidth=0,cursor="hand2",command=loadframe41).place(x=714,y=270)
    tk1.Label(frame17,text='FINANCE',font=("Arial",10),foreground="white",bg=mybgcol,width=10).place(x=755,y=290)
    bphoto=tk1.PhotoImage(file="assets/Bed Status.gif").subsample(6,6)
    tk1.Button(frame17,image=bphoto,borderwidth=0,cursor="hand2",command=loadframe27).place(x=350,y=270)
    tk1.Label(frame17,text='BED STATUS',font=("Arial",10),foreground="white",bg=mybgcol,width=10).place(x=400,y=290)
    sphoto=tk1.PhotoImage(file="assets/Schedule.gif").subsample(6,6)
    tk1.Button(frame17,image=sphoto,borderwidth=0,cursor="hand2",command=loadframe18).place(x=350,y=100)
    tk1.Label(frame17,text='SCHEDULE',font=("Arial",10),foreground="white",bg=mybgcol,width=10).place(x=400,y=101)
    ephoto=tk1.PhotoImage(file="assets/Events.gif").subsample(6,6)
    tk1.Button(frame17,image=ephoto,borderwidth=0,cursor="hand2",command=loadframe22).place(x=532,y=100)
    tk1.Label(frame17,text='EVENTS',font=("Arial",10),foreground="white",bg=mybgcol,width=10).place(x=572,y=101)
    dphoto=tk1.PhotoImage(file="assets/Doctors.gif").subsample(6,6)
    tk1.Button(frame17,image=dphoto,borderwidth=0,cursor="hand2",command=loadframe36).place(x=532,y=440)
    tk1.Label(frame17,text='DOCTORS',font=("Arial",10),foreground="white",bg=mybgcol,width=10).place(x=572,y=441)
    iphoto=tk1.PhotoImage(file="assets/Inventory.gif").subsample(6,6)
    tk1.Button(frame17,image=iphoto,borderwidth=0,cursor="hand2",command=loadframe29).place(x=350,y=440)
    tk1.Label(frame17,text='INVENTORY',font=("Arial",10),foreground="white",bg=mybgcol,width=10).place(x=400,y=441)
    pphoto=tk1.PhotoImage(file="assets/Patients.gif").subsample(6,6)
    tk1.Button(frame17,image=pphoto,borderwidth=0,cursor="hand2",command=loadframe31).place(x=714,y=100)
    tk1.Label(frame17,text='PATIENTS',font=("Arial",10),foreground="white",bg=mybgcol,width=10).place(x=755,y=101)
    cphoto=tk1.PhotoImage(file="assets/Circulars.gif").subsample(6,6)
    tk1.Button(frame17,image=cphoto,borderwidth=0,cursor="hand2",command=loadframe19).place(x=714,y=440)
    tk1.Label(frame17,text='CIRCULARS',font=("Arial",10),foreground="white",bg=mybgcol,width=10).place(x=755,y=441)
    tk1.Label(frame17,text='ADMIN',font=("Arial",19),foreground="white",bg=mybgcol).place(x=580,y=320)
    tk1.Label(frame17,text='DASHBOARD',font=("Arial",19),foreground="white",bg=mybgcol).place(x=540,y=370)
    tk1.Button(frame17,text="EXIT APP",font=("Arial",10),height=1,width=7,background="white",foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=window1.destroy).place(x=1100,y=20)
    
#frame18,the admin schedule page frame25(day wise shift) and frame 26(add new schedule) also defined under it
def loadframe18():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame17)
    clearwid(frame25)
    clearwid(frame26)
    frame18.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage2)
    widge=tk1.Label(frame18,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    tk1.Label(frame18,text='SCHEDULE',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
    sf = ScrolledFrame(frame18,height=360,width=900)
    sf.grid(row=7,column=4)
    sf.bind_arrow_keys(window1)
    sf.bind_scroll_wheel(window1)
    innerframe1 = sf.display_widget(tk1.Frame)
    query='select distinct weekstart,week_end from schedule order by weekstart desc;'
    cur.execute(query)
    z=cur.fetchall()

    #frame25 which shows day-wise shift allotment
    def loadframe25(x):
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame18)
        frame25.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame25,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        tk1.Label(frame25,text='SCHEDULE',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
        query="select Docid,docname,day,shift from schedule where weekstart='{}'ORDER BY FIELD(day, 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY');".format(x,z[0])
        cur.execute(query)
        k=cur.fetchall()
        sf1 = ScrolledFrame(frame25,height=360,width=900)
        sf1.grid(row=7,column=4)
        sf1.bind_arrow_keys(window1)
        sf1.bind_scroll_wheel(window1)
        innerframe2 = sf1.display_widget(tk1.Frame)
        tk1.Label(innerframe2,anchor='nw',text="DOCID",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',foreground="white",width=15).grid(row=1,column=0)
        tk1.Label(innerframe2,anchor='nw',text="DOCTOR NAME",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',foreground="white",width=25).grid(row=1,column=1)
        tk1.Label(innerframe2,anchor='nw',text="DAY",font=("Arial",14),borderwidth=5,relief='solid',bg=mybgcol,
              foreground="white",width=15).grid(row=1,column=2)
        tk1.Label(innerframe2,anchor='nw',text="SHIFT",font=("Arial",14),borderwidth=5,relief='solid',bg=mybgcol,
              foreground="white",width=20).grid(row=1,column=3)
        global count1
        count1=2
        for x in k:
            a,b,c,d=x[0],x[1],x[2],x[3]
            tk1.Label(innerframe2,anchor='nw',text=a,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=15).grid(row=count1,column=0)
            tk1.Label(innerframe2,anchor='nw',text=b,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=25).grid(row=count1,column=1)
            tk1.Label(innerframe2,anchor='nw',text=c,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=15).grid(row=count1,column=2)
            tk1.Label(innerframe2,anchor='nw',text=d,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=20).grid(row=count1,column=3)
            count1+=1
        b1=tk1.Button(frame25,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                      activebackground=mybgcol,activeforeground="white",command=loadframe18)
        b1.place(x=555,y=590)

    #frame26 for adding schedule
    def loadframe26():
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame18)
        frame26.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame26,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        tk1.Label(frame26,text='SCHEDULE',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
        tk1.Label(frame26,text='WEEK START',borderwidth=2,relief='solid',anchor='w',
                  bg=mybgcol,font=("Calibri",15),foreground="white",width=25).place(x=305,y=230)
        tk1.Label(frame26,text='WEEK END',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=260)
        E1=tk1.Entry(frame26,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E1.place(x=560,y=230)
        tk1.Label(frame26,text='DAY',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=290)
        E2=tk1.Entry(frame26,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E2.place(x=560,y=260)
        tk1.Label(frame26,text='SHIFT',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=320)
        E3=tk1.Entry(frame26,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E3.place(x=560,y=290)
        tk1.Label(frame26,text='DOCTOR NAME',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=350)
        E4=tk1.Entry(frame26,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E4.place(x=560,y=320)
        E5=tk1.Entry(frame26,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E5.place(x=560,y=350)
        E1.insert(0,'yyyy-mm-dd')
        E2.insert(0,'yyyy-mm-dd')
        
        def submitschedule():
            global adminname
            startdate=E1.get()
            enddate=E2.get()
            day=E3.get()
            shift=E4.get()
            docname=E5.get()
            query1="select docid from doctors where name='{}';".format(docname)
            cur.execute(query1)
            docid=cur.fetchone()[0]
            query2="insert into schedule values('{}','{}','{}','{}','{}','{}');".format(day,shift,docname,docid,startdate,enddate)
            cur.execute(query2)
            con.commit()
            E1.delete(0,tk1.END)
            E2.delete(0,tk1.END)
            E3.delete(0,tk1.END)
            E4.delete(0,tk1.END)
            E5.delete(0,tk1.END)
            tk1.Label(frame26,text='SCHEDULE UPDATED',anchor='w',font=("Calibri",14),bg="white",foreground=mybgcol,width=20).place(x=205,y=550)      
        b1=tk1.Button(frame26,text="SUBMIT",font=("Arial",16),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,width=16,activeforeground="white",command=submitschedule)
        b1.place(x=500,y=540)
        b2=tk1.Button(frame26,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                          activebackground=mybgcol,activeforeground="white",command=loadframe18)
        b2.place(x=565,y=590)  
    tk1.Label(innerframe1,anchor='nw',text="WEEK START",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',foreground="white",width=15).grid(row=1,column=0)
    tk1.Label(innerframe1,anchor='nw',text="WEEK END",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',foreground="white",width=15).grid(row=1,column=1)
    tk1.Label(innerframe1,anchor='nw',text="TITLE",font=("Arial",14),borderwidth=5,relief='solid',bg=mybgcol,
              foreground="white",width=48).grid(row=1,column=2)
    
    global count
    count=2
    for x in z:
        a,b=x[0],x[1]
        tk1.Label(innerframe1,anchor='nw',text=a,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=15).grid(row=count,column=0)
        tk1.Label(innerframe1,anchor='nw',text=b,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=15).grid(row=count,column=1)
        tk1.Button(innerframe1,anchor='nw',text="Weekly Schedule",font=("Arial",12),borderwidth=3,relief='solid',cursor="hand2",bg="white",activebackground=mybgcol,
                   foreground="black",activeforeground="white",command=lambda tempa=a:loadframe25(tempa),width=59).grid(row=count,column=2)
        count+=1
    b3=tk1.Button(frame18,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe17)
    b3.place(x=555,y=590)
    b4=tk1.Button(frame18,text="EDIT",font=("Arial",12),foreground="white",bg=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe26)
    b4.place(x=1000,y=50)

#frame19, containing circulars also contains frame 20(circular details) and frame 21(add new circular)
def loadframe19():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame17)
    clearwid(frame20)
    clearwid(frame21)
    frame19.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage2)
    widge=tk1.Label(frame19,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    tk1.Label(frame19,text='CIRCULARS',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
    sf = ScrolledFrame(frame19,height=360,width=900)
    sf.grid(row=7,column=4)
    sf.bind_arrow_keys(window1)
    sf.bind_scroll_wheel(window1)
    inner_frame = sf.display_widget(tk1.Frame)
    query='select * from circulars order by DateOfIssue desc;'
    cur.execute(query)
    k=cur.rowcount
    z=cur.fetchall()

    #creating frame 20 whichshows circular details
    def loadframe20(x):
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame19)
        frame20.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame20,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        tk1.Label(frame20,text='CIRCULARS',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
        b3=tk1.Button(frame20,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe19)
        b3.place(x=555,y=590)
        tk1.Label(frame20,text=x,borderwidth=5,relief='solid',anchor='nw',width=90,height=15, font=("Arial",15),bg="white",foreground=mybgcol).place(x=120,y=200)

    #frame21 add new circular
    def loadframe21():
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame19)
        frame21.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame21,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        tk1.Label(frame21,text='CIRCULARS',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
        tk1.Label(frame21,text='TITLE',borderwidth=2,relief='solid',anchor='w',
                  bg=mybgcol,font=("Calibri",15),foreground="white",width=25).place(x=105,y=180)
        E1=tk1.Entry(frame21,font=('Times',17),borderwidth=1,relief='solid',bg="white",fg="black",cursor="hand2",width=50)
        E1.place(x=360,y=180)
        tk1.Label(frame21,text='CONTENT',anchor='w',font=("Calibri",30),bg="white",foreground=mybgcol,width=25).place(x=105,y=210)
        E2=tk1.Text(frame21,font=('Times',14),borderwidth=1,relief='solid',bg="white",fg="black",cursor="hand2",width=110,height=13)
        E2.place(x=110,y=260)

        def submitcircular():
            global adminname
            title=E1.get()
            content=E2.get("1.0",tk1.END)
            query1="select curdate();"
            cur.execute(query1)
            dateofissue=cur.fetchone()[0]
            query2="insert into circulars values('{}','{}','{}','{}');".format(dateofissue,title,content,adminname)
            cur.execute(query2)
            con.commit()
            E1.delete(0,tk1.END)
            E2.delete("1.0",tk1.END)
            tk1.Label(frame21,text='CIRCULAR ISSUED',anchor='w',font=("Calibri",14),bg="white",foreground=mybgcol,width=20).place(x=205,y=550)
            
            
        b1=tk1.Button(frame21,text="SUBMIT",font=("Arial",16),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,width=16,activeforeground="white",command=submitcircular)
        b1.place(x=500,y=540)
        b2=tk1.Button(frame21,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                      activebackground=mybgcol,activeforeground="white",command=loadframe19)
        b2.place(x=565,y=590)
        
    tk1.Label(inner_frame,anchor='nw',text="DATE",font=("Arial",14),bg=mybgcol,borderwidth=3,relief='solid',foreground="white",width=10).grid(row=1,column=0)
    tk1.Label(inner_frame,anchor='nw',text="TITLE",font=("Arial",14),borderwidth=3,relief='solid',bg=mybgcol,foreground="white",width=52).grid(row=1,column=3)
    tk1.Label(inner_frame,anchor='nw',text="ISSUED BY",font=("Arial",14),bg=mybgcol,borderwidth=3,relief='solid',foreground="white",width=17).grid(row=1,column=5)

    global count
    count=2
    for x in z:
        a,b,c,d=x[0],x[1],x[2],x[3]
        tk1.Label(inner_frame,anchor='nw',text=a,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=10).grid(row=count,column=0)
        tk1.Button(inner_frame,anchor='nw',text=b,font=("Arial",12),borderwidth=3,relief='solid',cursor="hand2",bg="white",activebackground=mybgcol,
                   foreground="black",activeforeground="white",command=lambda tempc=c:loadframe20(tempc),width=63).grid(row=count,column=3)
        tk1.Label(inner_frame,anchor='nw',text=d,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=17).grid(row=count,column=5)
        count+=1
    b3=tk1.Button(frame19,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe17)
    b3.place(x=555,y=590)
    b4=tk1.Button(frame19,text="ADD NEW",font=("Arial",12),foreground="white",bg=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe21)
    b4.place(x=1000,y=50)

#frame22 containing the events page frame 23(event details) and frame24(add new event) also defined under this frame
def loadframe22():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame17)
    clearwid(frame23)
    clearwid(frame24)
    frame22.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage2)
    widge=tk1.Label(frame22,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    tk1.Label(frame22,text='EVENTS',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
    sf = ScrolledFrame(frame22,height=360,width=900)
    sf.grid(row=7,column=4)
    sf.bind_arrow_keys(window1)
    sf.bind_scroll_wheel(window1)
    inner_frame = sf.display_widget(tk1.Frame)
    query='select * from events order by DateOfIssue desc;'
    cur.execute(query)
    k=cur.rowcount
    z=cur.fetchall()

    #creating frame 23 whichshows EVENT details
    def loadframe23(x):
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame22)
        frame23.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame23,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        tk1.Label(frame23,text='EVENTS',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
        b3=tk1.Button(frame23,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe22)
        b3.place(x=555,y=590)
        tk1.Label(frame23,text=x,borderwidth=5,relief='solid',anchor='nw',width=90,height=15, font=("Arial",15),bg="white",foreground=mybgcol).place(x=120,y=200)

    #frame24 add new event   
    def loadframe24():
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame22)
        frame24.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame24,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        tk1.Label(frame24,text='EVENTS',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
        tk1.Label(frame24,text='TITLE',borderwidth=2,relief='solid',anchor='w',
                  bg=mybgcol,font=("Calibri",15),foreground="white",width=13).place(x=105,y=180)
        E1=tk1.Entry(frame24,font=('Times',17),borderwidth=1,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E1.place(x=240,y=180)
        tk1.Label(frame24,text='EVENT DATE',borderwidth=2,relief='solid',anchor='w',
                  bg=mybgcol,font=("Calibri",15),foreground="white",width=13).place(x=585,y=180)
        E3=tk1.Entry(frame24,font=('Times',17),borderwidth=1,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E3.place(x=720,y=180)
        E3.insert(0,'yyyy-mm-dd')
        tk1.Label(frame24,text='CONTENT',anchor='w',font=("Calibri",30),bg="white",foreground=mybgcol,width=25).place(x=105,y=210)
        E2=tk1.Text(frame24,font=('Times',14),borderwidth=1,relief='solid',bg="white",fg="black",cursor="hand2",width=110,height=13)
        E2.place(x=110,y=260)

        def submitevent():
            title=E1.get()
            eventdate=E3.get()
            content=E2.get("1.0",tk1.END)
            query1="select curdate();"
            cur.execute(query1)
            dateofissue=cur.fetchone()[0]
            query2="insert into events values('{}','{}','{}','{}');".format(dateofissue,title,eventdate,content)
            cur.execute(query2)
            con.commit()
            E1.delete(0,tk1.END)
            E3.delete(0,tk1.END)
            E2.delete("1.0",tk1.END)
            tk1.Label(frame24,text='EVENT ISSUED',anchor='w',font=("Calibri",14),bg="white",foreground=mybgcol,width=20).place(x=205,y=550)
            
            
        b1=tk1.Button(frame24,text="SUBMIT",font=("Arial",16),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,width=16,activeforeground="white",command=submitevent)
        b1.place(x=500,y=540)
        b2=tk1.Button(frame24,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                      activebackground=mybgcol,activeforeground="white",command=loadframe22)
        b2.place(x=565,y=590)
        
    tk1.Label(inner_frame,anchor='nw',text="EVENT DATE",font=("Arial",14),bg=mybgcol,borderwidth=4,relief='solid',foreground="white",width=12).grid(row=1,column=0)
    tk1.Label(inner_frame,anchor='nw',text="EVENT NAME",font=("Arial",14),borderwidth=4,relief='solid',bg=mybgcol,foreground="white",width=50).grid(row=1,column=3)
    tk1.Label(inner_frame,anchor='nw',text="DATE OF ISSUE",font=("Arial",14),bg=mybgcol,borderwidth=4,relief='solid',foreground="white",width=16).grid(row=1,column=5)

    global count
    count=2
    for x in z:
        a,b,c,d=x[0],x[1],x[2],x[3]
        tk1.Label(inner_frame,anchor='nw',text=a,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=12).grid(row=count,column=0)
        tk1.Button(inner_frame,anchor='nw',text=b,font=("Arial",12),borderwidth=3,relief='solid',cursor="hand2",bg="white",activebackground=mybgcol,
                   foreground="black",activeforeground="white",command=lambda tempd=d:loadframe23(tempd),width=61).grid(row=count,column=3)
        tk1.Label(inner_frame,anchor='nw',text=c,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=16).grid(row=count,column=5)
        count+=1
    b3=tk1.Button(frame22,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe17)
    b3.place(x=555,y=590)
    b4=tk1.Button(frame22,text="ADD NEW",font=("Arial",12),foreground="white",bg=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe24)
    b4.place(x=1000,y=50)

#frame27 bed status admin side, frame28(edit bed status) also defined under it
def loadframe27():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame17)
    clearwid(frame28)
    frame27.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage2)
    widge=tk1.Label(frame27,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    
    def show():
       department=clicked.get()
       query="select * from beds where Department='{}';".format(department)
       cur.execute(query)  
       z=cur.fetchall()
       for i in z:
        a=i[0]
        b=i[1]
        c=i[2]
        
       tk1.Label( frame27 , text = "DEPARTMENT",bg="white",font=("Arial",15),
                  foreground=mybgcol ).place(x=180,y=370)
       tk1.Label( frame27, text = "TOTAL BEDS",bg="white",font=("Arial",15),
                  foreground=mybgcol ).place(x=485,y=370)
       tk1.Label( frame27, text = "AVAILABLE BEDS",bg="white",font=("Arial",15),
                  foreground=mybgcol ).place(x=685,y=370)
       tk1.Label( frame27, text = department,width=40,bg="white",font=("Arial",15),
                  foreground="black",anchor='w' ).place(x=180,y=400)
       tk1.Label( frame27, text = b,bg="white",font=("Arial",15),
                  foreground="black" ).place(x=520,y=400)
       tk1.Label( frame27, text = c,bg="white",font=("Arial",15),
                  foreground="black" ).place(x=730,y=400)

       
    options = ['ICU','HDU','Cardiac Care Unit(CCU)', 'Intensive Cardiac Care Unit(ICCU)', 'Trauma Unit(ITU)'
               ,'OPS', 'Pediatrics','Surgical', 'General Medicine']
    clicked = tk1.StringVar()
    clicked.set( "ICU")
    tk1.Label( frame27 , text = "SELECT DEPARTMENT",bg="white",font=("Arial",15),foreground=mybgcol ).place(x=375,y=220)
    drop = tk1.OptionMenu( frame27 , clicked , *options )
    drop.config(width=40,font=("Times",15))
    drop.place(x=370,y=260)
    tk1.Button( frame27, text = "ENTER" ,font=("Arial",15),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white" ,command = show ).place(x=550,y=310)
    tk1.Label(frame27,text='BED STATUS',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
    b3=tk1.Button(frame27,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe17)
    b3.place(x=555,y=590)

    #frame28 edit bed status
    def loadframe28():
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame27)
        frame28.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame28,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        tk1.Label(frame28,text='BED STATUS',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
        options = ['ICU','HDU','Cardiac Care Unit(CCU)', 'Intensive Cardiac Care Unit(ICCU)', 'Trauma Unit(ITU)'
               ,'OPS', 'Pediatrics','Surgical', 'General Medicine']
        clicked = tk1.StringVar()
        clicked.set( "ICU")
        tk1.Label( frame28 , text = "SELECT DEPARTMENT",bg="white",font=("Arial",15),foreground=mybgcol ).place(x=375,y=220)
        drop = tk1.OptionMenu( frame28 , clicked , *options )
        drop.config(width=40,font=("Times",15))
        drop.place(x=370,y=260)
        b3=tk1.Button(frame28,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe27)
        b3.place(x=555,y=590)
        tk1.Label(frame28,text='AVAILABLE BEDS',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
              font=("Calibri",15),foreground="white",width=25).place(x=305,y=310)
        E1=tk1.Entry(frame28,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E1.place(x=560,y=310)
        tk1.Label(frame28,text='TOTAL BEDS',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
              font=("Calibri",15),foreground="white",width=25).place(x=305,y=410)
        E2=tk1.Entry(frame28,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E2.place(x=560,y=410)
        
        def edit():
           department=clicked.get()
           availability=int(E1.get())
           total=int(E2.get())
           query="update beds set Totalbeds={},Availablebeds={} where Department='{}';".format(total,availability,department)
           cur.execute(query)  
           con.commit()
           E1.delete(0,tk1.END)
           E2.delete(0,tk1.END)
           tk1.Label(frame28,text='UPDATED',anchor='w',font=("Calibri",14),bg="white",foreground=mybgcol,width=20).place(x=205,y=550)
        tk1.Button( frame28, text = "SUBMIT" ,font=("Arial",15),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white" ,command = edit ).place(x=550,y=510)
        
    b4=tk1.Button(frame27,text="EDIT",font=("Arial",12),foreground="white",bg=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe28)
    b4.place(x=1000,y=50)

#frame29, the inventory page, frame30 edit inventory also defined under it
def loadframe29():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame17)
    clearwid(frame30)
    frame29.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage2)
    widge=tk1.Label(frame29,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    query1="select item from inventory order by item;"
    cur.execute(query1)
    k=cur.fetchall()
    items=[]
    for x in k:
        items.append(x[0])
    tk1.Label(frame29,text='INVENTORY',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
    clicked = tk1.StringVar()
    tk1.Label( frame29 , text = "SELECT ITEM",bg="white",font=("Arial",15),foreground=mybgcol ).place(x=375,y=220)
    drop = tk2.Combobox( frame29 , textvariable=clicked , values=items)
    drop.config(width=40,font=("Times",15))
    drop.place(x=370,y=260)
    tk1.Label(frame29,text='QUANTITY',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=360)
    tk1.Label(frame29,font=('Times',15),borderwidth=2,relief='solid',bg="white",fg="black",width=30).place(x=560,y=360)
    
    def show():
       item=clicked.get()
       query="select quantity from inventory where item='{}';".format(item)
       cur.execute(query)  
       q=cur.fetchone()[0]
       tk1.Label(frame29,text=q,font=('Times',15),borderwidth=2,relief='solid',bg="white",fg="black",width=30).place(x=560,y=360)
    tk1.Button( frame29, text = "ENTER" ,font=("Arial",15),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white" ,command = show ).place(x=550,y=310)
    b3=tk1.Button(frame29,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe17)
    b3.place(x=555,y=590)
    
    #frame30, edit inventory
    def loadframe30():
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame29)
        frame30.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame30,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        query1="select item from inventory order by item;"
        cur.execute(query1)
        k=cur.fetchall()
        items=[]
        for x in k:
            items.append(x[0])
        tk1.Label(frame30,text='INVENTORY',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
        b3=tk1.Button(frame30,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe29)
        b3.place(x=555,y=590)
        tk1.Label(frame30,text='ITEM NAME',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
              font=("Calibri",15),foreground="white",width=25).place(x=305,y=310)
        E1=tk1.Entry(frame30,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E1.place(x=560,y=310)
        tk1.Label(frame30,text='QUANTITY',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
              font=("Calibri",15),foreground="white",width=25).place(x=305,y=410)
        E2=tk1.Entry(frame30,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E2.place(x=560,y=410)
        
        def edit():
           itemname=E1.get()
           quantity=E2.get()
           if itemname in items:
               query="update inventory set quantity='{}' where item='{}';".format(quantity,itemname)
               cur.execute(query)  
               con.commit()
           else:
               query="insert into inventory values('{}','{}')".format(itemname,quantity)
               cur.execute(query)  
               con.commit()
           E1.delete(0,tk1.END)
           E2.delete(0,tk1.END)
           tk1.Label(frame30,text='UPDATED',anchor='w',font=("Calibri",14),bg="white",foreground=mybgcol,width=20).place(x=205,y=550)
           
        tk1.Button( frame30, text = "SUBMIT" ,font=("Arial",15),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white" ,command = edit ).place(x=550,y=510)
    b4=tk1.Button(frame29,text="EDIT",font=("Arial",12),foreground="white",bg=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe30)
    b4.place(x=1000,y=50)
    
#frame31,containing patient details also contains frame32(show patient reports),33(edit patient details),34(add new patient)( and 35(edit patient report)
def loadframe31():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame17)
    clearwid(frame34)
    clearwid(frame35)
    clearwid(frame32)
    clearwid(frame33)
    frame31.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage2)
    widge=tk1.Label(frame31,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    tk1.Label(frame31,text='PATIENT RECORDS',font=("Arial",30),bg="white",foreground=mybgcol).place(x=480,y=80)
    sf = ScrolledFrame(frame31,height=360,width=1050)
    sf.grid(row=7,column=4)
    sf.bind_arrow_keys(window1)
    sf.bind_scroll_wheel(window1)
    innerframe = sf.display_widget(tk1.Frame)
    query="select * from patient order by Doadmsn desc;"
    cur.execute(query)
    t=cur.fetchall()
    b3=tk1.Button(frame31,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe17).place(x=555,y=590)

    #frame35 edit patient report
    def loadframe35(x):
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame32)
        frame35.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame35,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        tk1.Label(frame35,text='EDIT REPORT',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
        tk1.Label(frame35,text='ENTER EDITED REPORT',anchor='w',font=("Calibri",30),bg="white",foreground=mybgcol,width=25).place(x=105,y=210)
        E1=tk1.Text(frame35,font=('Times',14),borderwidth=1,relief='solid',bg="white",fg="black",cursor="hand2",width=110,height=13)
        E1.place(x=110,y=260)
        def editrep():
            content=E1.get("1.0",tk1.END)
            query="update patient set remarks='{}' where remarks='{}'".format(content,x)
            cur.execute(query)
            con.commit()
            E1.delete("1.0",tk1.END)
            tk1.Label(frame35,text='REPORT UPDATED',anchor='w',font=("Calibri",14),bg="white",foreground=mybgcol,width=20).place(x=205,y=550)
        tk1.Button( frame35, text = "SUBMIT" ,font=("Arial",12),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white" ,command = editrep).place(x=550,y=550)
        tk1.Button(frame35,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe31).place(x=555,y=590)

    #frame32 which shows patient reports
    def loadframe32(x):
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame31)
        frame32.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame32,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        tk1.Label(frame32,text='REPORT',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
        b3=tk1.Button(frame32,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe31)
        b3.place(x=555,y=590)
        tk1.Label(frame32,text=x,borderwidth=5,relief='solid',anchor='nw',width=90,height=15, font=("Arial",15),
                  bg="white",foreground=mybgcol).place(x=120,y=200)
        b4=tk1.Button(frame32,text="EDIT",font=("Arial",12),foreground="white",bg=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=lambda: loadframe35(x))
        b4.place(x=1000,y=50)
        
        
        
    tk1.Label(innerframe,anchor='nw',text="P.ID",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=8).grid(row=1,column=0)
    tk1.Label(innerframe,anchor='nw',text="NAME",font=("Arial",14),borderwidth=5,relief='solid',bg=mybgcol,
              foreground="white",width=29).grid(row=1,column=3)
    tk1.Label(innerframe,anchor='nw',text="AGE",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=15).grid(row=1,column=5)
    tk1.Label(innerframe,anchor='nw',text="BLOOD GROUP",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=14).grid(row=1,column=7)
    tk1.Label(innerframe,anchor='nw',text="DOA",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=10).grid(row=1,column=9)
    tk1.Label(innerframe,anchor='nw',text="DOCTOR",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=13).grid(row=1,column=11)

    global count
    count=2
    for x in t:
        a,b,c,d,e,f,g=x[0],x[1],x[2],x[3],x[4],x[5],x[6]
        tk1.Label(innerframe,anchor='nw',text=a,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=8).grid(row=count,column=0)
        tk1.Button(innerframe,anchor='nw',text=b,font=("Arial",12),borderwidth=4,relief='solid',cursor="hand2",bg="white",activebackground=mybgcol,
                   foreground="black",activeforeground="white",command=lambda tempf=f:loadframe32(tempf),width=35).grid(row=count,column=3)
        tk1.Label(innerframe,anchor='nw',text=c,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=15).grid(row=count,column=5)
        tk1.Label(innerframe,anchor='nw',text=d,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=14).grid(row=count,column=7)
        tk1.Label(innerframe,anchor='nw',text=g,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=10).grid(row=count,column=9)
        tk1.Label(innerframe,anchor='nw',text=e,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=13).grid(row=count,column=11)
        count+=1
    #containing edit patient details
    def loadframe33():
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame31)
        frame33.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame33,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        options = ["NAME","AGE","BLOOD GROUP","DOCTOR","DOADMSN"]
        clicked = tk1.StringVar()
        clicked.set("NAME")
        tk1.Label( frame33 , text = "SELECT FIELD",bg="white",font=("Arial",15),foreground=mybgcol ).place(x=375,y=220)
        drop = tk1.OptionMenu( frame33 , clicked , *options )
        drop.config(width=40,font=("Times",15))
        drop.place(x=370,y=260)
        tk1.Label(frame33,text='PATIENT ID',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
              font=("Calibri",15),foreground="white",width=25).place(x=305,y=310)
        E1=tk1.Entry(frame33,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E1.place(x=560,y=310)
        tk1.Label(frame33,text='UPDATED FIELD',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
              font=("Calibri",15),foreground="white",width=25).place(x=305,y=410)
        E2=tk1.Entry(frame33,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E2.place(x=560,y=410)
        tk1.Label(frame33,text='EDIT PATIENT RECORDS',font=("Arial",30),bg="white",foreground=mybgcol).place(x=420,y=80)
        
        def edit():
           columnname=clicked.get()
           pid=E1.get()
           uval=E2.get()
           if columnname=='NAME':
               query="update patient set name='{}' where PatientID='{}';".format(uval,pid)
           elif columnname=='AGE':
               query="update patient set age='{}' where PatientID='{}';".format(uval,pid)
           elif columnname=="BLOOD GROUP":
               query="update patient set BloodGroup='{}' where PatientID='{}';".format(uval,pid)
           elif columnname=='DOCTOR':
                query="update patient set Doctor='{}' where PatientID='{}';".format(uval,pid)
           else:
               query="update patient set doadmsn='{}' where PatientID='{}';".format(uval,pid)
               
           cur.execute(query)  
           con.commit()
           E1.delete(0,tk1.END)
           E2.delete(0,tk1.END)
           tk1.Label(frame33,text='UPDATED',anchor='w',font=("Calibri",14),bg="white",foreground=mybgcol,width=20).place(x=205,y=550)
           
        tk1.Button( frame33, text = "SUBMIT" ,font=("Arial",15),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white" ,command = edit ).place(x=550,y=510)
        tk1.Button(frame33,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe31).place(x=555,y=590)
    #containing add new patient
    def loadframe34():
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame31)
        frame34.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame34,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        tk1.Label(frame34,text='ADD NEW PATIENT',anchor='w',bg="white",font=("Arial",30),foreground=mybgcol).place(x=420,y=80)
        E1=tk1.Entry(frame34,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E1.place(x=560,y=430)
        tk1.Label(frame34,text='NAME',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=310)
        tk1.Label(frame34,text='AGE',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=340)
        E2=tk1.Entry(frame34,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E2.place(x=560,y=310)
        tk1.Label(frame34,text='BLOOD GROUP',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=370)
        E3=tk1.Entry(frame34,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E3.place(x=560,y=340)
        tk1.Label(frame34,text='DOCTOR',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=400)
        E4=tk1.Entry(frame34,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E4.place(x=560,y=370)
        tk1.Label(frame34,text='DOA',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=430)
        E5=tk1.Entry(frame34,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E5.place(x=560,y=400)
        E1.insert(0,'yyyy-mm-dd')
        
        def submitpatient():
            doa=E1.get()
            name=E2.get()
            age=E3.get()
            bloodgroup=E4.get()
            doctor=E5.get()
            query="select PatientID from patient;"
            cur.execute(query)
            k=cur.fetchall()
            remarks=''
            pid=''
            for x in range(1,5000):
                tempid='P'+str(x)
                found=False
                for y in k:
                    if y[0]==tempid:
                        found=True
                if found==False:
                    pid=tempid
                    break
            query1="insert into patient values('{}','{}','{}','{}','{}','{}','{}');".format(pid,name,age,bloodgroup,doctor,remarks,doa)
            cur.execute(query1)
            con.commit()
            tk1.Label(frame34,text="PATIENT ADDED",width=40,bg="white",font=("Arial",12),foreground=mybgcol).place(x=460,y=550)

        tk1.Button( frame34, text = "SUBMIT" ,font=("Arial",15),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white" ,command = submitpatient ).place(x=550,y=510)
        tk1.Button(frame34,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe31).place(x=555,y=590)

        
        
        
    b4=tk1.Button(frame31,text="EDIT",font=("Arial",12),foreground="white",bg=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe33)
    b4.place(x=1000,y=50)
    b5=tk1.Button(frame31,text="ADD NEW",font=("Arial",12),foreground="white",bg=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe34)
    b5.place(x=1060,y=50)

#frame36 containing doc pages
def loadframe36():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame17)
    clearwid(frame37)
    clearwid(frame38)
    frame36.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage2)
    widge=tk1.Label(frame36,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    tk1.Label(frame36,text='DOCTOR RECORDS',font=("Arial",30),bg="white",foreground=mybgcol).place(x=480,y=80)
    sf = ScrolledFrame(frame36,height=360,width=1050)
    sf.grid(row=7,column=4)
    sf.bind_arrow_keys(window1)
    sf.bind_scroll_wheel(window1)
    innerframe = sf.display_widget(tk1.Frame)
    query="select * from doctors order by DOCID;"
    cur.execute(query)
    t=cur.fetchall()
    b3=tk1.Button(frame36,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe17).place(x=555,y=590)
    tk1.Label(innerframe,anchor='nw',text="D.ID",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=6).grid(row=1,column=0)
    tk1.Label(innerframe,anchor='nw',text="NAME",font=("Arial",14),borderwidth=5,relief='solid',bg=mybgcol,
              foreground="white",width=15).grid(row=1,column=3)
    tk1.Label(innerframe,anchor='nw',text="USERNAME",font=("Arial",14),borderwidth=5,relief='solid',bg=mybgcol,
              foreground="white",width=15).grid(row=1,column=5)
    tk1.Label(innerframe,anchor='nw',text="PHONE",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=14).grid(row=1,column=7)
    tk1.Label(innerframe,anchor='nw',text="EMAIL",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=25).grid(row=1,column=9)
    tk1.Label(innerframe,anchor='nw',text="ADDRESS",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=60).grid(row=1,column=11)
    tk1.Label(innerframe,anchor='nw',text="DOB",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=10).grid(row=1,column=13)
    tk1.Label(innerframe,anchor='nw',text="DOJ",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=10).grid(row=1,column=15)
    tk1.Label(innerframe,anchor='nw',text="DEPARTMENT",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=17).grid(row=1,column=17)
    tk1.Label(innerframe,anchor='nw',text="QUALIFICATION",font=("Arial",14),bg=mybgcol,borderwidth=5,relief='solid',
              foreground="white",width=35).grid(row=1,column=19)

    global count
    count=2
    for x in t:
        a,b,c,d,e,f,g,h,i,j=x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9]
        tk1.Label(innerframe,anchor='nw',text=a,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=6).grid(row=count,column=0)
        tk1.Label(innerframe,anchor='nw',text=b,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=15).grid(row=count,column=3)
        tk1.Label(innerframe,anchor='nw',text=c,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=15).grid(row=count,column=5)
        tk1.Label(innerframe,anchor='nw',text=d,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=14).grid(row=count,column=7)
        tk1.Label(innerframe,anchor='nw',text=e,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=25).grid(row=count,column=9)
        tk1.Label(innerframe,anchor='nw',text=f,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=60).grid(row=count,column=11)
        tk1.Label(innerframe,anchor='nw',text=g,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=10).grid(row=count,column=13)
        tk1.Label(innerframe,anchor='nw',text=h,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=10).grid(row=count,column=15)
        tk1.Label(innerframe,anchor='nw',text=i,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=17).grid(row=count,column=17)
        tk1.Label(innerframe,anchor='nw',text=j,font=("Arial",14),bg="white",borderwidth=5,relief='solid',foreground="black",width=35).grid(row=count,column=19)
        
        count+=1
        
    #frame37 containing edit doctor details
    def loadframe37():
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame36)
        frame37.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame37,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        options = ["NAME","PHONE","EMAIL ADDRESS","ADDRESS","DOB","DOJ","DEPARTMENT","QUALIFICATION"]
        clicked = tk1.StringVar()
        clicked.set("NAME")
        tk1.Label( frame37, text = "SELECT FIELD",bg="white",font=("Arial",15),foreground=mybgcol ).place(x=375,y=220)
        drop = tk1.OptionMenu( frame37, clicked , *options )
        drop.config(width=40,font=("Times",15))
        drop.place(x=370,y=260)
        tk1.Label(frame37,text='DOCTOR ID',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
              font=("Calibri",15),foreground="white",width=25).place(x=305,y=310)
        E1=tk1.Entry(frame37,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E1.place(x=560,y=310)
        tk1.Label(frame37,text='UPDATED FIELD',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
              font=("Calibri",15),foreground="white",width=25).place(x=305,y=410)
        E2=tk1.Entry(frame37,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E2.place(x=560,y=410)
        tk1.Label(frame37,text='EDIT DOCTOR RECORDS',font=("Arial",30),bg="white",foreground=mybgcol).place(x=420,y=80)
        
        def edit():
           columnname=clicked.get()
           did=E1.get()
           uval=E2.get()
           if columnname=='NAME':
               query="update doctors set name='{}' where DOCID='{}';".format(uval,did)
           elif columnname=='PHONE':
               query="update doctors set phone='{}' where DOCID='{}';".format(uval,did)
           elif columnname=="EMAIL ADDRESS":
               query="update doctors set email='{}' where DOCID='{}';".format(uval,did)
           elif columnname=='ADDRESS':
                query="update doctors set address='{}' where DOCID='{}';".format(uval,did)
           elif columnname=='DATE OF BIRTH':
                query="update doctors set DOB='{}' where DOCID='{}';".format(uval,did)
           elif columnname=='DATE OF JOINING':
                query="update doctors set DOJ='{}' where DOCID='{}';".format(uval,did)
           elif columnname=='DEPARTMENT':
                query="update doctors set DEPARTMENT='{}' where DOCID='{}';".format(uval,did)
           else:
               query="update doctors set QUALIFICATION='{}' where DOCID='{}';".format(uval,did)
               
           cur.execute(query)  
           con.commit()
           E1.delete(0,tk1.END)
           E2.delete(0,tk1.END)
           tk1.Label(frame37,text='UPDATED',anchor='w',font=("Calibri",14),bg="white",foreground=mybgcol,width=20).place(x=205,y=550)
           
        tk1.Button( frame37, text = "SUBMIT" ,font=("Arial",15),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white" ,command = edit ).place(x=550,y=510)
        tk1.Button(frame37,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe36).place(x=555,y=590)
        
    #frame38 containing add new doctor
    def loadframe38():
        if cur.rowcount>0:
            cur.fetchall()
        clearwid(frame36)
        frame38.tkraise()
        photo1=tk1.PhotoImage(file=mybgimage2)
        widge=tk1.Label(frame38,image=photo1)
        widge.image=photo1
        widge.grid(rowspan=10,columnspan=10)
        tk1.Label(frame38,text='ADD NEW DOCTOR',anchor='w',bg="white",font=("Arial",30),foreground=mybgcol).place(x=420,y=80)
        E1=tk1.Entry(frame38,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E1.place(x=560,y=220)
        tk1.Label(frame38,text='NAME',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=220)
        tk1.Label(frame38,text='PHONE',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=250)
        E2=tk1.Entry(frame38,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E2.place(x=560,y=250)
        tk1.Label(frame38,text='EMAIL',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=280)
        E3=tk1.Entry(frame38,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E3.place(x=560,y=280)
        tk1.Label(frame38,text='ADDRESS',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=310)
        E4=tk1.Entry(frame38,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E4.place(x=560,y=310)
        tk1.Label(frame38,text='DOB',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=340)
        E5=tk1.Entry(frame38,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E5.place(x=560,y=340)
        E5.insert(0,'yyyy-mm-dd')
        tk1.Label(frame38,text='DOJ',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=370)
        E6=tk1.Entry(frame38,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E6.place(x=560,y=370)
        E6.insert(0,'yyyy-mm-dd')
        tk1.Label(frame38,text='DEPARTMENT',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=400)
        E7=tk1.Entry(frame38,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E7.place(x=560,y=400)
        tk1.Label(frame38,text='QUALIFICATION',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                  font=("Calibri",15),foreground="white",width=25).place(x=305,y=430)
        E8=tk1.Entry(frame38,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
        E8.place(x=560,y=430)
        
        
        def submitdoctor():
            dob=E1.get()
            name=E2.get()
            phone=E3.get()
            email=E4.get()
            address=E5.get()
            doj=E6.get()
            department=E7.get()
            qualification=E8.get()
            query="select DOCID from doctors;"
            cur.execute(query)
            k=cur.fetchall()
            did=''
            for x in range(1,5000):
                tempid='D'+str(x)
                found=False
                for y in k:
                    if y[0]==tempid:
                        found=True
                if found==False:
                    did=tempid
                    break
            usertemp=name.split()
            username=did+usertemp[0]
            query1="insert into doctors values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(did,name,username,phone,email,address,dob,doj,department,qualification)
            cur.execute(query1)
            con.commit()
            query2="insert into logind values('{}','{}');".format(username,dob)
            cur.execute(query2)
            con.commit()
            tk1.Label(frame38,text="DOCTOR ADDED",width=40,bg="white",font=("Arial",12),foreground=mybgcol).place(x=460,y=550)

        tk1.Button( frame38, text = "SUBMIT" ,font=("Arial",15),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white" ,command = submitdoctor ).place(x=540,y=520)
        tk1.Button(frame38,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe36).place(x=555,y=590)

        
        
    b4=tk1.Button(frame36,text="EDIT",font=("Arial",12),foreground="white",bg=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe37)
    b4.place(x=1000,y=50)
    b5=tk1.Button(frame36,text="ADD NEW",font=("Arial",12),foreground="white",bg=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe38)
    b5.place(x=1060,y=50)

def loadframe41():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame17)
    clearwid(frame40)
    clearwid(frame42)
    frame41.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage2)
    widge=tk1.Label(frame41,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    tk1.Label(frame41,text='FINANCE',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
    global arphoto
    global genphoto
    arphoto=tk1.PhotoImage(file="assets/Arrow.gif").subsample(5,5)
    tk1.Button(frame41,image=arphoto,borderwidth=2,cursor="hand2",command=loadframe42).place(x=250,y=200)
    tk1.Label(frame41,text='UPDATE PAYMENT',font=("Arial",15),foreground="white",bg=mybgcol).place(x=280,y=470)
    genphoto=tk1.PhotoImage(file="assets/Generate.gif").subsample(5,5)
    tk1.Button(frame41,image=genphoto,borderwidth=2,cursor="hand2",command=loadframe40).place(x=750,y=200)
    tk1.Label(frame41,text='GENERATE AND PAY',font=("Arial",15),foreground="white",bg=mybgcol).place(x=780,y=470)
    b1=tk1.Button(frame41,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe17)
    b1.place(x=555,y=590)
    
def loadframe42():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame41)
    frame42.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage2)
    widge=tk1.Label(frame42,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    tk1.Label(frame42,text='FINANCE',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
    E1=tk1.Entry(frame42,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
    E1.place(x=560,y=170)
    tk1.Label(frame42,text='PATIENT ID',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
            font=("Calibri",15),foreground="white",width=25).place(x=305,y=170)
    tk1.Label( frame42 , text = "ENTER AMOUNT PAID",bg="white",font=("Arial",15),foreground=mybgcol ).place(x=305,y=210)
    E=tk1.Entry(frame42,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
    E.place(x=305,y=240)
    
    def paybill():
            pid=E1.get()
            paid=int(E.get())
            E.delete(0,tk1.END)
            E1.delete(0,tk1.END)
            query1="select AmountWithstanding from billing where pid='{}';".format(pid)
            cur.execute(query1)
            dat=cur.fetchall()
            amountwith=int(dat[0][0])
            amountw=amountwith-paid
            query2="update billing set AmountWithstanding={} where pid='{}';".format(amountw,pid)
            cur.execute(query2)
            con.commit()
            tk1.Label( frame42 , text = "AMOUNT WITHSTANDING",bg=mybgcol,
                       font=("Arial",15),foreground="white" ).place(x=305,y=300)
            tk1.Label( frame42 , text = amountw,bg="white",borderwidth=2,
                       font=("Arial",15),foreground="black" ).place(x=605,y=300)
            tk1.Label( frame42 , text = "TRANSACTION SUCCESSFUL, GO BACK",bg="white",
                       font=("Arial",15),foreground=mybgcol ).place(x=305,y=430)
            
    tk1.Button( frame42, text = "MAKE TRANSACTION" ,font=("Arial",12),foreground=mybgcol,cursor="hand2"
                ,activebackground=mybgcol,activeforeground="white",command=paybill).place(x=630,y=590)
    b1=tk1.Button(frame42,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe41)
    b1.place(x=555,y=590)
    
def loadframe40():
    if cur.rowcount>0:
        cur.fetchall()
    clearwid(frame41)
    frame40.tkraise()
    photo1=tk1.PhotoImage(file=mybgimage2)
    widge=tk1.Label(frame40,image=photo1)
    widge.image=photo1
    widge.grid(rowspan=10,columnspan=10)
    tk1.Label(frame40,text='FINANCE',bg="white",font=("Arial",40),foreground=mybgcol).place(x=460,y=50)
    E1=tk1.Entry(frame40,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
    E1.place(x=560,y=170)
    tk1.Label(frame40,text='PATIENT ID',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
            font=("Calibri",15),foreground="white",width=25).place(x=305,y=170)
    E2=tk1.Entry(frame40,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
    E2.place(x=560,y=200)
    tk1.Label(frame40,text='DATE OF RELEASE',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
            font=("Calibri",15),foreground="white",width=25).place(x=305,y=200)
    E2.insert(0,'yyyy-mm-dd')
    E3=tk1.Entry(frame40,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
    
    def show():
        department=clicked.get()
        pid=E1.get()
        dor=E2.get()
        query1="select doadmsn from patient where PatientID='{}';".format(pid)
        cur.execute(query1)
        k=cur.fetchall()
        doa=k[0][0]
        query2="select DATEDIFF('{}','{}');".format(dor,doa)
        cur.execute(query2)
        t=cur.fetchall()
        daysbed=int(t[0][0])

        def showbill(x):
            E1.delete(0,tk1.END)
            E2.delete(0,tk1.END)
            E3.delete(0,tk1.END)
            query1="select name from patient where PatientID='{}';".format(x)
            cur.execute(query1)
            ck=cur.fetchall()
            name=ck[0][0]
            query2="select department,totalnotax,totalfinal from billing where pid='{}';".format(x)
            cur.execute(query2)
            data=cur.fetchone()
            a,b,c=data[0],data[1],data[2]
            tk1.Label( frame40 , text = "BILL",relief='ridge',borderwidth=5,bg=mybgcol,anchor='w',font=("Arial",10),foreground="white",width=69
               ).place(x=80,y=370)
            tk1.Label( frame40 , text = 'PID',borderwidth=5,relief='ridge',bg="white",anchor='w',font=("Arial",15),foreground="black",width=20
               ).place(x=80,y=392)
            tk1.Label( frame40 , text = x,bg="white",font=("Arial",15),foreground="black",anchor='w',borderwidth=5,relief='ridge',width=30
                       ).place(x=300,y=392)
            tk1.Label( frame40 , text = 'NAME',bg="white",font=("Arial",15),foreground="black",anchor='w',borderwidth=5,relief='ridge',width=20
                       ).place(x=80,y=424)
            tk1.Label( frame40 , text = name,bg="white",font=("Arial",15),foreground="black",anchor='w' ,borderwidth=5,relief='ridge',width=30
                       ).place(x=300,y=424)
            tk1.Label( frame40 , text = 'DEPARTMENT',bg="white",font=("Arial",15),foreground="black",anchor='w',borderwidth=5,relief='ridge',width=20
                       ).place(x=80,y=456)
            tk1.Label( frame40 , text = a,bg="white",font=("Arial",15),foreground="black",anchor='w',borderwidth=5,relief='ridge',width=30
                       ).place(x=300,y=456)
            tk1.Label( frame40 , text = "TOTAL BEFORE TAX",bg="white",font=("Arial",15),foreground="black",anchor='w',borderwidth=5,relief='ridge',width=20
                       ).place(x=80,y=488)
            tk1.Label( frame40 , text = b,bg="white",font=("Arial",15),foreground="black",anchor='w',borderwidth=5,relief='ridge',width=30
                       ).place(x=300,y=488)
            tk1.Label( frame40 , text = "TOTAL FINAL",bg="white",font=("Arial",15),foreground="black",anchor='w',borderwidth=5,relief='ridge',width=20
                       ).place(x=80,y=520)
            tk1.Label( frame40 , text = c,bg="white",font=("Arial",15),foreground="black",anchor='w',borderwidth=5,relief='ridge',width=30
                       ).place(x=300,y=520)
            tk1.Label( frame40 , text = "ENTER AMOUNT PAID",bg="white",font=("Arial",15),foreground=mybgcol ).place(x=750,y=370)
            E=tk1.Entry(frame40,font=('Times',17),borderwidth=2,relief='solid',bg="white",fg="black",cursor="hand2",width=30)
            E.place(x=750,y=400)

            def paybill(y):
                paid=int(E.get())
                E.delete(0,tk1.END)
                query1="select AmountWithstanding from billing where pid='{}';".format(y)
                cur.execute(query1)
                dat=cur.fetchall()
                amountwith=int(dat[0][0])
                amountw=amountwith-paid
                query2="update billing set AmountWithstanding={} where pid='{}';".format(amountw,pid)
                cur.execute(query2)
                con.commit()
                tk1.Label( frame40 , text = "AMOUNT WITHSTANDING",bg=mybgcol,
                           font=("Arial",15),foreground="white" ).place(x=750,y=440)
                tk1.Label( frame40 , text = amountw,bg="white",borderwidth=2,
                           font=("Arial",15),foreground="black" ).place(x=1000,y=440)
                tk1.Label( frame40 , text = "TRANSACTION SUCCESSFUL, GO BACK",bg="white",
                           font=("Arial",8),foreground=mybgcol ).place(x=750,y=480)
                tk1.Label( frame40, bg="white",font=("Arial",15),foreground=mybgcol, width=20).place(x=630,y=590)
                
                
                
                
            tk1.Button( frame40, text = "MAKE TRANSACTION" ,font=("Arial",12),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=lambda tempx=x:paybill(tempx)).place(x=630,y=590)
        
        if department=='ICU':
           depfee=7000
           bedfee=8000
           bedtotal=5000*daysbed
           total1=bedtotal+depfee
           total2=total1+(25*total1/100)
           totalfinal=total2+(5*total2/100)
           query3="insert into billing values('{}','{}',{},{},{},'{}',{});".format(pid,department,daysbed,total2,totalfinal,dor,totalfinal)
           cur.execute(query3)
           con.commit()
           tk1.Button( frame40, text = "PROCEED" ,font=("Arial",12),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=lambda tempp=pid:showbill(tempp)).place(x=630,y=590)
           
        if department=='HDU':
           depfee=4000
           bedfee=5000
           bedtotal=bedfee*daysbed
           total1=bedtotal+depfee
           total2=total1+(25*total1/100)
           totalfinal=total2+(5*total2/100)
           query3="insert into billing values('{}','{}',{},{},{},'{}',{});".format(pid,department,daysbed,total2,totalfinal,dor,totalfinal)
           cur.execute(query3)
           con.commit()
           tk1.Button( frame40, text = "PROCEED" ,font=("Arial",12),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white" , command=lambda tempp=pid:showbill(tempp)).place(x=630,y=590)

        if department=='Cardiac Care Unit(CCU)':
           depfee=12000
           bedfee=6000
           bedtotal=bedfee*daysbed
           total1=bedtotal+depfee
           total2=total1+(25*total1/100)
           totalfinal=total2+(5*total2/100)
           query3="insert into billing values('{}','{}',{},{},{},'{}',{});".format(pid,department,daysbed,total2,totalfinal,dor,totalfinal)
           cur.execute(query3)
           con.commit()
           tk1.Button( frame40, text = "PROCEED" ,font=("Arial",12),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white" ,command=lambda tempp=pid:showbill(tempp)).place(x=630,y=590)


        if department=='Intensive Cardiac Care Unit(ICCU)':
           depfee=15000
           bedfee=6000
           bedtotal=bedfee*daysbed
           total1=bedtotal+depfee
           total2=total1+(25*total1/100)
           totalfinal=total2+(5*total2/100)
           query3="insert into billing values('{}','{}',{},{},{},'{}',{});".format(pid,department,daysbed,total2,totalfinal,dor,totalfinal)
           cur.execute(query3)
           con.commit()
           tk1.Button( frame40, text = "PROCEED" ,font=("Arial",12),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=lambda tempp=pid:showbill(tempp) ).place(x=630,y=590)


        if department=='Trauma Unit(ITU)':
           depfee=10000
           bedfee=5000
           bedtotal=bedfee*daysbed
           total1=bedtotal+depfee
           total2=total1+(25*total1/100)
           totalfinal=total2+(5*total2/100)
           query3="insert into billing values('{}','{}',{},{},{},'{}',{});".format(pid,department,daysbed,total2,totalfinal,dor,totalfinal)
           cur.execute(query3)
           con.commit()
           tk1.Button( frame40, text = "PROCEED" ,font=("Arial",12),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=lambda tempp=pid:showbill(tempp) ).place(x=630,y=590)


        if department=='Surgical':
           E3.place(x=560,y=330)
           tk1.Label(frame40,text='SURGERY COST',bg=mybgcol,anchor='w',borderwidth=2,relief='solid',
                font=("Calibri",15),foreground="white",width=25).place(x=305,y=330)
           def sur():
               surgerycost=int(E3.get())
               depfee=25000
               bedfee=10000
               bedtotal=bedfee*daysbed
               total1=bedtotal+depfee+surgerycost
               total2=total1+(25*total1/100)
               totalfinal=total2+(5*total2/100)
               query3="insert into billing values('{}','{}',{},{},{},'{}',{});".format(pid,department,daysbed,total2,totalfinal,dor,totalfinal)
               cur.execute(query3)
               con.commit()
               tk1.Button( frame40, text = "PROCEED" ,font=("Arial",12),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=lambda tempp=pid:showbill(tempp) ).place(x=630,y=590)
               
           tk1.Button( frame40, text = "ENTER" ,font=("Arial",9),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white" ,command = sur).place(x=950,y=330)

        if department=='Pediatrics':
           depfee=4000
           bedfee=4000
           bedtotal=bedfee*daysbed
           total1=bedtotal+depfee
           total2=total1+(25*total1/100)
           totalfinal=total2+(5*total2/100)
           query3="insert into billing values('{}','{}',{},{},{},'{}',{});".format(pid,department,daysbed,total2,totalfinal,dor,totalfinal)
           cur.execute(query3)
           con.commit()
           tk1.Button( frame40, text = "PROCEED" ,font=("Arial",12),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white" , command=lambda tempp=pid:showbill(tempp)).place(x=630,y=590)


        if department=='General Medicine':
           depfee=5000
           bedfee=4000
           bedtotal=bedfee*daysbed
           total1=bedtotal+depfee
           total2=total1+(25*total1/100)
           totalfinal=total2+(5*total2/100)
           query3="insert into billing values('{}','{}',{},{},{},'{}',{});".format(pid,department,daysbed,total2,totalfinal,dor,totalfinal)
           cur.execute(query3)
           con.commit()
           tk1.Button( frame40, text = "PROCEED" ,font=("Arial",12),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=lambda tempp=pid:showbill(tempp)).place(x=630,y=590)

           
        if department=='OutPatient Department(OPD)':
           depfee=5000
           bedfee=0
           bedtotal=bedfee*daysbed  
           total1=bedtotal+depfee
           total2=total1+(25*total1/100)
           totalfinal=total2+(5*total2/100)
           query3="insert into billing values('{}','{}',{},{},{},'{}',{});".format(pid,department,daysbed,total2,totalfinal,dor,totalfinal)
           cur.execute(query3)
           con.commit()
           tk1.Button( frame40, text = "PROCEED" ,font=("Arial",12),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white",command=lambda tempp=pid:showbill(tempp)).place(x=630,y=590)

    options = ['ICU','HDU','Cardiac Care Unit(CCU)', 'Intensive Cardiac Care Unit(ICCU)', 'Trauma Unit(ITU)'
               , 'Pediatrics','Surgical', 'General Medicine','OutPatient Department(OPD)']
    clicked = tk1.StringVar()
    clicked.set( "ICU")
    tk1.Label( frame40 , text = "SELECT DEPARTMENT",bg="white",font=("Arial",15),foreground=mybgcol ).place(x=305,y=250)
    drop = tk1.OptionMenu( frame40 , clicked , *options )
    drop.config(width=40,font=("Times",15))
    drop.place(x=305,y=290)
    tk1.Button( frame40, text = "ENTER" ,font=("Arial",12),foreground=mybgcol,cursor="hand2"
                  ,activebackground=mybgcol,activeforeground="white" ,command = show ).place(x=630,y=590)
    b3=tk1.Button(frame40,text="BACK",font=("Arial",12),foreground=mybgcol,cursor="hand2",
                  activebackground=mybgcol,activeforeground="white",command=loadframe41)
    b3.place(x=555,y=590)

def loadframe43():
    if cur.rowcount>0:
        cur.fetchall()
    global adminname
    frame43=tk1.Frame(frame17,bg="#D3D3D3",width=300,height=637)
    frame43.grid(row=0,column=9,columnspan=2)
    frame43.tkraise()
    tk1.Button(frame43,text="BACK",font=("Arial",12),bg=mybgcol,foreground="white",cursor="hand2",
                  activebackground="white",activeforeground=mybgcol,command=frame43.grid_forget).place(x=120,y=560)
    tk1.Label( frame43 , text = "PROFILE",bg="#D3D3D3",font=("Arial",30),foreground=mybgcol ).place(x=70,y=120)
    query1="select ID ,name,phone,email,username from admin where name='{}';".format(adminname)
    cur.execute(query1)
    k=cur.fetchall()
    data=k[0]
    a,b,c,d,e=data[0],data[1],data[2],data[3],data[4]
    tk1.Label( frame43 , text = "ID",bg=mybgcol,relief="ridge",borderwidth=2,font=("Arial",15),foreground="white",width=26).place(x=2,y=240)
    tk1.Label( frame43 , text = "NAME",bg=mybgcol,relief="ridge",borderwidth=2,font=("Arial",15),foreground="white",width=26).place(x=2,y=300)
    tk1.Label( frame43 , text = "PHONE",bg=mybgcol,relief="ridge",borderwidth=2,font=("Arial",15),foreground="white",width=26).place(x=2,y=360)
    tk1.Label( frame43 , text = "EMAIL",bg=mybgcol,relief="ridge",borderwidth=2,font=("Arial",15),foreground="white",width=26).place(x=2,y=420)
    tk1.Label( frame43 , text = "USERNAME",bg=mybgcol,relief="ridge",borderwidth=2,font=("Arial",15),foreground="white",width=26).place(x=2,y=480)
    tk1.Label( frame43 , text = a ,bg="white",relief="ridge",borderwidth=2,font=("Arial",15),
               foreground=mybgcol,width=26).place(x=2,y=270)
    tk1.Label( frame43 , text = b,bg="white",relief="ridge",borderwidth=2,font=("Arial",15),
               foreground=mybgcol,width=26).place(x=2,y=330)
    tk1.Label( frame43 , text = c,bg="white",relief="ridge",borderwidth=2,font=("Arial",15),
               foreground=mybgcol,width=26).place(x=2,y=390)
    tk1.Label( frame43 , text = d,bg="white",relief="ridge",borderwidth=2,font=("Arial",15),
               foreground=mybgcol,width=26).place(x=2,y=450)
    tk1.Label( frame43 , text = e,bg="white",relief="ridge",borderwidth=2,font=("Arial",15),
               foreground=mybgcol,width=26).place(x=2,y=510)
    
    
    
#calling frame 0 to initiate the program
loadframe0()


window1.mainloop()

 

