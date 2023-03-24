from tkinter import *
from tkinter import messagebox
class doctor:
    def func():
        roo=Tk()
        roo.title('يا')
        roo.geometry("925x500+300+200")
        roo.config(bg="#ECF9FF")
        roo.resizable(False,False)
        main_frame=Frame(roo,bd=2,bg="white")
        main_frame.place(x=0,y=0,width=925,height=925)

        label_doc=Label(main_frame,text="مرحبا اسامه شفيق",fg="#331c48",bg="#ECF9FF",font=('Microsoft YaHei UI Light ',30))
        label_doc.place(x=150,y=100)
        label_doc.pack()


        #frame for subjects
        fram_one=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="", font=("times new roman",12,"bold"))
        fram_one.place(x=20,y=90,width=250,height=270)
        fram_two=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="", font=("times new roman",12,"bold"))
        fram_two.place(x=300,y=90,width=250,height=270)
        fram_three=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="", font=("times new roman",12,"bold"))
        fram_three.place(x=600,y=90,width=250,height=270)

        #frames for subjects

        
        Label(roo,text="Data Structure",bg="white",fg='blue',font=('Microsoft YaHei UI Light ',15)).place(x=80,y=140)
        Label(roo,text="Data Base",bg="white",fg='blue',font=('Microsoft YaHei UI Light ',15)).place(x=390,y=140)
        Label(roo,text="Structure Programming",bg="white",fg='blue',font=('Microsoft YaHei UI Light ',15)).place(x=635,y=140)

        Label(roo,text="قسم حاسبات",bg="white",fg='blue',font=('Microsoft YaHei UI Light ',15)).place(x=110,y=190)
        Label(roo,text="شعبه علوم حاسب",bg="white",fg='blue',font=('Microsoft YaHei UI Light ',15)).place(x=90,y=240)

        #frame two
        Label(roo,text="قسم حاسبات",bg="white",fg='blue',font=('Microsoft YaHei UI Light ',15)).place(x=400,y=190)
        Label(roo,text="شعبه علوم حاسب",bg="white",fg='blue',font=('Microsoft YaHei UI Light ',15)).place(x=380,y=240)

        #frame three
        Label(roo,text="قسم حاسبات",bg="white",fg='blue',font=('Microsoft YaHei UI Light ',15)).place(x=700,y=190)
        Label(roo,text="شعبه علوم حاسب",bg="white",fg='blue',font=('Microsoft YaHei UI Light ',15)).place(x=680,y=240)

        Button(roo,width=10,pady=7,text="الدخول",bg="blue",fg='white',border=0).place(x=110,y=310)
        Button(roo,width=10,pady=7,text="الدخول",bg="blue",fg='white',border=0).place(x=405,y=310)
        Button(roo,width=10,pady=7,text="الدخول",bg="blue",fg='white',border=0).place(x=710,y=310)