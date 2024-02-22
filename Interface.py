import tkinter as tk
import tkinter.font as tkFont
import time
from netmiko_automation_tools import Device, Tools
from math import ceil
from PIL import Image, ImageTk

DEVICE_LIST = Tools.open_json_from_file(r"C:\Users\wilie\Documents\11vo Cuatrimestre\Redes 4\Scripts\TTM-Mexico-R4\test\data_test.json")
DEVICE_TYPE_FLAG = []
DEVICE_AREA_FLAG = []

class App:
    def __init__(self, root):
        #Create the interface
        root.title("Redes4 Interface")
        root.state('zoomed')
        root.configure(background = "#bcddd4")
        
        #Create important variables
        self.screenwidth = root.winfo_screenwidth()
        self.screenheight = root.winfo_screenheight()
        self.buttonwidth = self.screenheight * 0.4
        self.buttonheight = self.screenheight * 0.2
        self.bannerwidth = self.screenwidth * 0.6
        bannerheight = self.screenheight * 0.4
        self.var_area1 = tk.BooleanVar()
        self.var_area2 = tk.BooleanVar()
        self.var_area3 = tk.BooleanVar()

        #Create buttons
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
        ft = tkFont.Font(family='Lucida Console', size=ceil(self.buttonheight * 0.08))
        self.Switch_button["font"] = ft
        self.Switch_button["fg"] = "#3e3e3e"
        self.Switch_button["justify"] = "center"
        self.Switch_button["text"] = "Configurar Switches"
        self.Switch_button["command"] = lambda: self.Device_button_command(["Switch"])

        self.Router_button = tk.Button(root)
        self.Router_button["activebackground"] = "#009688"
        self.Router_button["activeforeground"] = "#000000"
        self.Router_button["bg"] = "#79b7ac"
        self.Router_button["borderwidth"] = "1.5px"
        self.Router_button["font"] = ft
        self.Router_button["fg"] = "#3e3e3e"
        self.Router_button["justify"] = "center"
        self.Router_button["text"] = "Configurar Routers"
        self.Router_button["command"] = lambda: self.Device_button_command(["Router"])

        self.All_De_button = tk.Button(root)
        self.All_De_button["activebackground"] = "#009688"
        self.All_De_button["activeforeground"] = "#000000"
        self.All_De_button["bg"] = "#79b7ac"
        self.All_De_button["borderwidth"] = "1.5px"
        self.All_De_button["font"] = ft
        self.All_De_button["fg"] = "#3e3e3e"
        self.All_De_button["justify"] = "center"
        self.All_De_button["text"] = "Configurar Todo"
        self.All_De_button["command"] = lambda: self.Device_button_command(["Switch", "Router"])

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

        #Create Banner Image
        self.original_image = Image.open('TTM_Logo.png')
        self.resized_image = self.original_image.resize((int(self.bannerwidth), int(bannerheight)))
        self.image = ImageTk.PhotoImage(self.resized_image)

        self.Banner_image = tk.Canvas(root, width=self.bannerwidth, height=bannerheight)
        self.Banner_image.create_image(0, 0, image=self.image, anchor=tk.NW)
        self.Banner_image.place(x=self.screenwidth / 2 - (self.bannerwidth / 2), y=self.screenheight * 0.1)

        #Create Checkboxes
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

        #Create Textbox
        self.message_Box=tk.Message(root)
        self.message_Box["font"] = ft
        self.message_Box["fg"] = "black"
        self.message_Box["justify"] = "center"

    #Button Functions
    def Show_button_command(self):
        self.Banner_image.place_forget()
        self.Show_button.place_forget()
        self.Config_button.place_forget()
        self.message_Box.place(x=(self.screenwidth / 2) - (self.buttonwidth * 2), y=(self.screenheight / 2 + (self.buttonheight * 3)),
                          width=(self.buttonwidth * 2), height=(self.buttonheight * 3))

        ping_device_list = []
        
        for device in DEVICE_LIST:
            connection_success = Tools.check_ping(device.get("device_data").get("host"))
            ping_device_list.append("Hostname: " + device.get("device") + " connection successful" if connection_success else " connection unsuccessful")
        print(ping_device_list)

    def Config_button_command(self):
        self.Show_button.place_forget()
        self.Config_button.place_forget()
        self.Banner_image.place(x=self.screenwidth / 2 - (self.bannerwidth / 2), y=self.screenheight * 0.1)
        
        self.Switch_button.place(x=(self.screenwidth / 4) * 1 - (self.buttonwidth / 3), y=(self.screenheight / 2 + (self.buttonheight / 2)),
                          width=(self.buttonwidth/1.5), height=(self.buttonheight/1.5))
        
        self.Router_button.place(x=(self.screenwidth / 4) * 2 - (self.buttonwidth / 3), y=(self.screenheight / 2 + (self.buttonheight / 2)),
                          width=(self.buttonwidth/1.5), height=(self.buttonheight/1.5))
        
        self.All_De_button.place(x=(self.screenwidth / 4) * 3 - (self.buttonwidth / 3), y=(self.screenheight / 2 + (self.buttonheight / 2)),
                          width=(self.buttonwidth/1.5), height=(self.buttonheight/1.5))
        
    def Device_button_command(self, device_flag):
        global DEVICE_TYPE_FLAG
        DEVICE_TYPE_FLAG = device_flag

        self.Switch_button.place_forget()
        self.Router_button.place_forget()
        self.All_De_button.place_forget()

        self.checkbox_area1.place(x=(self.screenwidth / 4) * 1 - (self.buttonwidth / 3), y=(self.screenheight / 2 + (self.buttonheight / 3)),
                          width=(self.buttonwidth/1.5), height=(self.buttonheight/1.5))
        self.checkbox_area2.place(x=(self.screenwidth / 4) * 2 - (self.buttonwidth / 3), y=(self.screenheight / 2 + (self.buttonheight / 3)),
                          width=(self.buttonwidth/1.5), height=(self.buttonheight/1.5))
        self.checkbox_area3.place(x=(self.screenwidth / 4) * 3 - (self.buttonwidth / 3), y=(self.screenheight / 2 + (self.buttonheight / 3)),
                          width=(self.buttonwidth/1.5), height=(self.buttonheight/1.5))
        self.submit_button.place(x=(self.screenwidth / 2) - (self.buttonwidth / 4), y=(self.screenheight / 6) * 5 - (self.buttonheight /3),
                          width=(self.buttonwidth/2), height=(self.buttonheight/2))

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