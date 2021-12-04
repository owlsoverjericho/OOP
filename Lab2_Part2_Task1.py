class Product:
    def __init__(self, price = 0, name = "TBU", description = "TBU", dimentions = "TBU"):
        self.price = price;
        self.name = name;
        self.description = description;
        self.dimentions = dimentions;

class Client:
    def __init__(self, name, surname, patronymic, phone_number):
        self.name = name;
        self.surname = surname;
        self.patronymic = patronymic;
        self.phone_number = phone_number;

class Order:
    orderList = [];
    def getClientInfo(self, Client):
        self.user = Client;
    def addItem(self, Product):
        self.orderList.append(Product);
    def showOrderList(self):
        for item in self.orderList:
            print(f"Product name: {item.name} \n Product Description: {item.description} \n Price: {item.price} \n Dimentions: {item.dimentions}");
    def showUserInfo(self):
        print(f"Client`s name: {self.user.name}\nClient's phone number: {self.user.phone_number}")
        
user1488 = Client('John', 'Smith', 'Smithovich', '+380671240791');

item1488 = Product(1500, "GTX 1080Ti", "Graphics card", "100x100x100");

item1489 = Product(499, "GTX 750", "GPU", "50x50x50");

ShoppingCart = Order();

ShoppingCart.getClientInfo(user1488);
ShoppingCart.addItem(item1488);
ShoppingCart.addItem(item1489);
ShoppingCart.showOrderList();
ShoppingCart.showUserInfo();
