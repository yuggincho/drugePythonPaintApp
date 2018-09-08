#-------------------------------------------------------------------------------
# Name:        Druge Drawing Program
# Purpose: User-friendly drawing program for seniors. Object-oriented
#
# Author:      Eugene Cho
#
# Created:     16-06-2017
# Copyright:   (c) Eugene Cho 2017
#-------------------------------------------------------------------------------


from Tkinter import *
#from PIL import ImageGrab
import time
import tkMessageBox as tm


class drawingSpace(object):

    def __init__(self, master, username):

        """
        Constructor method for the drawing space

        Inputs: master - Tkinter Window, username - Str
        Outputs: None
        """

        self.username = username
        self.LkeyStatus = "unpressed"
        self.RkeyStatus = "unpressed"
        self.xCoor = None
        self.yCoor = None
        self.master = master
        self.brushwidth = 1
        self.eraserwidth = 5
        self.brushcolor = "black"
        self.backgroundcolor = "white"
        self.photonumber = 0
        master.title("Druge Drawing Program")


        self.drawingSurface = Canvas(master)
        self.drawingSurface.config(background = "white", width = 800, height = 600)
        self.drawingSurface.pack()
        self.drawingSurface.bind("<Motion>", self.editCanvas)
        self.drawingSurface.bind("<ButtonRelease-1>", self.LkeyUp)
        self.drawingSurface.bind("<ButtonPress-1>", self.LkeyDown)

        self.menubar = Menu(self.master)


        self.mainMenu = Menu(self.menubar, tearoff=0)


        self.brushThicknessMenu = Menu(self.mainMenu, tearoff=False)
        self.brushThicknessMenu .add_command(label="1", command = lambda: self.brushThickness(1))
        self.brushThicknessMenu .add_command(label="2", command = lambda: self.brushThickness(2))
        self.brushThicknessMenu .add_command(label="3", command = lambda: self.brushThickness(3))
        self.brushThicknessMenu .add_command(label="4", command = lambda: self.brushThickness(4))
        self.brushThicknessMenu .add_command(label="5", command = lambda: self.brushThickness(5))
        self.brushThicknessMenu .add_command(label="6", command = lambda: self.brushThickness(6))
        self.brushThicknessMenu .add_command(label="7", command = lambda: self.brushThickness(7))
        self.brushThicknessMenu .add_command(label="8", command = lambda: self.brushThickness(8))
        self.brushThicknessMenu .add_command(label="9", command = lambda: self.brushThickness(9))
        self.brushThicknessMenu .add_command(label="10", command = lambda: self.brushThickness(10))


        self.eraserThicknessMenu = Menu(self.mainMenu, tearoff=False)
        self.eraserThicknessMenu .add_command(label="1", command = lambda: self.eraserThickness(2))
        self.eraserThicknessMenu .add_command(label="2", command = lambda: self.eraserThickness(4))
        self.eraserThicknessMenu .add_command(label="3", command = lambda: self.eraserThickness(6))
        self.eraserThicknessMenu .add_command(label="4", command = lambda: self.eraserThickness(8))
        self.eraserThicknessMenu .add_command(label="5", command = lambda: self.eraserThickness(10))
        self.eraserThicknessMenu .add_command(label="6", command = lambda: self.eraserThickness(12))
        self.eraserThicknessMenu .add_command(label="7", command = lambda: self.eraserThickness(14))
        self.eraserThicknessMenu .add_command(label="8", command = lambda: self.eraserThickness(16))
        self.eraserThicknessMenu .add_command(label="9", command = lambda: self.eraserThickness(18))
        self.eraserThicknessMenu .add_command(label="10", command = lambda: self.eraserThickness(20))

        self.brushColorMenu = Menu(self.mainMenu, tearoff=False)
        self.brushColorMenu .add_command(label="White", command = lambda: self.brushColor("white"))
        self.brushColorMenu .add_command(label="Black", command = lambda: self.brushColor("black"))
        self.brushColorMenu .add_command(label="Red", command = lambda: self.brushColor("red"))
        self.brushColorMenu .add_command(label="Green", command = lambda: self.brushColor("green"))
        self.brushColorMenu .add_command(label="Blue", command = lambda: self.brushColor("blue"))
        self.brushColorMenu .add_command(label="Cyan", command = lambda: self.brushColor("cyan"))
        self.brushColorMenu .add_command(label="Yellow", command = lambda: self.brushColor("yellow"))
        self.brushColorMenu .add_command(label="Magenta", command = lambda: self.brushColor("magenta"))

        self.backgroundColorMenu = Menu(self.mainMenu, tearoff=False)
        self.backgroundColorMenu .add_command(label="White", command = lambda: self.backgroundColor("white"))
        self.backgroundColorMenu .add_command(label="Black", command = lambda: self.backgroundColor("black"))
        self.backgroundColorMenu .add_command(label="Red", command = lambda: self.backgroundColor("red"))
        self.backgroundColorMenu .add_command(label="Green", command = lambda: self.backgroundColor("green"))
        self.backgroundColorMenu .add_command(label="Blue", command = lambda: self.backgroundColor("blue"))
        self.backgroundColorMenu .add_command(label="Cyan", command = lambda: self.backgroundColor("cyan"))
        self.backgroundColorMenu .add_command(label="Yellow", command = lambda: self.backgroundColor("yellow"))
        self.backgroundColorMenu .add_command(label="Magenta", command = lambda: self.backgroundColor("magenta"))







        self.menubar.add_cascade(label="Tools & Options", menu = self.mainMenu)

        self.mainMenu.add_command(label="Instructions", command = self.instructions)
        self.mainMenu.add_cascade(label = "Brush Thickness", menu = self.brushThicknessMenu)
        self.mainMenu.add_cascade(label = "Eraser Thickness", menu = self.eraserThicknessMenu)
        self.mainMenu.add_cascade(label = "Brush Color", menu = self.brushColorMenu)
        self.mainMenu.add_cascade(label = "Background Color", menu = self.backgroundColorMenu)
        self.mainMenu.add_command(label="Clear Canvas", command = self.clear)

        self.mainMenu.add_command(label="Save", command = self.save)
        self.mainMenu.add_command(label="Log Out", command=self.logOut)
        self.mainMenu.add_command(label="Quit!", command=self.master.destroy)
        self.master.config(menu=self.menubar)

        self.drawingSurface.bind("<ButtonRelease-3>", self.RkeyUp)
        self.drawingSurface.bind("<ButtonPress-3>", self.RkeyDown)

    def clear(self):

        """
        Clears the drawing canvas

        Inputs: None
        Outputs: Background is reset on the screen.
        """
        self.drawingSurface.delete(ALL)

    def save(self):
        """
        Triggers the image-taking and saving process.

        Inputs: None
        Outputs: None
        """
        time.sleep(2)
        self.photoSnap(self.drawingSurface)



        """def photoSnap(self,widget):

        Takes a screenshot of the current drawing on the canvas

        Inputs: widget to take a picture of - object
        Outputs: Image file to program folder, Success confirmation notice window

        x=self.master.winfo_rootx()+widget.winfo_x()
        y=self.master.winfo_rooty()+widget.winfo_y()
        x1=x+widget.winfo_width()
        y1=y+widget.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save("{0}_{1}.png".format(self.username,self.photonumber))
        tm.showinfo("Photo Saved", "Picture has been saved as '{0}_{1}'. Please check the program folder.".format(self.username,self.photonumber))
        self.photonumber+=1"""



    def brushThickness(self, width):
        """
        Changes the brush thickness

        Inputs: width - int
        Outputs: None
        """
        self.brushwidth = width
    def eraserThickness(self, width):
        """
        Changes the eraser thickness

        Inputs: width - int
        Outputs: None
        """
        self.eraserwidth = width
    def brushColor(self,color):
        """
        Changes the brush color

        Inputs: color - str
        Outputs: None
        """
        self.brushcolor = color

    def backgroundColor(self,color):
        """
        Changes the background color

        Inputs: color - Str
        Outputs: Changes canvas background color
        """
        self.clear()
        self.backgroundcolor = color
        self.drawingSurface.config(background = self.backgroundcolor)

    def LkeyUp(self,event):
        """
        Records when the right mouse key is up

        Inputs: event (the status of the mouse keys)
        Outputs: None
        """
        self.LkeyStatus = "unpressed"
        self.xCoor = None
        self.yCoor = None

    def LkeyDown(self,event):
        """
        Records when the left mouse key is down

        Inputs: event (the status of the mouse keys)
        Outputs: None
        """
        self.LkeyStatus = "pressed"

    def RkeyUp(self,event):
        """
        Records when the right mouse key is up

        Inputs: event (the status of the mouse keys)
        Outputs: None
        """

        self.RkeyStatus = "unpressed"
        self.xCoor = None
        self.yCoor = None

    def RkeyDown(self,event):
        """
        Records when the right mouse key is down

        Inputs: event (the status of the mouse keys)
        Outputs: None
        """

        self.RkeyStatus = "pressed"

    def editCanvas(self, event):
        """
        Edits the canvas based on drawing and erasing inputs

        Inputs: event (the status of the left and right mouse keys)
        Outputs: Drawings and erased portions are outputted on to screen
        """

        if self.LkeyStatus == "pressed":
            if self.xCoor != None and self.yCoor != None:
                event.widget.create_line(self.xCoor,self.yCoor,event.x,event.y,smooth=TRUE, fill = self.brushcolor, width = self.brushwidth)

            self.xCoor = event.x
            self.yCoor = event.y

        elif self.RkeyStatus == "pressed":
            if self.xCoor != None and self.yCoor != None:
                event.widget.create_line(self.xCoor,self.yCoor,event.x,event.y,smooth=TRUE, fill = self.backgroundcolor, width = self.eraserwidth)

            self.xCoor = event.x
            self.yCoor = event.y

    def logOut(self):
        """
        Logs the user out of the program and returns to login screen

        Inputs: None other than self
        Outputs: Returns user to login screen.
        """
        self.master.destroy()

        global root
        root = Tk()
        lf = LoginScreen(root)
        root.mainloop()

    def instructions(self):
        """
        Displays an instruction window to the user

        Inputs: None other than self
        Outputs: A Tkinter Display Window
        """
        instructionWindow = Tk()
        instructionWindow.title("Instructions")
        label = Label(instructionWindow, text = "Left Click to Draw. Right Click to Erase. Have fun with a variety of options in the toolbar!")
        label.grid(row=0)




