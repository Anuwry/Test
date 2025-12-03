class Product:
    def __init__(self, name:str, price:float, quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity
    
class Inventory:
    def __init__(self, store_name):
        self.store_name = store_name
        self.__products = {}
    
    def add_product(self, product_name, price: float, quantity: int):
        key = product_name.lower()
        if key in self.__products:
            existing_product = self.__products[key]
            existing_product += quantity
            if price > existing_product.price:
                existing_product = price
            return f"Updated {product_name} stock."
        else:
            new_product = Product(product_name, price, quantity)
            self.__products[key] = new_product
            return f"Added {product_name} to inventory."
    
    def sell_product(self, product_name, quantity: int):
        found_item = None
        for item in self.__products:
            if item.name.lower() == product_name.lower():
                found_item = item
                break

            if found_item is None:
                return "Error: Product not found."
            if found_item.quantity >= quantity:
                found_item.quantity -= quantity
                total_price = found_item.price * quantity
                return f"Sold {quantity} of {found_item.name} for total {total_price}."
            else:
                return f"Error: Not enough stock for {found_item.name}."
    
    def get_report(self):
        total_value = 0
        unique_count = len(self.__products)
        
        for prod in self.__products.values():
            total_value += (prod.price * prod.quantity)
            
        return f"--- Inventory Report ---\nStore: {self.store_name}\nUnique Products: {unique_count}\nTotal Value: {total_value}"

if __name__ == "__main__":
    my_store = Inventory("MyStore")
    while True:
        try:
            user_input = input("Enter command: ").strip()
            parts = user_input.split()

            if not parts:
                continue
            command = parts[0].lower()

            if command == "exit":
                print("Goodbye")
                break

            elif command == "report":
                print(my_store.get_report())
            elif command == "restock":
                if len(parts) == 4:
                    name = parts[1]
                    try:
                        price = float(parts[2])
                        quantity = int(parts[3])
                        print(my_store.add_product(name, price, quantity))
                    except ValueError:
                        print("Error: Invalid price or quantity.")
                else:
                    print("Error: Invalid command.")
            elif command == "sell":
                if len(parts) == 3:
                    name = parts[1]
                    try:
                        quantity = int(parts[2])
                        print(my_store.sell_product(name, quantity))
                    except ValueError:
                            print("Error: Invalid quantity.")
                else:
                    print("Error: Invalid command.")
            
            elif command == "report":
                print(my_store.get_report())
            else:
                print("Error: Invalid command.")
        except Exception:
            print("Error: Invalid command.")