
# data={'username':'chujwdupee', 'email':'ko@ko.pl'}
# response = requests.delete("http://localhost:8000/api/users/6")
# response_get = requests.get("http://localhost:8000/api/users/").json()
# for r in response_get['results']:
# 	print(r)

import json
import requests

import tkinter as tk
from PIL import ImageTk, Image

from django.contrib.auth.hashers import check_password
from tkinter import font  as tkfont

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    token=None
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_page()


    def login_process(self):
        login=self.E1.get();
        password=self.E2.get();
        self.token=requests.post("http://localhost:8000/api-token-auth/", data={'username':login,'password':password}).json()

        if 'token' in self.token:
            # cls variable
            StartPage.token=self.token['token']
            print('logged in')
            self.controller.show_frame("PageOne")

        else:
            print('User doesnt exists')
            self.token=None;

    def create_page(self):
        self.L1 = tk.Label(self, text="User Name")
        self.L1.grid( row=1, column=0, padx=10, pady=10)
        self.E1 = tk.Entry(self, bd =5)
        self.E1.grid(row=1, column=1, padx=10, pady=10)

        self.L2 = tk.Label(self, text="Password")
        self.L2.grid( row=2, column=0, padx=10, pady=10)
        self.E2 = tk.Entry(self, bd =5)
        self.E2.grid(row=2, column=1, padx=10, pady=10)


        self.login = tk.Button(self, text="LOGIN", fg="red",command=self.login_process)
        self.login.grid(row=3, column=0, padx=10, pady=10)

        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.controller.destroy)
        self.quit.grid(row=3, column=1, padx=10, pady=10)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.grid(row=0, column=0, padx=10, pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda:self.response_get())
        button.grid(row=1, column=0, padx=10, pady=10)

    def response_get(self):
        column=0
        row=0
        bands=[]
        response_get = requests.get("http://localhost:8000/api/bands/", headers={'Authorization':'Token '+StartPage.token}).json()
        for b in response_get['results']:
            bands.append(b['band'])
            # self.img = ImageTk.PhotoImage(Image.open("cover1.jpg"))
            # self.panel = tk.Button(self, text='CHUJ') # image = self.img # )
            # self.panel.grid(row=2, column=0, padx=10, pady=10)
        self.bl=[0]*len(bands)
        for i in range(len(self.bl)):
            self.bl[i]=tk.Button(self, text=bands[i]) # image = self.img # )
            if column >2: 
                row+=1
                column=0
            self.bl[i].grid(row=row+2, column=column, padx=10, pady=10)
            column+=1
        # self.L1 = tk.Label(self, text="User Name")
        # self.L1.grid( row=1, column=0, padx=10, pady=10)
        # self.E1 = tk.Entry(self, bd =5)
        # self.E1.grid(row=1, column=1, padx=10, pady=10)

        # self.L2 = tk.Label(self, text="Password")
        # self.L2.grid( row=2, column=0, padx=10, pady=10)
        # self.E2 = tk.Entry(self, bd =5)
        # self.E2.grid(row=2, column=1, padx=10, pady=10)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


# class Application(tk.Frame):
# 	def __init__(self, master=None):
# 		super().__init__(master)
# 		self.grid()
# 		self.pack()
# 		self.create_widgets()

# 	def login_process(self):
# 		login=self.E1.get();
# 		password=self.E2.get();
# 		x=requests.post("http://localhost:8000/api-token-auth/", data={'username':login,'password':password}).json()

# 		if 'token' in x :
# 			response_get = requests.get("http://localhost:8000/api/users/", headers={'Authorization':'Token '+x['token']}).json()
# 			print('logged in')
# 		else:
# 			print('User doesnt exists')



# 	def create_widgets(self):
# 		self.hi_there = tk.Button(self)
# 		self.hi_there["text"] = "Hello World\n(click me)"
# 		self.hi_there["command"] = self.say_hi
# 		self.hi_there.grid(row=0, column=0, padx=10, pady=10)

# 		# self.img = ImageTk.PhotoImage(Image.open("C:/Users/Tomasz/djangopro/media/cover1.jpg"))
# 		# self.panel = tk.Label(self, image = self.img)
# 		# self.panel.pack(side = "left")

# 		# self.img2 = ImageTk.PhotoImage(Image.open("C:/Users/Tomasz/djangopro/media/cover1.jpg"))
# 		# self.panel2 = tk.Label(self, image = self.img)
# 		# self.panel2.pack(side = "left")

# 		# self.img3 = ImageTk.PhotoImage(Image.open("C:/Users/Tomasz/djangopro/media/cover1.jpg"))
# 		# self.panel3 = tk.Label(self, image = self.img)
# 		# self.panel3.pack(side = "left")


# 		self.L1 = tk.Label(self, text="User Name")
# 		self.L1.grid( row=1, column=0, padx=10, pady=10)
# 		self.E1 = tk.Entry(self, bd =5)
# 		self.E1.grid(row=1, column=1, padx=10, pady=10)

# 		self.L2 = tk.Label(self, text="Password")
# 		self.L2.grid( row=2, column=0, padx=10, pady=10)
# 		self.E2 = tk.Entry(self, bd =5)
# 		self.E2.grid(row=2, column=1, padx=10, pady=10)


# 		self.login = tk.Button(self, text="LOGIN", fg="red",command=self.login_process)
# 		self.login.grid(row=3, column=0, padx=10, pady=10)

# 		self.quit = tk.Button(self, text="QUIT", fg="red",command=root.destroy)
# 		self.quit.grid(row=3, column=1, padx=10, pady=10)

# 	def say_hi(self):
# 		print("hi there, everyone!")

# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()


