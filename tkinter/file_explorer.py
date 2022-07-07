# Python program to create
# a file explorer in Tkinter
  
# import all components
# from the tkinter library
from tkinter import *
  
# import filedialog module
from tkinter import filedialog
  
# Function for opening the
# file explorer window
def browseFiles():
    
    filetypes = (
        ('Image files', ('*.png', '*.jpg', '*.jpeg')),
        ('All files', '*.png*')
    )
    
    files = filedialog.askopenfilenames(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = filetypes )
      
    # Change label contents
    print(files)
    return files

def process_images():
    print('process_images')
    
                                                                                                  
# Create the root window
window = Tk()
  
# Set window title
window.title('Exotic India - Image Auto Recorter')
  
# Set window size
window.geometry("500x500")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "Image Auto Recorder",
                            width = 100, height = 4,
                            fg = "blue")
      
button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFiles)

button_process = Button(window,
                        text = "Process Images",
                        command = browseFiles,
                        )
  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns


label_file_explorer.grid(column = 1, row = 1)
  
button_explore.grid(column = 1, row = 2)

button_process.grid(column = 1, row = 3)
  
# Let the window wait for any events
window.mainloop()




# root = Tk()
# myapp = App(root)
# myapp.mainloop()