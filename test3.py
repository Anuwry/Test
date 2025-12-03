import random

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} ({self.price} บาท)"

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []
        self.earning = 0

    def add_menu(self, item_name, item_price):
        new_item = MenuItem(item_name, item_price)
        self.menu.append(new_item)
    
    def show_menu(self):
        for b in self.menu:
            print(b)
    
    def find_item(self, item_name):
        for b in self.menu:
            if b.name == item_name:
                return b
        return None
    
    def receive_income(self, amount):
        self.earning += amount

class Customer:
    def __init__(self, name):
        self.name = name
        self.wallet = 0
    
    def top_up(self, amount):
        self.wallet += amount
    
    def deduct_money(self, amount):
        if self.wallet >= amount:
            self.wallet -= amount
            return True
        else:
            return False

class Rider:
    def __init__(self, name):
        self.name = name
        self.wallet = 0
    
    def receive_job(self, delivery_fee):
        self.wallet += delivery_fee
        return f"ไรเดอร์ {self.name} ส่งอาหารสำเร็จ!"

class DeliveryApp:
    def __init__(self):
        self.riders = []

    def add_rider(self, rider):
        self.riders.append(rider)
    
    def process_order(self, customer, restaurant, food_name):
        find = restaurant.find_item(food_name)
        if find == None:
            print("ไม่มีเมนูนี้")
            return
        
        delivery_fee = 20
        total = find.price + delivery_fee
        if customer.deduct_money(total):
            restaurant.receive_income(find.price)

            if len(self.riders) > 0:
                selected_rider = random.choice(self.riders)
                selected_rider.receive_job(20)
                print("--- สั่งซื้อสำเร็จ ---")
                print(f"ลูกค้า: {customer.name}")
                print(f"เมนู: {find.name} ({find.price} บาท)")
                print(f"ค่าส่ง: {delivery_fee} บาท")
                print(f"รวมทั้งสิ้น: {total} บาท")
                print(f"ไรเดอร์ที่รับงาน: {selected_rider.name}")
            else:
                print("ระบบผิดพลาด: ไม่มีไรเดอร์ในระบบ")
        else:
            print("สั่งซื้อล้มเหลว เงินไม่พอ")

if __name__ == "__main__":
    shop = Restaurant("เจ๊ไฝ")
    shop.add_menu("ไข่เจียวปู", 1000)
    shop.add_menu("กะเพรา", 50)
    shop.show_menu() # ลองปริ้นเมนูดู

    # 2. สร้างลูกค้าและเติมเงิน
    user = Customer("Somchai")
    user.top_up(2000)
    print(f"\nลูกค้า {user.name} มีเงิน: {user.wallet} บาท")

    # 3. สร้างระบบแอปและไรเดอร์
    app = DeliveryApp()
    rider1 = Rider("Man")
    rider2 = Rider("Boy")
    app.add_rider(rider1)
    app.add_rider(rider2)

    # 4. ทดสอบสั่งอาหาร
    print("\n--- เริ่มการสั่งซื้อ 1 ---")
    app.process_order(user, shop, "ไข่เจียวปู") # ควรสำเร็จ

    print("\n--- เริ่มการสั่งซื้อ 2 ---")
    app.process_order(user, shop, "กะเพรา") # ควรสำเร็จ

    print("\n--- เริ่มการสั่งซื้อ 3 ---")
    app.process_order(user, shop, "หูฉลาม") # เมนูไม่มี

    print("\n--- เริ่มการสั่งซื้อ 4 ---")
    app.process_order(user, shop, "ไข่เจียวปู") # เงินไม่พอแล้ว (เหลือ 900 กว่าบาท)