class LoginScreen(object):
    def __init__(self, master):

        """
        Constructs the login screen

        Inputs: A master Tkinter window to display logins screen on
        Outputs: None
        """

        self.master = master
        self.master.title("Druge")

        self.label_1 = Label(self.master, text="Username")
        self.label_2 = Label(self.master, text="Password")
        self.label_3 = Label(self.master, text = "(In users.txt)")

        self.entry_1 = Entry(self.master)
        self.entry_2 = Entry(self.master, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.label_3.grid(row=2, column = 0)


        self.loginButton = Button(self.master, text="Login", command = self.login)
        self.loginButton.grid(columnspan=2)



    def login(self):
        """
        Logs the user into the program and displays main program.

        Inputs: None other than self
        Outputs: Main Program is Entered
        """
        #print("Clicked")
        username = self.entry_1.get()
        password = self.entry_2.get()

        #print(username, password)

        userList = getTextFile("users.txt","r").readlines()
        userList = userList[1:]
        done = False
        counter = 0
        for line in userList:
            counter +=1
            line = line[:-1]
            subList = line.split(",")
            if subList[0] == username and subList[1] == password:

                tm.showinfo("Login Confirmation", "Welcome {0}".format(username))

                global root
                root.destroy()

                main = Tk()
                my_gui = drawingSpace(main, username)
                main.mainloop()
                done = True

        if done == False:
                tm.showerror("Login Error", "Incorrect Username or Password")


def getTextFile(generalFile, openType):
    """
    Opens up a file and returns it

    Inputs: File name, open type
    Outputs: File contents
    """
    fileObject = open(generalFile, openType)
    return fileObject


root = Tk()
loginLevel = LoginScreen(root)
root.mainloop()



