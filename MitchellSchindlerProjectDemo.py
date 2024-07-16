"""

Author:  Mitchell Schindler
Date written: 07/15/24
Assignment:   Module 06 Programming Assignment Part I
Short Desc:   A GUI program that converts between fahrenheit and celsius.


"""
import tkinter as tk
from PIL import Image, ImageTk
bgColor = "#ADD8E6" #List of colors used by the application.
btnColor0 = "#76BDD5" #Buttons can't be colored on MacOS sadly.
btnColor1 = "#D8EDF3"

def load_mainFrame(): #Loaded when the project is started
    mainFrame.tkraise() #Puts the main frame in the front
    mainFrame.pack_propagate(False) #Makes it so that the frame can't interfere with window size
    
    #mainFrame Images
    tempImg = ImageTk.PhotoImage(file="Temperature.png") #Assigns the photo the object
    tempWidget = tk.Label(mainFrame,
                          image = tempImg,
                          bg = bgColor)
    tempWidget.image = tempImg #Assigns the object with the attachet photo to the widget
    tempWidget.grid() #Places the widget on the screen
    root.eval("tk::PlaceWindow . center") #Centers the window in the center of the screen

    #mainFrame Labels
    label1 = tk.Label(mainFrame,
                      text = "Enter a temperature:",
                      bg = bgColor,
                      fg = "white",
                      font = ("TkMenuFont", 14) ).grid() #Configures the label instructing the user to
                                                        #enter a temperature, and adds it to the screen

    #mainFrame Text Entry Box
    entry1 = tk.Text(mainFrame,
                     width = 10, height = 1).grid(row = 1, column = 1) #configures and adds the
                                                                        #temperature entry box to the
                                                                        #screen

    #mainFrame Buttons
    button1 = tk.Button(mainFrame,
                        text = "See Statistics",
                        font = ("TkMenuFont", 25),
                        bg = btnColor0,
                        fg = "white",
                        cursor = "hand2",
                        activebackground = btnColor1,
                        activeforeground = "black",
                        command = lambda:load_sideFrame() ).grid(pady = 20) #configures and adds the
                                                                            #button to view statistics
                                                                            #to the screen
    
    button2 = tk.Button(mainFrame,
                        text = "Convert to Fahrenheit",
                        font = ("TkMenuFont", 25),
                        bg = btnColor0,
                        fg = "white",
                        cursor = "hand2",
                        activebackground = btnColor1,
                        activeforeground = "black",
                        command = lambda:load_sideFrame() ).grid(pady = 20) #configures and adds the
                                                                            #button to convert to
                                                                            #fahrenheit to the screen
    
    button3 = tk.Button(mainFrame,
                        text = "Convert to Celsius",
                        font = ("TkMenuFont", 25),
                        bg = btnColor0,
                        fg = "white",
                        cursor = "hand2",
                        activebackground = btnColor1,
                        activeforeground = "black",
                        command = lambda:load_sideFrame() ).grid(pady = 20) #configures and adds the
                                                                            #button to convert to
                                                                            #celsius to the screen



def load_sideFrame():
    sideFrame.tkraise() #moves the seccond window to the front when called

#Configures the windows
root = tk.Tk()
root.title("Temperature Calculator") #names the window

mainFrame = tk.Frame(root,
                     width = 500, height = 600,
                     bg = bgColor) #configures the main frame of the project

sideFrame = tk.Frame(root,
                     bg = bgColor) #configures the secondary frame of the project

for frame in(mainFrame, sideFrame):
    frame.grid(row = 0, column = 0) #assigns both frames to (0, 0)

load_mainFrame()

#Starts the window
root.mainloop() #main project loop
