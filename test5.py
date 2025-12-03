class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self):
        if self.stock >= 1:
            self.stock -= 1
        else:
            print("Out of stock")
    
    def has_stock(self):
        if self.stock >= 1: return True
        return False
    
    def get_details(self):
        return f"{self.name} ({self.price} บาท) - เหลือ {self.stock} ชิ้น"

class Drink(Product):
    def __init__(self, name, price, stock, volume):
        super().__init__(name, price, stock)
        self.volume = volume
    
    def get_details(self):
        return f"{super().get_details()} [{self.volume}] mL"

class Snack(Product):
    def __init__(self, name, price, stock, weight):
        super().__init__(name, price, stock)
        self.weight = weight
    
    def get_details(self):
        return f"{super().get_details()} [{self.weight}] g"

class VendingMachine:
    def __init__(self):
        self.products = []
        self.balance = 0
    
    def add_product(self, product):
        self.products.append(product)
    
    def insert_money(self, amount):
        self.balance += amount
        print(f"ยอดเงิน {self.balance}")
    
    def show_menu(self):
        for i,b in enumerate(self.products):
            print(f"{i+1}. {b.get_details()}")
    
    def select_product(self, product_name):
        found = None
        for b in self.products:
            if b.name == product_name:
                found = b
                break
        if found == None:
            print(f"ไม่พบสินค้า")
            return
        
        if not found.has_stock():
            print(f"สินค้าหมดแล้ว")
            return
        
        if self.balance < found.price:
            need = found.price - self.balance
            print(f"เงินไม่พอ")
            return
        
        self.balance -= found.price
        found.reduce_stock()
        print(f"รับสินค้า [{found.name}] เรียบร้อย")
        print(f"เงินคงเหลืออยู่ {self.balance} บาท")
    
    def return_change(self):
        if self.balance > 0: 
            print(f"ได้รับเงินทอนทั้งสิ้น {self.balance}")
        self.balance = 0

if __name__ == "__main__":
    machine = VendingMachine()
    coke = Drink("Coke", 20, 5, 325)
    lays = Snack("Lays", 30, 2, 50)
    machine.add_product(coke)
    machine.add_product(lays)
    machine.show_menu()

    print("\n--- Test 1: เงินไม่พอ ---")
    machine.insert_money(10)
    machine.select_product("Coke")

    print("\n--- Test 2: ซื้อสำเร็จ ---")
    machine.insert_money(20)
    machine.select_product("Coke")
    
    print("\n--- Test 3: เหมา Lays จนหมด ---")
    machine.insert_money(100)
    machine.select_product("Lays")
    machine.select_product("Lays")
    machine.select_product("Lays")

    print("\n--- Test 4: คืนเงิน ---")
    machine.return_change()