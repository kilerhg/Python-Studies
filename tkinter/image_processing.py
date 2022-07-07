import os

import tkinter as tk
from tkinter import filedialog

class Application(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('200x300')
        self.title('Exotic India - Image Auto Recorter')
        #Set window background color
        self.config(background = "white")
        self.resizable(width=False, height=False) # lock the size
        icon=tk.PhotoImage(file='./favicon.png')
        self.iconphoto(True,icon)        
        
        self.slash = '/' # change if are in other OS
        self.files = ()
        self.selected = ''
        self.folder = ''
        self.output_folder_cover = ''
        self.output_folder_inside = ''
        
        first_label = tk.Label(self, text = "Image Auto Recorter",
                                    width = 100, height = 4,
                                    fg = "blue")
        first_label.pack(pady= 2, padx = 2)
        
            
        button_input = tk.Button(self,
                                text = "Browse Input Images",
                                command = self.browseFiles)
        
        button_output = tk.Button(self,
                                text = "Select Output Folder",
                                command = self.browseFolder)
        
        # browseFolder
        
        self.button_process = tk.Button(self,
                                text = "Process Images",
                                command = self.process_images,
                                state = tk.DISABLED
                                )
        self.var = tk.StringVar()
        
        self.first_label = tk.Label(self, text = "Select an option",
                                    width = 100, height = 4,
                                    fg = "blue")
        self.first_label.pack(pady= 2, padx = 2)
        
        R1 = tk.Radiobutton(self, text="Cover of the book", value='cover', command=self.selection, variable=self.var)
        R1.pack(pady= 2, padx = 2)
        
        R2 = tk.Radiobutton(self, text="Inside of the book", value='inside', command=self.selection, variable=self.var)
        R2.pack(pady= 2, padx = 2)
        
        # DISABLED
        
        
        
        button_input.pack(pady= 2, padx = 2)
        button_output.pack(pady= 2, padx = 2)
        self.button_process.pack(pady= 2, padx = 2)
    
    # Define a function to get the output for selected option
    def selection(self):
        self.selected = "You have selected " + str(self.var.get())
        self.first_label.config(text=self.selected)
        
        self.verify_process()
        
        # if self.selected and self.files:
        #     self.button_process["state"] = "normal"
        
    def browseFiles(self):
        
        filetypes = (
            ('Image files', ('*.png', '*.jpg', '*.jpeg')),
            ('All files', '*.png*')
        )
        
        self.files = filedialog.askopenfilenames(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = filetypes )
        # if self.selected and self.files:
        #     self.button_process["state"] = "normal"
        self.verify_process()
        print(self.files)
    
    
    def create_output_folder(self):
        
        output_folder = self.folder + f'{self.slash}image_processing{self.slash}'
        self.output_folder_cover = f'{output_folder}cover{self.slash}'
        self.output_folder_inside = f'{output_folder}inside{self.slash}'
        
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        if not os.path.exists(self.output_folder_cover):
            os.makedirs(self.output_folder_cover)
        if not os.path.exists(self.output_folder_inside):
            os.makedirs(self.output_folder_inside)
        
    def browseFolder(self):

        
        self.folder = filedialog.askdirectory()
        if not os.path.isdir(self.folder):
            self.folder = ''
            print('Invalid Path')
        print(self.folder)
        
        self.verify_process()

    def process_images(self):
        self.create_output_folder()
        print('process_images')
        print(self.files)
    
    def verify_process(self):
        print(f'selected: {bool(self.selected)}')
        print(f'files: {bool(self.files)}')
        print(f'folder: {bool(self.folder)}')
        if self.selected and self.files and self.folder:
            self.button_process["state"] = "normal"
    
app = Application()
app.mainloop()