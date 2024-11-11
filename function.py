from tkinter import  messagebox,Toplevel,Label,Entry,Button,Text,DISABLED,END,BOTH,WORD
from numpy.ma.core import empty
import  re
import  itertools


#check length
def buttonCheck(root,e):
    password_dictionary = ['User1234#','Qwerty!23','Letmein@123','Password@2024','SecureP@ss12',
        'Admin#2024','StrongPassword1!','Welcome@Home23','Super$ecret12','1234Secure!aA','MyP@ssword#2024',
        'TestPassword@12','F!rstPassw0rd','P@ssw0rd123!','OpenSes@me42','123Qwerty!@#','#AdmiN1234!',
        'SecretPassw0rd!','M3mber@2024','Strong1@Pass!']

    text=e.get()
    if not text:
        messagebox.showwarning('Warning','The field is empty')
        return
    else:
        pasL=len(text)
        if pasL < 8:
            messagebox.showwarning('Warning', 'The field is too short; a minimum of 8 characters is required.')
            return False
        if not re.search(r'[a-z]', text):  # Cel puțin o literă mică
            messagebox.showwarning('Warning', 'The password must contain at least one lowercase letter')
            return False
        if not re.search(r'[A-Z]', text):  # Cel puțin o literă mare
            messagebox.showwarning('Warning', 'The password must contain at least one uppercase letter')
            return False
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', text):
            messagebox.showwarning('Warning', 'The password must contain at least one special character')
            return False
        if not re.search(r'[0-9]', text):
            messagebox.showwarning('Warning', 'The password must contain at least one digit')
            return False
        if text in password_dictionary:
            messagebox.showwarning('Warning', 'The password is too common and may be easily guessed.')
            return False

        messagebox.showinfo('Success', 'Password is strong')
        return True



# data input
def dataInput(root):
    top=Toplevel()
    top.title('Data Input')
    top.geometry("600x300")
    labelFirstName=Label(top,text="First Name: ")
    labelFirstName.place(x=100, y=30)
    e1=Entry(top)
    e1.place(x=220, y=30)

    labelSecondName = Label(top, text="Second Name: ")
    labelSecondName.place(x=100, y=60)
    e2 = Entry(top)
    e2.place(x=220, y=60)

    labelDataB = Label(top, text="Birthday: ")
    labelDataB.place(x=100, y=90)
    e3 = Entry(top)
    e3.place(x=220, y=90)

    labelDataB = Label(top, text="Pet name: ")
    labelDataB.place(x=100, y=120)
    e4 = Entry(top)
    e4.place(x=220, y=120)

    labelDataB = Label(top, text="Mother name: ")
    labelDataB.place(x=100, y=150)
    e5 = Entry(top)
    e5.place(x=220, y=150)

    labelDataB = Label(top, text="Father name: ")
    labelDataB.place(x=100, y=180)
    e6 = Entry(top)
    e6.place(x=220, y=180)

    button = Button(top, text="OK", width=6,command= lambda: checkDataInput(top,e1,e2,e3,e4,e5,e6))
    button.place(x=190, y=230)

    top.mainloop()



def checkDataInput(top,e1,e2,e3,e4,e5,e6):
    entries=[e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()]
    empty_entries=[entry for entry in entries if not entry]
    if len(empty_entries) >0 :
        messagebox.showwarning('Warning', "You must complete all fields before clicking the 'OK' button.")
    else:
        e3_value = e3.get()
        if not re.match(r'^\d{2}\.\d{2}\.\d{4}$', e3_value):
            messagebox.showwarning('Invalid Input',  "The 'Birthday' field must be in the format xx.xx.xxxx (e.g., 10.10.2200).")
            return
    messagebox.showwarning('Task completed','Your list with easy passwords it was generated. To view it, you can access it from the report section')
    generateEassyPassword(entries)


def generateEassyPassword(entries):
    with open("raport.txt", 'w') as f:
        f.write("Raport - Parole Easy Generated\n")
        f.write("==================================\n\n")

        max_length = 3
        all_combinations = []

        for r in range(1, min(max_length, len(entries)) + 1):
            all_combinations.extend(itertools.combinations(entries, r))

        number_combinations = ['1234']

        generated_passwords = []

        for comb in all_combinations:
            base_password = ''.join(comb)
            for num in number_combinations:
                generated_passwords.append(base_password + num)

        for password in generated_passwords:
            f.write(password + "\n")

    print(f"{len(generated_passwords)} passwords have been generated and saved to 'raport.txt'.")


def toggle_password_visibility(entry, button):
    if entry.cget("show") == "":
        entry.config(show="*")
        button.config(text="Show")
    else:
        entry.config(show="")
        button.config(text="Hide")


def open_report(root):
    try:
        with open("raport.txt", "r") as file:
            content = file.read()

        report_window = Toplevel(root)
        report_window.title("Raport Parole")
        report_window.geometry("600x400")


        textShow = Text(report_window, wrap=WORD)
        textShow .pack(expand=True, fill=BOTH)

        textShow .insert(END, content)

        textShow .config(state=DISABLED)

        close_button = Button(report_window, text="Close", command=report_window.destroy)
        close_button.pack(pady=10)

    except FileNotFoundError:
        messagebox.showerror("Error", "File 'raport.txt' not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
