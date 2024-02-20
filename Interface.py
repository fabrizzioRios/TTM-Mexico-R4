import tkinter as tk
import tkinter.font as tkFont
from math import ceil
from PIL import Image, ImageTk


class App:
    def __init__(self, root):
        root.title("BigNuts")
        root.state('zoomed')
        root.configure(background="#bcddd4")
        self.screenwidth = root.winfo_screenwidth()
        self.screenheight = root.winfo_screenheight()
        self.buttonwidth = self.screenheight * 0.4
        self.buttonheight = self.screenheight * 0.2
        self.bannerwidth = self.screenwidth * 0.6
        bannerheight = self.screenheight * 0.4

        self.show_button = tk.Button(root)
        self.show_button["activebackground"] = "#009688"
        self.show_button["activeforeground"] = "#000000"
        self.show_button["bg"] = "#79b7ac"
        self.show_button["borderwidth"] = "1.5px"
        ft = tkFont.Font(family='Lucida Console', size=ceil(self.buttonheight * 0.1))
        self.show_button["font"] = ft
        self.show_button["fg"] = "#3e3e3e"
        self.show_button["justify"] = "center"
        self.show_button["text"] = "Revisar Dispositivos"
        self.show_button.place(x=(self.screenwidth / 3) * 1 - (self.buttonwidth / 2),
                               y=(self.screenheight / 2 + (self.buttonheight / 2)),
                               width=self.buttonwidth, height=self.buttonheight)
        self.show_button["command"] = self.show_button_command

        self.config_button = tk.Button(root)
        self.config_button["activebackground"] = "#009688"
        self.config_button["activeforeground"] = "#000000"
        self.config_button["bg"] = "#79b7ac"
        self.config_button["borderwidth"] = "1.5px"
        ft = tkFont.Font(family='Lucida Console', size=ceil(self.buttonheight * 0.1))
        self.config_button["font"] = ft
        self.config_button["fg"] = "#3e3e3e"
        self.config_button["justify"] = "center"
        self.config_button["text"] = "Configurar Dispositivos"
        self.config_button.place(x=(self.screenwidth / 3) * 2 - (self.buttonwidth / 2),
                                 y=(self.screenheight / 2 + (self.buttonheight / 2)),
                                 width=self.buttonwidth, height=self.buttonheight)
        self.config_button["command"] = self.config_button_command

        self.switch_button = tk.Button(root)
        self.switch_button["activebackground"] = "#009688"
        self.switch_button["activeforeground"] = "#000000"
        self.switch_button["bg"] = "#79b7ac"
        self.switch_button["borderwidth"] = "1.5px"
        ft = tkFont.Font(family='Lucida Console', size=ceil(self.buttonheight * 0.1))
        self.switch_button["font"] = ft
        self.switch_button["fg"] = "#3e3e3e"
        self.switch_button["justify"] = "center"
        self.switch_button["text"] = "Configurar Switches"
        self.switch_button["command"] = self.switch_button

        self.router_button = tk.Button(root)
        self.router_button["activebackground"] = "#009688"
        self.router_button["activeforeground"] = "#000000"
        self.router_button["bg"] = "#79b7ac"
        self.router_button["borderwidth"] = "1.5px"
        ft = tkFont.Font(family='Lucida Console', size=ceil(self.buttonheight * 0.1))
        self.router_button["font"] = ft
        self.router_button["fg"] = "#3e3e3e"
        self.router_button["justify"] = "center"
        self.router_button["text"] = "Configurar Routers"
        self.router_button["command"] = self.router_button_command

        self.original_image = Image.open('TTM_Logo.png')
        self.resized_image = self.original_image.resize((int(self.bannerwidth), int(bannerheight)))
        self.image = ImageTk.PhotoImage(self.resized_image)

        self.banner_image = tk.Canvas(root, width=self.bannerwidth, height=bannerheight)
        self.banner_image.create_image(0, 0, image=self.image, anchor=tk.NW)
        self.banner_image.place(x=self.screenwidth / 2 - (self.bannerwidth / 2), y=self.screenheight * 0.1)

    def show_button_command(self):
        self.banner_image.place_forget()
        self.show_button.place_forget()
        self.config_button.place_forget()

    def config_button_command(self):
        self.show_button.place_forget()
        self.config_button.place_forget()
        self.banner_image.place(x=self.screenwidth / 2 - (self.bannerwidth / 2), y=self.screenheight * 0.1)
        self.switch_button.place(x=(self.screenwidth / 3) * 1 - (self.buttonwidth / 2),
                                 y=(self.screenheight / 2 + (self.buttonheight / 2)),
                                 width=self.buttonwidth, height=self.buttonheight)
        self.router_button.place(x=(self.screenwidth / 3) * 2 - (self.buttonwidth / 2),
                                 y=(self.screenheight / 2 + (self.buttonheight / 2)),
                                 width=self.buttonwidth, height=self.buttonheight)

    def switch_button_command(self):
        self.switch_button.place_forget()
        self.router_button.place_forget()

    def router_button_command(self):
        self.switch_button.place_forget()
        self.router_button.place_forget()


root = tk.Tk()
app = App(root)
root.mainloop()
