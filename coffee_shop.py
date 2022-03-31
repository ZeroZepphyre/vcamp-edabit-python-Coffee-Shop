class CoffeeShop:
    def __init__(self, name, menu, orders):
        self.cs_name = name
        self.menu = menu
        self.orders_list = orders
        self.due_amount_val = 0

    def search_order(self, order, atribute):
        for item in self.menu:
            if order == item["item"]:
                return item[atribute]
        return False

    def add_order(self, order):
        if not self.search_order(order, "item"):
            return "This item is currently unavailable!"
        self.orders_list.append(self.search_order(order, "item"))
        self.due_amount_val += self.search_order(order, "price")
        self.due_amount_val = round(self.due_amount_val, 2)
        return "Order added!"

    def fulfill_order(self):
        if not self.orders_list:
            return "All orders have been fulfilled!"
        order = self.orders_list[0]
        self.due_amount_val -= self.search_order(order, 'price')
        self.due_amount_val = round(self.due_amount_val, 2)
        del self.orders_list[0]
        return 'The {} is ready!'.format(order)

    def list_orders(self):
        return self.orders_list

    def due_amount(self):
        if self.due_amount_val == 0:
            return 0
        return self.due_amount_val

    def cheapest_item(self):
        cheapest = self.menu[0]['price']
        for item in self.menu:
            if item['price'] < cheapest:
                cheapest = item['price']
                cheapest_name = item['item']
        return cheapest_name

    def drinks_only(self):
        drinks = []
        for item in self.menu:
            if item['type'] == 'drink':
                drinks.append(item['item'])
        return drinks

    def food_only(self):
        food = []
        for item in self.menu:
            if item['type'] == 'food':
                food.append(item['item'])
        return food
