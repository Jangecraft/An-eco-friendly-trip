import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import math

class Menu:
    def __init__(self, window):
        self.window = window
        # Font
        self.ft = tkFont.Font(family='Angsana New', size=20)
        self.ftSm = tkFont.Font(family='Angsana New', size=12)

        self.label1 = tk.Label(self.window, text="Distance")
        self.label1.place(x=10, y=30)
        self.distanceEntry = tk.Entry(window)
        self.distanceEntry["borderwidth"] = "1px"
        self.distanceEntry["font"] = self.ft
        self.distanceEntry["fg"] = "#333333"
        self.distanceEntry["justify"] = "center"
        self.distanceEntry["text"] = "distance"
        self.distanceEntry.place(x=10, y=50, width=300, height=35)
        
        self.label2 = tk.Label(self.window, text="UNIT OF LENGTH")
        self.label2.place(x=320, y=30)
        self.unit_of_length_box = ttk.Combobox(window)
        self.unit_of_length_box["font"] = self.ft
        self.unit_of_length_box["values"] = ["centimeter", "meter", "kilometer"]
        self.unit_of_length_box.current(0)
        self.unit_of_length_box.bind('<Key>', 'break') # หยุดการเปลี่ยน values ใน unit_of_length
        self.unit_of_length_box.option_add("*TCombobox*Listbox*Font", self.ftSm)
        self.unit_of_length_box.place(x=320, y=50, width=130, height=35)

        self.label3 = tk.Label(self.window, text="number of passengers")
        self.label3.place(x=460, y=30)
        self.passenger_box = ttk.Combobox(window)
        self.passenger_box["font"] = self.ft
        self.passenger_box["values"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.passenger_box.current(0)
        self.passenger_box.option_add("*TCombobox*Listbox*Font", self.ftSm)
        self.passenger_box.place(x=460, y=50, width=130, height=35)

        self.calculate_button = tk.Button(window)
        self.calculate_button["bg"] = "#efefef"
        self.calculate_button["font"] = self.ft
        self.calculate_button["fg"] = "#000000"
        self.calculate_button["justify"] = "center"
        self.calculate_button["text"] = "calculate"
        self.calculate_button.place(x=10, y=100, width=285, height=35)
        self.calculate_button["command"] = self.calculate

        self.suggest_button = tk.Button(window)
        self.suggest_button["bg"] = "#efefef"
        self.suggest_button["font"] = self.ft
        self.suggest_button["fg"] = "#000000"
        self.suggest_button["justify"] = "center"
        self.suggest_button["text"] = "suggest"
        self.suggest_button.place(x=305, y=100, width=285, height=35)
        self.suggest_button["command"] = self.suggest

        self.label4 = tk.Label(self.window, text="traveling with car")
        self.label4.place(x=10, y=140)
        self.carEntry = tk.Entry(window)
        self.carEntry["borderwidth"] = "1px"
        self.carEntry["font"] = self.ft
        self.carEntry["fg"] = "#333333"
        self.carEntry["justify"] = "center"
        self.carEntry["text"] = "carEntry"
        self.carEntry.place(x=10, y=160, width=440, height=35)

        self.car_box = ttk.Combobox(window)
        self.car_box["font"] = self.ft
        self.car_box["values"] = ["enabled", "unenabled"]
        self.car_box.current(0)
        self.car_box.bind('<Key>', 'break') # หยุดการเปลี่ยน values
        self.car_box.option_add("*TCombobox*Listbox*Font", self.ftSm)
        self.car_box.place(x=460, y=160, width=130, height=35)

        self.label5 = tk.Label(self.window, text="traveling with bus")
        self.label5.place(x=10, y=215)
        self.busEntry = tk.Entry(window)
        self.busEntry["borderwidth"] = "1px"
        self.busEntry["font"] = self.ft
        self.busEntry["fg"] = "#333333"
        self.busEntry["justify"] = "center"
        self.busEntry["text"] = "busEntry"
        self.busEntry.place(x=10, y=235, width=440, height=35)

        self.bus_box = ttk.Combobox(window)
        self.bus_box["font"] = self.ft
        self.bus_box["values"] = ["enabled", "unenabled"]
        self.bus_box.current(0)
        self.bus_box.bind('<Key>', 'break') # หยุดการเปลี่ยน values
        self.bus_box.option_add("*TCombobox*Listbox*Font", self.ftSm)
        self.bus_box.place(x=460, y=235, width=130, height=35)


        self.label6 = tk.Label(self.window, text="traveling with motorcycle")
        self.label6.place(x=10, y=290)
        self.motorcycleEntry = tk.Entry(window)
        self.motorcycleEntry["borderwidth"] = "1px"
        self.motorcycleEntry["font"] = self.ft
        self.motorcycleEntry["fg"] = "#333333"
        self.motorcycleEntry["justify"] = "center"
        self.motorcycleEntry["text"] = "motorcycleEntry"
        self.motorcycleEntry.place(x=10, y=310, width=440, height=35)

        self.motorcy_box = ttk.Combobox(window)
        self.motorcy_box["font"] = self.ft
        self.motorcy_box["values"] = ["enabled", "unenabled"]
        self.motorcy_box.current(0)
        self.motorcy_box.bind('<Key>', 'break') # หยุดการเปลี่ยน values
        self.motorcy_box.option_add("*TCombobox*Listbox*Font", self.ftSm)
        self.motorcy_box.place(x=460, y=310, width=130, height=35)

        self.label7 = tk.Label(self.window, text="traveling with bike")
        self.label7.place(x=10, y=365)
        self.bikeEntry = tk.Entry(window)
        self.bikeEntry["borderwidth"] = "1px"
        self.bikeEntry["font"] = self.ft
        self.bikeEntry["fg"] = "#333333"
        self.bikeEntry["justify"] = "center"
        self.bikeEntry["text"] = "bikeEntry"
        self.bikeEntry.place(x=10, y=385, width=440, height=35)

        self.bike_box = ttk.Combobox(window)
        self.bike_box["font"] = self.ft
        self.bike_box["values"] = ["enabled", "unenabled"]
        self.bike_box.current(0)
        self.bike_box.bind('<Key>', 'break') # หยุดการเปลี่ยน values
        self.bike_box.option_add("*TCombobox*Listbox*Font", self.ftSm)
        self.bike_box.place(x=460, y=385, width=130, height=35)

        self.label8 = tk.Label(self.window, text="traveling with walk")
        self.label8.place(x=10, y=430)
        self.walkEntry = tk.Entry(window)
        self.walkEntry["borderwidth"] = "1px"
        self.walkEntry["font"] = self.ft
        self.walkEntry["fg"] = "#333333"
        self.walkEntry["justify"] = "center"
        self.walkEntry["text"] = "walkEntry"
        self.walkEntry.place(x=10, y=450, width=440, height=35)

        self.walk_box = ttk.Combobox(window)
        self.walk_box["font"] = self.ft
        self.walk_box["values"] = ["enabled", "unenabled"]
        self.walk_box.current(0)
        self.walk_box.bind('<Key>', 'break') # หยุดการเปลี่ยน values
        self.walk_box.option_add("*TCombobox*Listbox*Font", self.ftSm)
        self.walk_box.place(x=460, y=450, width=130, height=35)

    # ฟังก์ชันคำนวณการปล่อยคาร์บอนสำหรับรูปแบบการขนส่งและระยะทางที่กำหนด
    def calculate_carbon_emissions(self, mode, distance, passenger):
        # จำนวนความจุต่อคัน
        divider = {
            'car': math.ceil(passenger/4),
            'bus': math.ceil(passenger/30),
            'motorcycle': math.ceil(passenger/2),
            'bike': passenger,
            'walk': passenger
        }
        # ระบุการปล่อยคาร์บอนสำหรับแต่ละโหมดการเดินทาง (ค่าประมาณ)
        emissions_per_mode = {
            'car': 0.3,   # kg CO2 per km
            'bus': 0.152,
            'motorcycle': 0.45,
            'bike': 0,
            'walk': 0
        }
        return (emissions_per_mode[mode] * distance) * divider[mode]

    # ฟังก์ชั่นแนะนำรูปแบบการเดินทางที่ปล่อย CO2 น้อยที่สุด
    def suggest_trip_mode(self, distance, passenger):
        # คำนวณการปล่อย CO2 สำหรับการเดินทางแต่ละรูปแบบ
        if self.car_box.get() == "unenabled":
            car_emissions = float('inf') # กำหนดค่าเป็นอนันต์ เพื่อหลีกเลี่ยงการคำนวณ
        else:
            car_emissions = self.calculate_carbon_emissions('car', distance, passenger)

        if self.bus_box.get() == "unenabled":
            bus_emissions = float('inf')
        else:
            bus_emissions = self.calculate_carbon_emissions('bus', distance, passenger)

        if self.motorcy_box.get() == "unenabled":
            motorcycle_emissions = float('inf')
        else:
            motorcycle_emissions = self.calculate_carbon_emissions('motorcycle', distance, passenger)

        if self.bike_box.get() == "unenabled":
            bike_emissions = float('inf')
        else:
            bike_emissions = self.calculate_carbon_emissions('bike', distance, passenger)

        if self.walk_box.get() == "unenabled":
            walk_emissions = float('inf')
        else:
            walk_emissions = self.calculate_carbon_emissions('walk', distance, passenger)

        # ค้นหาการปล่อย CO2 น้อยที่สุด
        min_emissions = min(walk_emissions, bike_emissions, motorcycle_emissions, bus_emissions, car_emissions)
        if min_emissions == walk_emissions:
            return 'walk'
        elif min_emissions == bike_emissions:
            return 'bike'
        elif min_emissions == motorcycle_emissions:
            return 'motorcycle'
        elif min_emissions == bus_emissions:
            return 'bus'
        else:
            return 'car'
        
    def verify_can_calculated(self):
        distance = self.distanceEntry.get()
        try:
            distance = float(distance)
        except:
            distance = 0.0
        distance = self.unit_conversion(distance) # แปลงหน่วยเป็นกิโลเมตร

        passenger = self.passenger_box.get()
        try:
            passenger = int(passenger)
        except:
            passenger = 1
            self.passenger_box.current(0)
        
        return distance, passenger
    
    def clear_data(self):
        self.carEntry.delete(0, tk.END)
        self.busEntry.delete(0, tk.END)
        self.motorcycleEntry.delete(0, tk.END)
        self.bikeEntry.delete(0, tk.END)
        self.walkEntry.delete(0, tk.END)
    
    def unit_conversion(self, distance):
        if self.unit_of_length_box.get() == "centimeter":
            return (distance / 100) / 1000
        elif self.unit_of_length_box.get() == "meter":
            return distance / 1000
        elif self.unit_of_length_box.get() == "kilometer":
            return distance

    def calculate(self):
        distance, passenger = self.verify_can_calculated()
        self.clear_data()
        if self.car_box.get() != "unenabled":
            carbon_emissions = self.calculate_carbon_emissions('car', distance, passenger)
            self.carEntry.insert(0, f"Carbon emissions: {carbon_emissions} kg CO2")
        if self.bus_box.get() != "unenabled":
            carbon_emissions = self.calculate_carbon_emissions('bus', distance, passenger)
            self.busEntry.insert(0, f"Carbon emissions: {carbon_emissions} kg CO2")
        if self.motorcy_box.get() != "unenabled":
            carbon_emissions = self.calculate_carbon_emissions('motorcycle', distance, passenger)
            self.motorcycleEntry.insert(0, f"Carbon emissions: {carbon_emissions} kg CO2")
        if self.bike_box.get() != "unenabled":
            carbon_emissions = self.calculate_carbon_emissions('bike', distance, passenger)
            self.bikeEntry.insert(0, f"Carbon emissions: {carbon_emissions} kg CO2")
        if self.walk_box.get() != "unenabled":
            carbon_emissions = self.calculate_carbon_emissions('walk', distance, passenger)
            self.walkEntry.insert(0, f"Carbon emissions: {carbon_emissions} kg CO2")

    def suggest(self):
        distance, passenger = self.verify_can_calculated()
        self.clear_data()
        suggested_mode = self.suggest_trip_mode(distance, passenger)
        carbon_emissions = self.calculate_carbon_emissions(suggested_mode, distance, passenger)
        if suggested_mode == 'car':
            self.carEntry.insert(0, f"Minimal Carbon Emissions: {carbon_emissions} kg CO2")
        elif suggested_mode == 'bus':
            self.busEntry.insert(0, f"Minimal Carbon Emissions: {carbon_emissions} kg CO2")
        elif suggested_mode == 'motorcycle':
            self.motorcycleEntry.insert(0, f"Minimal Carbon Emissions: {carbon_emissions} kg CO2")
        elif suggested_mode == 'bike':
            self.bikeEntry.insert(0, f"Minimal Carbon Emissions: {carbon_emissions} kg CO2")
        elif suggested_mode == 'walk':
            self.walkEntry.insert(0, f"Minimal Carbon Emissions: {carbon_emissions} kg CO2")

if __name__ == '__main__':
    window = tk.Tk()
    window.title("An eco-friendly trip")
    # window size
    width = 600
    height = 500
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    window.geometry(alignstr)
    window.resizable(width=False, height=False)
    Menu(window)
    window.mainloop()
