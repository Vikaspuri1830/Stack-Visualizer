from tkinter import *
import time

base = Tk()
base.title("Stack")
base.geometry("500x600")
base.maxsize(width=500, height=600)
base.configure(background="Indigo")

fnt = ("Arial Bold", 29)
btn_font = ("Arial", 20)
btn_color = "Lightgreen"

arr = []

def push_stack():
    # Logic 1
    all_num = textarea.get(1.0, END)
    length = len(all_num)

    if length<=17:
        label.configure(text="")
        num = entry.get()
        entry.delete(0,END)
        textarea.insert(1.0, num)
        arr.append(num)
        print(arr)

        all_num = textarea.get(1.0, END)
        length = len(all_num)
        print(length)

    else:
        label.configure(text="Stack Overflow")

    # Logic 2
    # num = entry.get()
    # entry.delete(0,END)
    # textarea.insert(1.0, num + "\n")
    # arr.append(num)
    # print(arr)


def pop_stack():
    # Logic 1
    print("Pop Executed")
    all_num = textarea.get(1.0, END)
    print(all_num)
    all_num = all_num[2:]
    print(all_num)
    textarea.delete(1.0, END)
    textarea.insert(1.0, all_num)

    if len(arr) != 0:
        entry.delete(0, END)
        entry.insert(0, arr[-1])
        arr.pop()

    if len(arr) == 0:
        label.configure(text="Stack Underflow")

    print(len(arr))

    # Logic 2
    # all_num = textarea.get(1.0, END)
    # length = len(all_num)
    # print(length)
    # all_num = all_num[2:]
    # textarea.delete(1.0, END)
    # textarea.insert(1.0, all_num)

label = Label(base, fg="white", bg="Indigo", font=btn_font, text="")
label.place(relx=0.47, rely=0.2)

textarea = Text(base, font=fnt)
textarea.place(relx=0.2, rely=0.1, relheight=0.7, relwidth=0.1)

entry = Entry(base, font=("Arial", 20))
entry.place(relx=0.575, rely=0.34, relheight=0.08, relwidth=0.15)

push = Button(base, font=btn_font, text="Push", bg=btn_color, command=push_stack)
push.place(relx=0.43, rely=0.5)

pop = Button(base, font=btn_font, text="Pop", bg=btn_color, command=pop_stack)
pop.place(relx=0.73, rely=0.5)

base.mainloop()