from tkinter import *
import cv2
import newadmin
import newmatrial
import edit
def AdminEdit():
    root=Tk()
    root.title("Attendance System")

    root.geometry("925x500+300+200")
    root.config(bg="#ECF9FF")
    root.resizable(False,False)

    #img_logo = PhotoImage(file="E:\logo.png")
    #root.iconphoto(False,img_logo)
    Label(root, bg="white",background="#ECF9FF").place(x=50,y=120)
    frame = Frame(root,width=350,height=370,bg="#ECF9FF")
    frame.place(x=480,y=100)

    heading = Label(frame,text="admin مرحبا محمد",fg="black",bg="#ECF9FF",font=('Microsoft YaHei UI Light ',25,'bold'))
    heading.place(x=100,y=-6)

    def createAccount_btn():
        newadmin.NewAccount()
    
    def edit_data_btn():
        edit.edit_data()

    
    def add_course_btn():
        newmatrial.add_course()



    # create three buttons for taking attendance, adding new students, and viewing sheets
    attendance_button = Button(frame,width=15,border=0 ,bg="#0081C9",fg='white',text="انشاء حساب جديد",command=createAccount_btn,  font=("Arial", 14))
    attendance_button.place(x=140,y=80)


    add_button = Button(frame, width=15,border=0,bg="#0081C9",fg='white',text="تغيير دكتور",command= edit_data_btn,  font=("Arial", 14))
    add_button.place(x=140,y=150)

    sheets_button = Button(frame,width=15,border=0 ,bg="#0081C9",fg='white',text="اضافة ماده جديده",command=add_course_btn,  font=("Arial", 14))
    sheets_button.place(x=140,y=220)

    # start the main event loop to handle user interactions
    #root.mainloop()
#AdminEdit()