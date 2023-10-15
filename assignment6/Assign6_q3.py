 #  Create a class named Mobile with attributes ModelName,Company,Price and with methods:
 #  set_attributes, print_details and can_afford


class Mobile:
    def set_attributes(self, model, company, price):
        setattr(self, 'model', model)
        setattr(self, 'company', company)
        setattr(self, 'price', price)

    def print_details(self):
        print(f"model: {getattr(self, 'model')}")
        print(f"company: {getattr(self, 'company')}")
        print(f"price: {getattr(self, 'price')}")

    def can_afford(self):
        if getattr(self, 'price') >= 20000:
            print(f"{getattr(self, 'model')} is NOT affordable")
        else:
            print(f"{getattr(self, 'model')} is affordable")


m1 = Mobile()
m1.set_attributes('M33', 'Samsung', 18999)
m1.can_afford()
m1.print_details()
