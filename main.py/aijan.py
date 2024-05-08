class Product:

    def __init__(self):
        self.products={}

    def  create(self, name, description, price,kilo, category, date):
        self.name = name
        self.description = description
        self.price = price
        self.kilo= kilo
        self.category = category
        self.date = date

    def read(self):

        return f"{self.name} ,{self.description}, {self.price} *{self.kilo},{self.category}, {self.date}"



    def update(self, name, new_description):
        if name in self.products:
            self.products[name] = new_description
        else:
            print('error')

    def delete(self, price):
        if price in self.products:
            del self.products[price]
        else:
            print('error')
    def sum_price(self):
        return f'{self.price}* {self.kilo} = {self.price*self.kilo}'

product1=Product()

product1.create('apple ','gsjlgnf' ,140 ,6,'fruits','2024')
product1.create('banana','fsvsv', 180,4,'fruits',2024)
product1.update('apple','ygfbewib')
product1.delete(140 )

print(product1.create())
