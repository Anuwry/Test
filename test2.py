class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        return f"{self.name} เปิดใช้งานแล้ว"
    
    def turn_off(self):
        self.is_on = False
        return f"{self.name} ปิดการทำงาน"
    
    def get_status(self):
        return "ON" if self.is_on else "OFF"

class SmartLight(SmartDevice):
    def __init__(self, name, brightness=100, color="White"):
        super().__init__(name)
        self.brightness = brightness
        self.color = color
    
    def adjust_brightness(self, level):
        if level <= 0:
            self.brightness == 0
        elif level >= 100:
            self.brightness == 100
    
    def get_status(self):
        status_text = super().get_status()
        return f"Light [{self.name}] | Status: {status_text} | Brightness: {self.brightness}% | Color: {self.color}"
    
class SmartAirConditioner(SmartDevice):
    def __init__(self, name, temperature=25):
        super().__init__(name)
        self.temperatur = temperature
    
    def set_temperature(self, temp):
        if temp < 18:
            print("ต่ำสุดได้แค่ 18 องศา")
        elif temp > 30:
            print("ต่ำสุดได้แค่ 30 องศา")
        else:
            self.temperatur == temp
            print(f"ค่า {self.temperatur} องศา")
    
    def get_status(self):
        status_text = super().get_status()
        return f"AC [{self.name}] | Status: {status_text} | Temp: {self.temperatur}C"

class SmartHomeHub:
    def __init__(self):
        self.devices = []
    
    def add_device(self, device):
        self.devices.append(device)
    
    def turn_all_off(self):
        print("\n--- 🔌 Executing: Turn All Devices OFF ---")
        for device in self.devices:
            device.turn_off()
    
    def show_dashboard(self):
        print("\n--- 🏠 Smart Home Dashboard ---")
        for device in self.devices:
            print(device.get_status())

if __name__ == "__main__":
    print(">>> เริ่มระบบ Smart Home <<<\n")

    hub = SmartHomeHub()

    # สร้างอุปกรณ์
    light1 = SmartLight("Living Room Light")
    ac1 = SmartAirConditioner("Bedroom AC")

    # เพิ่มเข้า Hub
    hub.add_device(light1)
    hub.add_device(ac1)

    # ทดสอบการทำงาน
    print("--- Test Individual Control ---")
    light1.turn_on()
    light1.adjust_brightness(150) # ลองปรับเกิน 100 (ต้องถูกปัดลง)
    
    ac1.turn_on()
    ac1.set_temperature(16) # ลองปรับเย็นเกิน (ต้อง Error)
    ac1.set_temperature(22) # ลองปรับปกติ (ต้องผ่าน)

    # ดูสถานะรวม
    hub.show_dashboard()

    # สั่งปิดทั้งบ้าน (Polymorphism)
    hub.turn_all_off()
    
    # ดูสถานะอีกครั้งเพื่อยืนยันว่าปิดจริง
    hub.show_dashboard()