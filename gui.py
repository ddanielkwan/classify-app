from tkinter import Tk, Button, Frame, Label, Text, Entry, INSERT, END, PhotoImage, messagebox, LEFT, FLAT, GROOVE, BOTTOM, BOTH
from PIL import Image, ImageTk
# from main import get_input
class main(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.name = "Classifer Application"
        self.master = master
        self.master["bg"] = "black"
        self.master.title("Classifier Application")
        self.master.iconbitmap(r'images/magnify.ico')
        self.master.geometry("1000x700")
        self.add_label()
        # self.add_search_bar()
        self.add_buttons()

    def onClick(self):
        #For debugging
        print("Clicked")
    
    def add_search_bar(self):
        self.search_bar = Entry(self.master, bg = "#1F417B", width = 42, font=("Times New Roman", 22))
        self.search_bar.place(x=150,y=100)
        self.get_search_results = Button(self.master, text="Enter", command=self.retrieve_input, width=10, height = 2, bg="#1F417B")
        self.get_search_results.configure(fg='white',font=("Courier", 10))
        self.get_search_results.place(x=770,y=97.7) #FIX
    
    def retrieve_input(self):
        result = self.search_bar.get()
        # spamResult = get_input(result)
        # messagebox.showinfo("Result", "Not spam" if spamResult == 0 else "Spam")
        print(result)

    def add_label(self):
        """Function to add the app name onto the GUI"""
        self.bgPath = 'images/bg.PNG'
        self.bg = ImageTk.PhotoImage(Image.open(self.bgPath))
        icon_size = Label(self.master)
        icon_size.image = self.bg
        icon_size.configure(image=self.bg)
        icon_size.pack()
  
        self.authorName = Label(self.master, text="By Daniel Kwan", bg = "#1F417B")
        self.authorName.config(font=("Courier", 10))
        self.authorName.place(x=870,y=670)
     

    def add_buttons(self):
        """Function to add buttons for applications"""
        self.mailPhoto=PhotoImage(file="images/mail.png")
        emailButton=Button(self.master, height = 150, command=self.onClick, borderwidth=0)
        emailButton.config(image=self.mailPhoto, bg='#7990B7', font =("Courier", 20, "bold"))
        emailButton.configure(activebackground="#33B5E5")
        emailButton.place(x=40,y=500)

        self.twitterPhoto=PhotoImage(file="images/twitter.png")
        twitterButton=Button(self.master, height = 150, width=250, command=self.onClick, borderwidth=0)
        twitterButton.config(image=self.twitterPhoto, bg='#7990B7', font =("Courier", 20, "bold"))
        twitterButton.configure(activebackground="#33B5E5")
        twitterButton.place(x=370,y=500)

        self.fbPhoto=PhotoImage(file="images/facebook.png")
        fbButton=Button(self.master, height = 150, width=250, command=self.onClick, borderwidth=0)
        fbButton.config(image=self.fbPhoto, bg='#9adfe6', font =("Courier", 20, "bold"))
        fbButton.configure(activebackground='#9adfe6')
        fbButton.place(x=700,y=500)
        
root = Tk()
run = main(root)
root.mainloop()
