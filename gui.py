from tkinter import Tk, Button, Frame, Label, Text, Entry, INSERT, END, PhotoImage, Image, messagebox
from main import get_input
class main(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.name = "Classifer Application"
        self.master = master
        self.master["bg"] = "#A4A4A4"
        self.pack()
        self.master.title("Classifier Application")
        self.master.iconbitmap(r'images/magnify.ico')
        self.master.geometry("1000x700")
        self.add_buttons()
        self.add_label()
        self.add_search_bar()

    def onClick(self):
        #for debugging
        print("Clicked")
    
    def add_search_bar(self):
        self.search_bar = Entry(self.master, bg = "#A4A4A4", width = 50, font=("Times New Roman", 18))
        self.search_bar.pack(ipady=10)
        get_search_results = Button(self.master, text="Get search", command=self.retrieve_input)
        get_search_results.pack() #FIX
    
    def retrieve_input(self):
        result = self.search_bar.get()
        spamResult = get_input(result)

        messagebox.showinfo("Result", "Not spam" if spamResult == 0 else "Spam")
        print(result)

    def add_label(self):
        """Function to add the app name onto the GUI"""
        appName = Label(self.master, text=self.name, bg = "#A4A4A4")
        appName.config(font=("Courier", 44))
        appName.pack()
        authorName = Label(self.master, text="By Daniel Kwan", bg = "#A4A4A4")
        authorName.config(font=("Courier", 10))
        authorName.place(x=870,y=670)

    def add_buttons(self):
        """Function to add buttons for applications"""
        emailButton = Button(self.master, text="Classify Email",
                            width=35, height = 10,command=self.onClick, bg="#A6CFE8")
        twitterButton = Button(self.master, text="Classify Tweet",
                            width=35, height = 10,command=self.onClick, bg="#A6CFE8")
        facebookButton = Button(self.master, text="Classify Post",
                            width=35, height = 10,command=self.onClick, bg="#A6CFE8")
        emailButton.place(x=50,y=300)
        twitterButton.place(x=370,y=300)
        facebookButton.place(x=685,y=300)
        
root = Tk()
run = main(root)
root.mainloop()
