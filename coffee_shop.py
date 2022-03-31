class CoffeeShop:
    
    
    # Método de inicialização da classe, onde se deve passar o nome, menu e pedidos.
    # A variavel "orders" praticamente não é utilizada. Nos testes do edabit é passado o construtor list() em "orders", o que poderia ser feito
    # internamente ao criar o __init__.
    def __init__(self, name, menu, orders):
        # nome da loja de café, não é utilizado nos testes.
        self.cs_name = name
        # lista de dicionários, onde cada dicionário é um produto com nome, preço e tipo.
        self.menu = menu
        # declara uma lista vazia, pois nos testes é utilizado o construtor list()
        self.orders_list = orders
        # total devido
        self.due_amount_val = 0
    
    # Função para pesquisar item e algum atributo desse item (nome, preço, tipo), retorna o atributo do item, ou False caso não haja esse item.
    def search_order(self, order, atribute):
        # Checa se o "order" passado corresponde ao nome de algum produto no menu.
        for item in self.menu:
            if order == item["item"]:
                return item[atribute]
        return False
    
    # Adiciona um pedido a lista de pedidos, adiciona o item ao final (o exercício pedia que fosse do tipo "primeiro a pedir, primeiro a receber").
    # Também adiciona o custo do pedido ao total devido.
    def add_order(self, order):
        # Se search_order retorna falso, significa que o item não está no menu.
        if not self.search_order(order, "item"):
            return "This item is currently unavailable!"
        # append() adiciona o item ao final da lista, possibilitando o "primeiro a pedir, primeiro a receber"
        self.orders_list.append(self.search_order(order, "item"))
        self.due_amount_val += self.search_order(order, "price")
        # Tive que arredondar o total devido, pois quando é realizada a subtração, ela tende a criar mais casas decimais.
        self.due_amount_val = round(self.due_amount_val, 2)
        return "Order added!"
    
    # Retira o pedido mais antigo da lista, e subtrai o custo do item do total devido.
    def fulfill_order(self):
        # Se não houverem itens na lista, retorna que todos pedidos foram concluídos.
        if not self.orders_list:
            return "All orders have been fulfilled!"
        order = self.orders_list[0]
        self.due_amount_val -= self.search_order(order, 'price')
        # Tive que arredondar os preços e o total devido, pois números do tipo float tendem a causar erros quando tem mais de 2 pontos decimais.
        self.due_amount_val = round(self.due_amount_val, 2)
        # deleta o primeiro item da lista, que foi o primeiro a ser pedido.
        del self.orders_list[0]
        return 'The {} is ready!'.format(order)
    
    # Retorna a lista dos itens que foram pedidos e não foram concluidos.
    def list_orders(self):
        return self.orders_list
    
    # Retorna o total devido.
    def due_amount(self):
        if self.due_amount_val == 0:
            return 0
        return self.due_amount_val
    
    # Retorna o item mais barato do menu.
    def cheapest_item(self):
        cheapest = self.menu[0]['price']
        # Loop for para analisar cada item no menu, começando pelo primeiro.
        for item in self.menu:
            if item['price'] < cheapest:
                cheapest = item['price']
                cheapest_name = item['item']
        return cheapest_name
    
    # Retorna uma lista com somente os itens do tipo bebida do menu.
    def drinks_only(self):
        drinks = []
        for item in self.menu:
            if item['type'] == 'drink':
                drinks.append(item['item'])
        return drinks
    
    # Retorna uma lista com somente os itens do tipo comida do menu.
    def food_only(self):
        food = []
        for item in self.menu:
            if item['type'] == 'food':
                food.append(item['item'])
        return food
