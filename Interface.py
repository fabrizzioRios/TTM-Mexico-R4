import tkinter as tk
import tkinter.font as tkFont
from math import ceil
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        root.title("BigNuts")
        root.state('zoomed')
        root.configure(background = "#bcddd4")
        self.screenwidth = root.winfo_screenwidth()
        self.screenheight = root.winfo_screenheight()
        self.buttonwidth = self.screenheight * 0.4
        self.buttonheight = self.screenheight * 0.2
        self.bannerwidth = self.screenwidth * 0.6
        bannerheight = self.screenheight * 0.4

        self.Show_button = tk.Button(root)
        self.Show_button["activebackground"] = "#009688"
        self.Show_button["activeforeground"] = "#000000"
        self.Show_button["bg"] = "#79b7ac"
        self.Show_button["borderwidth"] = "1.5px"
        ft = tkFont.Font(family='Lucida Console', size=ceil(self.buttonheight * 0.1))
        self.Show_button["font"] = ft
        self.Show_button["fg"] = "#3e3e3e"
        self.Show_button["justify"] = "center"
        self.Show_button["text"] = "Revisar Dispositivos"
        self.Show_button.place(x=(self.screenwidth / 3) * 1 - (self.buttonwidth / 2), y=(self.screenheight / 2 + (self.buttonheight / 2)),
                          width=self.buttonwidth, height=self.buttonheight)
        self.Show_button["command"] = self.Show_button_command

        self.Config_button = tk.Button(root)
        self.Config_button["activebackground"] = "#009688"
        self.Config_button["activeforeground"] = "#000000"
        self.Config_button["bg"] = "#79b7ac"
        self.Config_button["borderwidth"] = "1.5px"
        ft = tkFont.Font(family='Lucida Console', size=ceil(self.buttonheight * 0.1))
        self.Config_button["font"] = ft
        self.Config_button["fg"] = "#3e3e3e"
        self.Config_button["justify"] = "center"
        self.Config_button["text"] = "Configurar Dispositivos"
        self.Config_button.place(x=(self.screenwidth / 3) * 2 - (self.buttonwidth / 2), y=(self.screenheight / 2 + (self.buttonheight / 2)),
                            width=self.buttonwidth, height=self.buttonheight)
        self.Config_button["command"] = self.Config_button_command

        self.Switch_button = tk.Button(root)
        self.Switch_button["activebackground"] = "#009688"
        self.Switch_button["activeforeground"] = "#000000"
        self.Switch_button["bg"] = "#79b7ac"
        self.Switch_button["borderwidth"] = "1.5px"
        ft = tkFont.Font(family='Lucida Console', size=ceil(self.buttonheight * 0.1))
        self.Switch_button["font"] = ft
        self.Switch_button["fg"] = "#3e3e3e"
        self.Switch_button["justify"] = "center"
        self.Switch_button["text"] = "Configurar Switches"
        self.Switch_button["command"] = self.Switch_button_command

        self.Router_button = tk.Button(root)
        self.Router_button["activebackground"] = "#009688"
        self.Router_button["activeforeground"] = "#000000"
        self.Router_button["bg"] = "#79b7ac"
        self.Router_button["borderwidth"] = "1.5px"
        ft = tkFont.Font(family='Lucida Console', size=ceil(self.buttonheight * 0.1))
        self.Router_button["font"] = ft
        self.Router_button["fg"] = "#3e3e3e"
        self.Router_button["justify"] = "center"
        self.Router_button["text"] = "Configurar Routers"
        self.Router_button["command"] = self.Router_button_command

        self.original_image = Image.open('TTM_Logo.png')
        self.resized_image = self.original_image.resize((int(self.bannerwidth), int(bannerheight)))
        self.image = ImageTk.PhotoImage(self.resized_image)

        self.Banner_image = tk.Canvas(root, width=self.bannerwidth, height=bannerheight)
        self.Banner_image.create_image(0, 0, image=self.image, anchor=tk.NW)
        self.Banner_image.place(x=self.screenwidth / 2 - (self.bannerwidth / 2), y=self.screenheight * 0.1)

    def Show_button_command(self):
        self.Banner_image.place_forget()
        self.Show_button.place_forget()
        self.Config_button.place_forget()

    def Config_button_command(self):
        self.Show_button.place_forget()
        self.Config_button.place_forget()
        self.Banner_image.place(x=self.screenwidth / 2 - (self.bannerwidth / 2), y=self.screenheight * 0.1)
        self.Switch_button.place(x=(self.screenwidth / 3) * 1 - (self.buttonwidth / 2), y=(self.screenheight / 2 + (self.buttonheight / 2)),
                          width=self.buttonwidth, height=self.buttonheight)
        self.Router_button.place(x=(self.screenwidth / 3) * 2 - (self.buttonwidth / 2), y=(self.screenheight / 2 + (self.buttonheight / 2)),
                          width=self.buttonwidth, height=self.buttonheight)
        
    def Switch_button_command(self):
        self.Switch_button.place_forget()
        self.Router_button.place_forget()

    def Router_button_command(self):
        self.Switch_button.place_forget()
        self.Router_button.place_forget()

root = tk.Tk()
app = App(root)
root.mainloop()