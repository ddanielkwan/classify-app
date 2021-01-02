from tkinter import Tk, Button, Frame, Label, Text, Entry, INSERT, END, PhotoImage, messagebox, LEFT, FLAT, GROOVE, BOTTOM, BOTH, Toplevel
from PIL import Image, ImageTk
from config import *
from functools import partial
    
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

    def onClick_email(self):
        #this is not done
        emailWindow = Toplevel(self.master)
        emailWindow.title("Settings") 
        emailWindow.geometry("300x300") 

        emailsearch_bar = Entry(emailWindow, font=("Times New Roman", 22))
        emailsearch_bar.pack()

        action = partial(self.retrieve_email_input, emailsearch_bar)

        get_search_results = Button(emailWindow, text="Enter", command=action, width=10, height = 2, bg="#1F417B")
        get_search_results.configure(fg='white',font=("Courier", 10))
        get_search_results.pack() 

        print("Clicked")
    
    def onClick_fb(self):
        print("clicked fb")

    def onClick_twitter(self):
        print("clicked twitter")
    
    def setting(self):
        """Creates setting window for application customize"""
        settingsWindow = Toplevel(self.master)
        settingsWindow.title("Settings") 
        settingsWindow.geometry("300x300") 
        settingChange = Entry(settingsWindow)
        settingChange.pack()
        action = partial(write_config, settingChange)
        settingButton = Button(settingsWindow, text="Change", command = action)
        settingButton.pack()

    def retrieve_email_input(self, search_bar):
        result = search_bar.get()
        print(result)

    def add_label(self):
        """Function to add the app name onto the GUI"""
        config = read_config()
        try:
            if "/" in config['DEFAULT']['bg']:
                self.bgPath = config['DEFAULT']['bg']
                self.bg = ImageTk.PhotoImage(Image.open(self.bgPath))
                icon_size = Label(self.master)
                icon_size.image = self.bg
                icon_size.configure(image=self.bg)
                icon_size.pack()
            elif "/" not in config['DEFAULT']['bg']:
                self.master['bg'] = config['DEFAULT']['bg']
                appName = Label(self.master, text=self.name, bg = config['DEFAULT']['bg'])
                appName.config(font=("Courier", 44))
                appName.pack()
        except:
            write_default()
        self.authorName = Label(self.master, text="By Daniel Kwan", bg = "#1F417B")
        self.authorName.config(font=("Courier", 10))
        self.authorName.place(x=870,y=670)
     
    def add_buttons(self):
        """Function to add buttons for applications"""
        #mail button
        self.mailPhoto=PhotoImage(file="images/mail.png")
        emailButton=Button(self.master, height = 150, command=self.onClick_email, borderwidth=0)
        emailButton.config(image=self.mailPhoto, bg='#7990B7', font =("Courier", 20, "bold"))
        emailButton.configure(activebackground="#33B5E5")
        emailButton.place(x=40,y=500)
        #twitter post button
        self.twitterPhoto=PhotoImage(file="images/twitter.png")
        twitterButton=Button(self.master, height = 150, width=250, command=self.onClick_twitter, borderwidth=0)
        twitterButton.config(image=self.twitterPhoto, bg='#7990B7', font =("Courier", 20, "bold"))
        twitterButton.configure(activebackground="#33B5E5")
        twitterButton.place(x=370,y=500)
        #facebook post button
        self.fbPhoto=PhotoImage(file="images/facebook.png")
        fbButton=Button(self.master, height = 150, width=250, command=self.onClick_fb, borderwidth=0)
        fbButton.config(image=self.fbPhoto, bg='#9adfe6', font =("Courier", 20, "bold"))
        fbButton.configure(activebackground='#9adfe6')
        fbButton.place(x=700,y=500)
        #settings button
        settingsButton = Button(self.master, height=1,width=4,command=self.setting)
        settingsButton.place(x=800,y=669)

root = Tk()
run = main(root)
root.mainloop()

