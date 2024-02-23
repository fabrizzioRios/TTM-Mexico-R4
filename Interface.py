import tkinter as tk
import tkinter.font as tkFont
import time
from netmiko_automation_tools import Device, Tools
from math import ceil
from PIL import Image, ImageTk

DEVICE_LIST = Tools.open_json_from_file(r"./test/data_test.json")
DEVICE_TYPE_FLAG = []
DEVICE_AREA_FLAG = []


class App:
    def __init__(self, root):
        # Create the interface
        root.title("Redes4 Interface")
        root.state('zoomed')
        root.configure(background="#bcddd4")

        # Create important variables
        self.screenwidth = root.winfo_screenwidth()
        self.screenheight = root.winfo_screenheight()
        self.buttonwidth = self.screenheight * 0.4
        self.buttonheight = self.screenheight * 0.2
        self.bannerwidth = self.screenwidth * 0.6
        bannerheight = self.screenheight * 0.4
        self.var_area1 = tk.BooleanVar()
        self.var_area2 = tk.BooleanVar()
        self.var_area3 = tk.BooleanVar()

        # Create buttons
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
        ft = tkFont.Font(family='Lucida Console', size=ceil(self.buttonheight * 0.08))
        self.switch_button["font"] = ft
        self.switch_button["fg"] = "#3e3e3e"
        self.switch_button["justify"] = "center"
        self.switch_button["text"] = "Configurar Switches"
        self.switch_button["command"] = lambda: self.device_button_command(["Switch"])

        self.router_button = tk.Button(root)
        self.router_button["activebackground"] = "#009688"
        self.router_button["activeforeground"] = "#000000"
        self.router_button["bg"] = "#79b7ac"
        self.router_button["borderwidth"] = "1.5px"
        self.router_button["font"] = ft
        self.router_button["fg"] = "#3e3e3e"
        self.router_button["justify"] = "center"
        self.router_button["text"] = "Configurar Routers"
        self.router_button["command"] = lambda: self.device_button_command(["Router"])

        self.all_de_button = tk.Button(root)
        self.all_de_button["activebackground"] = "#009688"
        self.all_de_button["activeforeground"] = "#000000"
        self.all_de_button["bg"] = "#79b7ac"
        self.all_de_button["borderwidth"] = "1.5px"
        self.all_de_button["font"] = ft
        self.all_de_button["fg"] = "#3e3e3e"
        self.all_de_button["justify"] = "center"
        self.all_de_button["text"] = "Configurar Todo"
        self.all_de_button["command"] = lambda: self.device_button_command(["Switch", "Router"])

        self.submit_button = tk.Button(root)
        self.submit_button["activebackground"] = "#009688"
        self.submit_button["activeforeground"] = "#000000"
        self.submit_button["bg"] = "#79b7ac"
        self.submit_button["borderwidth"] = "1.5px"
        self.submit_button["font"] = ft
        self.submit_button["fg"] = "#3e3e3e"
        self.submit_button["justify"] = "center"
        self.submit_button["text"] = "Confirmar"
        self.submit_button["command"] = self.submit

        # Create Banner Image
        self.original_image = Image.open('TTM_Logo.png')
        self.resized_image = self.original_image.resize((int(self.bannerwidth), int(bannerheight)))
        self.image = ImageTk.PhotoImage(self.resized_image)

        self.banner_image = tk.Canvas(root, width=self.bannerwidth, height=bannerheight)
        self.banner_image.create_image(0, 0, image=self.image, anchor=tk.NW)
        self.banner_image.place(x=self.screenwidth / 2 - (self.bannerwidth / 2), y=self.screenheight * 0.1)

        # Create Checkboxes
        self.checkbox_area1 = tk.Checkbutton(root, text="Area 1", variable=self.var_area1)
        self.checkbox_area1["activebackground"] = "#009688"
        self.checkbox_area1["activeforeground"] = "#000000"
        self.checkbox_area1["bg"] = "#79b7ac"
        self.checkbox_area1["borderwidth"] = "1.5px"
        self.checkbox_area1["font"] = ft
        self.checkbox_area1["fg"] = "#3e3e3e"
        self.checkbox_area1["justify"] = "center"

        self.checkbox_area2 = tk.Checkbutton(root, text="Area 2", variable=self.var_area2)
        self.checkbox_area2["activebackground"] = "#009688"
        self.checkbox_area2["activeforeground"] = "#000000"
        self.checkbox_area2["bg"] = "#79b7ac"
        self.checkbox_area2["borderwidth"] = "1.5px"
        self.checkbox_area2["font"] = ft
        self.checkbox_area2["fg"] = "#3e3e3e"
        self.checkbox_area2["justify"] = "center"

        self.checkbox_area3 = tk.Checkbutton(root, text="Area 3", variable=self.var_area3)
        self.checkbox_area3["activebackground"] = "#009688"
        self.checkbox_area3["activeforeground"] = "#000000"
        self.checkbox_area3["bg"] = "#79b7ac"
        self.checkbox_area3["borderwidth"] = "1.5px"
        self.checkbox_area3["font"] = ft
        self.checkbox_area3["fg"] = "#3e3e3e"
        self.checkbox_area3["justify"] = "center"

        # Create Textbox
        self.message_Box = tk.Message(root)
        self.message_Box["font"] = ft
        self.message_Box["fg"] = "black"
        self.message_Box["justify"] = "center"

    # Button Functions
    def show_button_command(self):
        self.banner_image.place_forget()
        self.show_button.place_forget()
        self.config_button.place_forget()
        self.message_Box.place(x=(self.screenwidth / 2) - (self.buttonwidth * 2),
                               y=(self.screenheight / 2 + (self.buttonheight * 3)),
                               width=(self.buttonwidth * 2), height=(self.buttonheight * 3))

        ping_device_list = []

        for device in DEVICE_LIST:
            connection_success = Tools.check_ping(device.get("device_data").get("host"))
            ping_device_list.append("Hostname: " + device.get(
                "device") + " connection successful" if connection_success else " connection unsuccessful")
        print(ping_device_list)

    def config_button_command(self):
        self.show_button.place_forget()
        self.config_button.place_forget()
        self.banner_image.place(x=self.screenwidth / 2 - (self.bannerwidth / 2), y=self.screenheight * 0.1)

        self.switch_button.place(x=(self.screenwidth / 4) * 1 - (self.buttonwidth / 3),
                                 y=(self.screenheight / 2 + (self.buttonheight / 2)),
                                 width=(self.buttonwidth / 1.5), height=(self.buttonheight / 1.5))

        self.router_button.place(x=(self.screenwidth / 4) * 2 - (self.buttonwidth / 3),
                                 y=(self.screenheight / 2 + (self.buttonheight / 2)),
                                 width=(self.buttonwidth / 1.5), height=(self.buttonheight / 1.5))

        self.all_de_button.place(x=(self.screenwidth / 4) * 3 - (self.buttonwidth / 3),
                                 y=(self.screenheight / 2 + (self.buttonheight / 2)),
                                 width=(self.buttonwidth / 1.5), height=(self.buttonheight / 1.5))

    def device_button_command(self, device_flag):
        global DEVICE_TYPE_FLAG
        DEVICE_TYPE_FLAG = device_flag

        self.switch_button.place_forget()
        self.router_button.place_forget()
        self.all_de_button.place_forget()

        self.checkbox_area1.place(x=(self.screenwidth / 4) * 1 - (self.buttonwidth / 3),
                                  y=(self.screenheight / 2 + (self.buttonheight / 3)),
                                  width=(self.buttonwidth / 1.5), height=(self.buttonheight / 1.5))
        self.checkbox_area2.place(x=(self.screenwidth / 4) * 2 - (self.buttonwidth / 3),
                                  y=(self.screenheight / 2 + (self.buttonheight / 3)),
                                  width=(self.buttonwidth / 1.5), height=(self.buttonheight / 1.5))
        self.checkbox_area3.place(x=(self.screenwidth / 4) * 3 - (self.buttonwidth / 3),
                                  y=(self.screenheight / 2 + (self.buttonheight / 3)),
                                  width=(self.buttonwidth / 1.5), height=(self.buttonheight / 1.5))
        self.submit_button.place(x=(self.screenwidth / 2) - (self.buttonwidth / 4),
                                 y=(self.screenheight / 6) * 5 - (self.buttonheight / 3),
                                 width=(self.buttonwidth / 2), height=(self.buttonheight / 2))

    def submit(self):
        global DEVICE_AREA_FLAG, DEVICE_TYPE_FLAG

        if self.var_area1.get():
            DEVICE_AREA_FLAG.append("Site_1")
        if self.var_area2.get():
            DEVICE_AREA_FLAG.append("Site_2")
        if self.var_area3.get():
            DEVICE_AREA_FLAG.append("Site_3")

        print(DEVICE_AREA_FLAG, DEVICE_TYPE_FLAG)

        filtered_list_by_zone = Tools.eliminate_element(DEVICE_LIST, "device_site", DEVICE_AREA_FLAG)
        filtered_list_by_role = Tools.eliminate_element(filtered_list_by_zone, "device_role", DEVICE_TYPE_FLAG)

        for device in filtered_list_by_role:
            print(Device.config_device_with_txt(device.get("device_data"), r"comands.txt"))


root = tk.Tk()
app = App(root)
root.mainloop()