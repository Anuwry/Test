class Character:
    def __init__(self, name, max_hp, attack_power):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack_power = attack_power
    
    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            print(f"[{self.name}] โดนโจมตี {damage}! (HP เหลือ 0)")
            print(f"[{self.name} พ่ายแพ้แล้ว]")
        else:
            print(f"[{self.name}] โดนโจมตี {damage}! (HP เหลือ {self.hp})")

    def attack(self, target):
        if self.hp == 0:
            return
        else:
            print(f"[{self.name}] โจทตีปกติใส่ [{target.name}]")
            target.take_damage(self.attack_power)
    
    def get_status(self):
        return f"[{self.name}] HP: {self.hp}/{self.max_hp}"
    
class Warrior(Character):
    def __init__(self, name, max_hp, attack_power, max_stamina):
        super().__init__(name, max_hp, attack_power)
        self.stamina = max_stamina

    def heavy_slash(self, target):
        if self.hp == 0:
            return
        if self.stamina < 20:
            print(f"Stamina ไม่พอ!")
            return
        
        self.stamina -= 20
        print(f"[{self.name}] ใข้ Heavy Slash ใส่ [{target.name}]")
        total_damage = self.attack_power * 2
        target.take_damage(total_damage)

class Mage(Character):
    def __init__(self, name, max_hp, attack_power, max_mana):
        super().__init__(name, max_hp, attack_power)
        self.mana = max_mana

    def fire_ball(self, target):
        if self.hp == 0:
            return
        if self.mana < 30:
            print(f"Mana ไม่พอ!")
            return
        
        self.mana -= 30
        print(f"[{self.name}] ร่าย Fire Ball ใส่ [{target.name}]")
        target.take_damage(80)

if __name__ == "__main__":
    print(">>> เริ่มการประลองเวทีเดือด! <<<\n")

    # สร้างตัวละคร
    # Warrior: เลือดเยอะ (200), ตี 15, Stamina 50
    arthur = Warrior("Arthur", 200, 15, 50) 
    
    # Mage: เลือดน้อย (100), ตีเบา (5), Mana 100
    merlin = Mage("Merlin", 100, 5, 100)

    # Round 1: Arthur เปิดก่อน
    print("\n--- Round 1 ---")
    arthur.attack(merlin)       # ตีธรรมดา (15 dmg)
    
    # Round 2: Merlin สวนด้วยเวทย์
    print("\n--- Round 2 ---")
    merlin.fire_ball(arthur)    # โดนไป 80 จุกๆ

    # Round 3: Arthur ใช้ท่าไม้ตาย
    print("\n--- Round 3 ---")
    arthur.heavy_slash(merlin)  # ตีแรง 2 เท่า (30 dmg)

    # Round 4: Merlin มานาหมด (สมมติ) ลองร่ายเวทย์รัวๆ
    print("\n--- Round 4 ---")
    merlin.mana = 10            # แอบโกงลดมานาเหลือ 10
    merlin.fire_ball(arthur)    # ต้องร่ายไม่ได้

    # Round 5: Arthur ปิดบัญชี
    print("\n--- Round 5 (Final) ---")
    arthur.heavy_slash(merlin)  # ตีอีก 30 dmg
    arthur.heavy_slash(merlin)  # ตีอีก 30 dmg (Merlin น่าจะตายรอบนี้)

    # เช็คศพ (Merlin ตายแล้ว ต้องลุกมาตีไม่ได้)
    print("\n--- Check Dead Body ---")
    merlin.attack(arthur)       # ต้องตีไม่ได้