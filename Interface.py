import tkinter as tk
import tkinter.font as tkFont
import time
from netmiko_automation_tools import Device, Tools
from math import ceil
from PIL import Image, ImageTk

DEVICE_LIST = Tools.open_json_from_file(
    r"C:\Users\wilie\Documents\11vo Cuatrimestre\Redes 4\Scripts\TTM-Mexico-R4-1\test\data_test.json")
DEVICE_TYPE_FLAG = []
DEVICE_AREA_FLAG = []


class App:
    def __init__(self, root):
        # Create the interface
        root.title("Redes4 Interface")
        root.state('zoomed')
        root.configure(background="#232323")

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
        self.var_area4 = tk.BooleanVar()
        self.var_area5 = tk.BooleanVar()
        self.var_area6 = tk.BooleanVar()
        self.area_number = 3

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

        self.all_De_button = tk.Button(root)
        self.all_De_button["activebackground"] = "#009688"
        self.all_De_button["activeforeground"] = "#000000"
        self.all_De_button["bg"] = "#79b7ac"
        self.all_De_button["borderwidth"] = "1.5px"
        self.all_De_button["font"] = ft
        self.all_De_button["fg"] = "#3e3e3e"
        self.all_De_button["justify"] = "center"
        self.all_De_button["text"] = "Configurar Todo"
        self.all_De_button["command"] = lambda: self.device_button_command(["Switch", "Router"])

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

        self.add_area_buttonde_button = tk.Button(root)
        self.add_area_buttonde_button["activebackground"] = "#009688"
        self.add_area_buttonde_button["activeforeground"] = "#000000"
        self.add_area_buttonde_button["bg"] = "#79b7ac"
        self.add_area_buttonde_button["borderwidth"] = "1.5px"
        self.add_area_buttonde_button["font"] = ft
        self.add_area_buttonde_button["fg"] = "#3e3e3e"
        self.add_area_buttonde_button["justify"] = "center"
        self.add_area_buttonde_button["text"] = "Agregar Area"
        self.add_area_buttonde_button["command"] = self.add_area

        ft = tkFont.Font(family='Lucida Console', size=ceil(self.buttonheight * 0.06))
        self.back_button = tk.Button(root, activebackground="#009688", activeforeground="#000000", fg="#3e3e3e",
                                     text="Regresar", font=ft)
        ft = tkFont.Font(family='Lucida Console', size=ceil(self.buttonheight * 0.08))

        # Create Banner Image
        self.original_image = Image.open('TTM_Logo2.png')
        self.resized_image = self.original_image.resize((int(self.bannerwidth), int(bannerheight)))
        self.image = ImageTk.PhotoImage(self.resized_image)

        self.banner_image = tk.Canvas(root, width=self.bannerwidth, height=bannerheight)
        self.banner_image.create_image(0, 0, image=self.image, anchor=tk.NW)

        # Create Checkboxes
        self.checkbox_area1 = tk.Checkbutton(root, text="Oficina Zapopan", variable=self.var_area1)
        self.checkbox_area1["activebackground"] = "#009688"
        self.checkbox_area1["activeforeground"] = "#000000"
        self.checkbox_area1["bg"] = "#79b7ac"
        self.checkbox_area1["borderwidth"] = "1.5px"
        self.checkbox_area1["font"] = ft
        self.checkbox_area1["fg"] = "#3e3e3e"
        self.checkbox_area1["justify"] = "center"

        self.checkbox_area2 = tk.Checkbutton(root, text="Oficina CDMX", variable=self.var_area2)
        self.checkbox_area2["activebackground"] = "#009688"
        self.checkbox_area2["activeforeground"] = "#000000"
        self.checkbox_area2["bg"] = "#79b7ac"
        self.checkbox_area2["borderwidth"] = "1.5px"
        self.checkbox_area2["font"] = ft
        self.checkbox_area2["fg"] = "#3e3e3e"
        self.checkbox_area2["justify"] = "center"

        self.checkbox_area3 = tk.Checkbutton(root, text="Datacenter MTY", variable=self.var_area3)
        self.checkbox_area3["activebackground"] = "#009688"
        self.checkbox_area3["activeforeground"] = "#000000"
        self.checkbox_area3["bg"] = "#79b7ac"
        self.checkbox_area3["borderwidth"] = "1.5px"
        self.checkbox_area3["font"] = ft
        self.checkbox_area3["fg"] = "#3e3e3e"
        self.checkbox_area3["justify"] = "center"

        self.checkbox_area4 = tk.Checkbutton(root, text="Area 4", variable=self.var_area4)
        self.checkbox_area4["activebackground"] = "#009688"
        self.checkbox_area4["activeforeground"] = "#000000"
        self.checkbox_area4["bg"] = "#79b7ac"
        self.checkbox_area4["borderwidth"] = "1.5px"
        self.checkbox_area4["font"] = ft
        self.checkbox_area4["fg"] = "#3e3e3e"
        self.checkbox_area4["justify"] = "center"

        self.checkbox_area5 = tk.Checkbutton(root, text="Area 5", variable=self.var_area5)
        self.checkbox_area5["activebackground"] = "#009688"
        self.checkbox_area5["activeforeground"] = "#000000"
        self.checkbox_area5["bg"] = "#79b7ac"
        self.checkbox_area5["borderwidth"] = "1.5px"
        self.checkbox_area5["font"] = ft
        self.checkbox_area5["fg"] = "#3e3e3e"
        self.checkbox_area5["justify"] = "center"

        self.checkbox_area6 = tk.Checkbutton(root, text="Area 6", variable=self.var_area6)
        self.checkbox_area6["activebackground"] = "#009688"
        self.checkbox_area6["activeforeground"] = "#000000"
        self.checkbox_area6["bg"] = "#79b7ac"
        self.checkbox_area6["borderwidth"] = "1.5px"
        self.checkbox_area6["font"] = ft
        self.checkbox_area6["fg"] = "#3e3e3e"
        self.checkbox_area6["justify"] = "center"

        # Create Textbox
        self.message_box = tk.Text(root, wrap=tk.WORD, padx=30, pady=30, bg="#232323")
        ft = tkFont.Font(family='Lucida Console', size=ceil(self.buttonheight * 0.06))
        self.message_box["font"] = ft
        self.message_box.tag_configure("success", foreground="#77DD77")
        self.message_box.tag_configure("failure", foreground="#FF6961")
        self.message_box.tag_configure("end", foreground="#966FD6")
        self.message_box.tag_configure("left", justify='left')

        # Display first interface
        self.startMenu()

    # Button Functions
    def startMenu(self):
        self.clear_interface()

        # Place necessary components
        self.banner_image.place(x=self.screenwidth / 2 - (self.bannerwidth / 2), y=self.screenheight * 0.1)
        self.show_button.place(x=(self.screenwidth / 3) * 1 - (self.buttonwidth / 2),
                               y=(self.screenheight / 2 + (self.buttonheight / 2)),
                               width=self.buttonwidth, height=self.buttonheight)
        self.config_button.place(x=(self.screenwidth / 3) * 2 - (self.buttonwidth / 2),
                                 y=(self.screenheight / 2 + (self.buttonheight / 2)),
                                 width=self.buttonwidth, height=self.buttonheight)

    def show_button_command(self):
        self.clear_interface()
        siteList = ["Oficina_Zapopan", "Oficina_CDMX", "Datacenter_Monterrey"]

        # Place necessary components
        self.message_box.delete(1.0, tk.END)
        self.message_box.place(x=(self.screenwidth / 2) - (self.buttonwidth * 1.5),
                               y=(self.screenheight / 2) - (self.buttonheight * 2.1),
                               width=(self.buttonwidth * 3), height=(self.buttonheight * 4))
        self.back_button["command"] = self.startMenu

        root.update()
        time.sleep(0.1)

        # Execute pings and show results
        filtered_list_by_area = []
        for area in siteList:
            filtered_list_by_area.append(Tools.eliminate_element(DEVICE_LIST, "device_site", area))

        for area in range(3):
            self.message_box.insert(tk.END, f"\nDevices in site: {siteList[area]}\n\n", "end")
            root.update()
            time.sleep(0.1)
            for device in filtered_list_by_area[area]:
                connection_success = Tools.check_ping(device.get("device_data").get("host"))
                ping_result = f"The {device.get('device_role')} {device.get('device')} from site {device.get('device_site')} " \
                              f"{'is reachable' if connection_success else 'is not reachable'}\n\n\n"

                # Paint successful configurations green and unsuccessful configurations red
                if connection_success:
                    self.message_box.insert(tk.END, ping_result, "success")
                else:
                    self.message_box.insert(tk.END, ping_result, "failure")

                self.message_box.see(tk.END)
                root.update()
                time.sleep(0.1)

            self.message_box.see(tk.END)
            root.update()
            time.sleep(0.1)

        self.message_box.insert(tk.END, "Ping process complete.", "end")
        self.back_button.place(x=20, y=20, width=100, height=40)

    def config_button_command(self):
        self.clear_interface()
        self.area_number = 3

        # Place necessary components
        self.banner_image.place(x=self.screenwidth / 2 - (self.bannerwidth / 2), y=self.screenheight * 0.1)
        self.switch_button.place(x=(self.screenwidth / 4) * 1 - (self.buttonwidth / 3),
                                 y=(self.screenheight / 2 + (self.buttonheight / 2)),
                                 width=(self.buttonwidth / 1.5), height=(self.buttonheight / 1.5))
        self.router_button.place(x=(self.screenwidth / 4) * 2 - (self.buttonwidth / 3),
                                 y=(self.screenheight / 2 + (self.buttonheight / 2)),
                                 width=(self.buttonwidth / 1.5), height=(self.buttonheight / 1.5))
        self.all_De_button.place(x=(self.screenwidth / 4) * 3 - (self.buttonwidth / 3),
                                 y=(self.screenheight / 2 + (self.buttonheight / 2)),
                                 width=(self.buttonwidth / 1.5), height=(self.buttonheight / 1.5))
        self.back_button["command"] = self.startMenu
        self.back_button.place(x=20, y=20, width=100, height=40)

    def device_button_command(self, device_flag):
        global DEVICE_TYPE_FLAG, DEVICE_AREA_FLAG
        DEVICE_TYPE_FLAG = device_flag
        DEVICE_AREA_FLAG = []
        self.clear_interface()
        self.var_area1.set(False)
        self.var_area2.set(False)
        self.var_area3.set(False)
        self.var_area4.set(False)
        self.var_area5.set(False)
        self.var_area6.set(False)

        # Place necessary components
        self.banner_image.place(x=self.screenwidth / 2 - (self.bannerwidth / 2), y=self.screenheight * 0.1)
        self.checkbox_area1.place(x=(self.screenwidth / 4) * 1 - (self.buttonwidth / 3),
                                  y=(self.screenheight / 2 + (self.buttonheight / 5)),
                                  width=(self.buttonwidth / 1.5), height=(self.buttonheight / 2))
        self.checkbox_area2.place(x=(self.screenwidth / 4) * 2 - (self.buttonwidth / 3),
                                  y=(self.screenheight / 2 + (self.buttonheight / 5)),
                                  width=(self.buttonwidth / 1.5), height=(self.buttonheight / 2))
        self.checkbox_area3.place(x=(self.screenwidth / 4) * 3 - (self.buttonwidth / 3),
                                  y=(self.screenheight / 2 + (self.buttonheight / 5)),
                                  width=(self.buttonwidth / 1.5), height=(self.buttonheight / 2))

        self.add_area_buttonde_button.place(x=(self.screenwidth / 3) * 1 - (self.buttonwidth / 3),
                                   y=(self.screenheight / 6) * 5 - (self.buttonheight / 6),
                                   width=(self.buttonwidth / 2), height=(self.buttonheight / 2))
        self.submit_button.place(x=(self.screenwidth / 3) * 2 - (self.buttonwidth / 3),
                                 y=(self.screenheight / 6) * 5 - (self.buttonheight / 6),
                                 width=(self.buttonwidth / 2), height=(self.buttonheight / 2))
        self.back_button["command"] = self.config_button_command
        self.back_button.place(x=20, y=20, width=100, height=40)

    def submit(self):
        global DEVICE_AREA_FLAG, DEVICE_TYPE_FLAG
        self.clear_interface()

        # Place necessary components
        self.message_box.delete(1.0, tk.END)
        self.message_box.place(x=(self.screenwidth / 2) - (self.buttonwidth * 1.5),
                               y=(self.screenheight / 2) - (self.buttonheight * 2.1),
                               width=(self.buttonwidth * 3), height=(self.buttonheight * 4))
        self.back_button["command"] = lambda: self.device_button_command(DEVICE_TYPE_FLAG)
        root.update()
        time.sleep(0.1)

        # Add selected checkbox values to list
        if self.var_area1.get():
            DEVICE_AREA_FLAG.append("Oficina_Zapopan")
        if self.var_area2.get():
            DEVICE_AREA_FLAG.append("Oficina_CDMX")
        if self.var_area3.get():
            DEVICE_AREA_FLAG.append("Datacenter_Monterrey")
        if self.var_area4.get():
            DEVICE_AREA_FLAG.append("Site_4")
        if self.var_area5.get():
            DEVICE_AREA_FLAG.append("Site_5")
        if self.var_area6.get():
            DEVICE_AREA_FLAG.append("Site_6")

        # Filter devices by zone and role
        filtered_list_by_role = Tools.eliminate_element(DEVICE_LIST, "device_role", DEVICE_TYPE_FLAG)
        filtered_list_by_area = []
        for area in DEVICE_AREA_FLAG:
            filtered_list_by_area.append(Tools.eliminate_element(filtered_list_by_role, "device_site", area))

        print(filtered_list_by_area)

        # Send configuration file to all applicable routers
        comandos = ""
        with open('comands.txt', 'r') as file:
            for line in file:
                comandos += line.rstrip()
                comandos += "\n"

        for area in range(len(filtered_list_by_area)):
            self.message_box.insert(tk.END, f"\nDevices in site: {DEVICE_AREA_FLAG[area]}\n\n", "end")
            root.update()
            time.sleep(0.1)
            for device in filtered_list_by_area[area]:
                configuration_success = Device.config_device_with_txt(device.get("device_data"), r"comands.txt")
                config_result = f"Successfully sent the following configurations \n\n{comandos}\n" \
                                f"to the {device.get('device_role')} from site {device.get('device_site')} \n\n\n" if configuration_success else "Could not send configurations " \
                                                                                                                                                 f"to the {device.get('device_role')} from site {device.get('device_site')} \n\n\n"

                # Paint successful configurations green and unsuccessful configurations red
                if configuration_success:
                    self.message_box.insert(tk.END, config_result, "success")
                else:
                    self.message_box.insert(tk.END, config_result, "failure")

                self.message_box.see(tk.END)
                root.update()
                time.sleep(0.1)

        self.message_box.insert(tk.END, "Configuration process complete.", "end")
        self.back_button.place(x=20, y=20, width=100, height=40)

    def add_area(self):
        if self.area_number < 6:
            self.checkbox_area4.place_forget()
            self.checkbox_area5.place_forget()
            self.checkbox_area6.place_forget()

        if self.area_number == 3:
            self.checkbox_area4.place(x=(self.screenwidth / 2) - (self.buttonwidth / 3),
                                      y=(self.screenheight / 2 + (self.buttonheight / 1.2)),
                                      width=(self.buttonwidth / 1.5), height=(self.buttonheight / 2))
            self.area_number = 4

        elif self.area_number == 4:
            self.checkbox_area4.place(x=(self.screenwidth / 5) * 2 - (self.buttonwidth / 2),
                                      y=(self.screenheight / 2 + (self.buttonheight / 1.2)),
                                      width=(self.buttonwidth / 1.5), height=(self.buttonheight / 2))
            self.checkbox_area5.place(x=(self.screenwidth / 5) * 3 - (self.buttonwidth / 5.5),
                                      y=(self.screenheight / 2 + (self.buttonheight / 1.2)),
                                      width=(self.buttonwidth / 1.5), height=(self.buttonheight / 2))
            self.area_number = 5

        elif self.area_number == 5:
            self.checkbox_area4.place(x=(self.screenwidth / 4) * 1 - (self.buttonwidth / 3),
                                      y=(self.screenheight / 2 + (self.buttonheight / 1.2)),
                                      width=(self.buttonwidth / 1.5), height=(self.buttonheight / 2))
            self.checkbox_area5.place(x=(self.screenwidth / 4) * 2 - (self.buttonwidth / 3),
                                      y=(self.screenheight / 2 + (self.buttonheight / 1.2)),
                                      width=(self.buttonwidth / 1.5), height=(self.buttonheight / 2))
            self.checkbox_area6.place(x=(self.screenwidth / 4) * 3 - (self.buttonwidth / 3),
                                      y=(self.screenheight / 2 + (self.buttonheight / 1.2)),
                                      width=(self.buttonwidth / 1.5), height=(self.buttonheight / 2))
            self.area_number = 6

    def clear_interface(self):
        self.checkbox_area1.place_forget()
        self.checkbox_area2.place_forget()
        self.checkbox_area3.place_forget()
        self.checkbox_area4.place_forget()
        self.checkbox_area5.place_forget()
        self.checkbox_area6.place_forget()
        self.banner_image.place_forget()
        self.submit_button.place_forget()
        self.add_area_buttonde_button.place_forget()
        self.switch_button.place_forget()
        self.router_button.place_forget()
        self.all_De_button.place_forget()
        self.show_button.place_forget()
        self.config_button.place_forget()
        self.message_box.place_forget()
        self.back_button.place_forget()


root = tk.Tk()
app = App(root)
root.mainloop()
