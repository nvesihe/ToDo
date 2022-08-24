import tkinter as wapp
from tkinter import *
from tkinter import messagebox



class Dolist(wapp.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('500x450+500+200')
        self.title('ToDo List')
        self.config(bg='#FFFFFF')
        self.resizable(width=False,height=False)


        def newTask():
            task = user_entry.get()
            if task != "":
                lb.insert(END, task)
                user_entry.delete(0, "end")
            else:
                    messagebox.showwarning("Warning!", "Please enter some task.")

        def deleteTask():
            lb.delete(ANCHOR)
        
      
        def terminate():
            self.destroy()
            

        frame = Frame(self)
        frame.pack(pady=10)

        lb = Listbox(frame,width=25,height=8,font=('Times',18),bd=0,fg='#000000',
        highlightthickness=0,selectbackground='#3ae01b',activestyle="none")

        lb.pack(side=LEFT,fill=BOTH)

        sb = Scrollbar(frame)
        sb.pack(side=RIGHT,fill=BOTH)

        lb.config(yscrollcommand=sb.set)
        sb.config(command=lb.yview)

        user_entry = Entry(self,font=('times',24))
        user_entry.pack(pady=20)

        button_frame = Frame(self)
        button_frame.pack(pady=20)

        addTask = Button(
        button_frame,
        text='Add Task',
        font=('times 14'),
        bg='#3ae01b',
        padx=20,
        pady=10,
        command=newTask
        )
        addTask.pack(fill=BOTH, expand=True, side=LEFT)

        delTask = Button(
        button_frame,
        text='Delete Task',
        font=('times 14'),
        bg='#3ae01b',
        padx=20,
        pady=10,
        command=deleteTask
)
        delTask.pack(fill=BOTH, expand=True, side=LEFT)

        menubar = Menu(self)
        self.config(menu=menubar)

        option_menu = Menu(menubar)
        option_menu.add_command(label="Exit",command=terminate)

        menubar.add_cascade(
            label="Menu",
            menu= option_menu
        )

        

       
        
        



if __name__=="__main__":
    app = Dolist()
    app.mainloop()
