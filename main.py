from tkinter import *
from function import *

# create the menu
root=Tk()
root.title('PasswordChecker')
menu=Menu(root)
root.geometry("900x500")
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='Check',menu=filemenu)
filemenu.add_command(label='Data Input',command=lambda : dataInput(root))
filemenu.add_command(label='Report',command=lambda :open_report(root))
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)



labelCheck=Label(root,text="Check your password: ")
labelCheck.place(x=350,y=150)
e1=Entry(root)
e1.place(x=350,y=180)
button=Button(root,text="Test",width=10,command=lambda: buttonCheck(root,e1))
button.place(x=370,y=280)


buttonPass = Button(root, text="Show", command=lambda: toggle_password_visibility(e1, buttonPass))
buttonPass.place(x=500,y=180)


mainloop()