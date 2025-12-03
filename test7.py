class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_details(self):
        return f"Name: {self.name} ({self.age} y.o.)"
    
class Patient(Person):
    def __init__(self, name, age, hp):
        super().__init__(name, age)
        self.hp = hp
    
    def is_healthy(self):
        if self.hp == 100:
            return True
        else:
            return False
    
    def receive_treatment(self, amount):
        new_hp = self.hp + amount
        if self.hp > 100:
            self.hp = 100
        print(f"[{self.name}] อาการดีขึ้น! (HP: {self.hp} -> {new_hp})")
        self.hp += amount
    
    def get_details(self):
        status = "Healthy" if self.is_healthy else "Sick"
        return f"[Patient] {super().get_details()} HP: {self.hp}/100 | {status}"
    
class Doctor(Person):
    def __init__(self, name, age, energy=100):
        super().__init__(name, age)
        self.energy = energy
    
    def heal(self, patient):
        if self.energy < 10:
            print(f"หมอ [{self.name}] หมดแรง! ต้องการพักผ่อน")
            return
        if patient.is_healthy() == True:
            print(f"คนไข้ [{self.name}] แข็งแรงดีแล้ว ไม่ต้องรักษา")
            return
        
        self.energy -= 10
        patient.receive_treatment(20)
        print(f"หมอ [{self.name}] รักษาคนไข้สำเร็จ! (Energy เหลือ {self.energy})")

    def rest(self):
        self.energy = 100
        print(f"หมอ {self.name} พักผ่อนเต็มที่! (Energy: 100)")

    def get_details(self):
        return f"[Doctor] {super().get_details()} | Energy: {self.energy}/100"
    
class Hospital:
    def __init__(self, name):
        self.name = name
        self.people = []

    def admit(self, person):
        self.people.append(person)

    def show_everyone(self):
        print(f"\n--- 🏥 รายชื่อในโรงพยาบาล: {self.name} ---")
        for b in self.people:
            print(b.get_details())
        print("-" * 30)
    
    def start_treatment_process(self, doctor_name, patient_name):
        print(f"🔄 เรียกตัวหมอ {doctor_name} เพื่อรักษา {patient_name}...")
        doc = None
        pat = None
        for b in self.people:
            if isinstance(b, Doctor) and b.name == doctor_name:
                doc = b
            elif isinstance(b, Patient) and b.name == patient_name:
                pat = b
        
        if doc is None or pat is None:
            print(f"ไม่พบข้อมูลหมอหรือคนไข้")
            return
        
        doc.heal(pat)

if __name__ == "__main__":
    hos = Hospital("Bangkok General")

    # สร้างหมอและคนไข้
    d1 = Doctor("Dr. Strange", 40)      # Energy 100
    p1 = Patient("Tony", 50, 50)        # ป่วย HP 50
    p2 = Patient("Steve", 90, 100)      # แข็งแรง HP 100
    
    hos.admit(d1)
    hos.admit(p1)
    hos.admit(p2)

    hos.show_everyone()

    # Case 1: รักษาปกติ
    hos.start_treatment_process("Dr. Strange", "Tony") # HP 50 -> 70, Energy 90
    hos.start_treatment_process("Dr. Strange", "Tony") # HP 70 -> 90, Energy 80
    hos.start_treatment_process("Dr. Strange", "Tony") # HP 90 -> 100, Energy 70

    # Case 2: รักษาคนหายแล้ว (ต้องไม่เสียแรงหมอ)
    hos.start_treatment_process("Dr. Strange", "Tony") 

    # Case 3: หมอหมดแรง (Hack Energy ทดสอบ)
    d1.energy = 5 
    hos.start_treatment_process("Dr. Strange", "Tony") # หมอต้องปฏิเสธ

    # Case 4: รักษาคนไม่มีตัวตน
    hos.start_treatment_process("Dr. Strange", "Thanos")

    # สรุปผล
    hos.show_everyone()