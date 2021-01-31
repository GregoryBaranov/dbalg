class Dish():
    def set_dish_information(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.dish = self.name + "(" + self.quantity + ")" + " - " + self.price
    def get_dish_information(self):
        return self.dish

class Menu:
    def set_menu_information(self, name):
        self.name = name
        self.products = []
    def set_menu(self, dish):
        self.dish = dish
        self.products.append(self.dish)
    def get_menu(self):
        print(self.name)
        return self.products

class Receipt():
    result = 0
    def set_order_information(self, name):
        self.name = name
        self.order = []
    def set_order(self, parametr1, parametr2):
        self.parametr1 = parametr1
        self.order.append(self.parametr1)
        self.parametr2 = parametr2
        self.result = self.result + int(self.parametr2)
    def get_order(self):
        print("Общий чек: ")
        return self.order
    def get_result(self):
        print("Итого: ")
        return self.result

def menu_entry(name_menu):
    for i in range(question1):
        name = input("Введите название блюда: ")
        quantity = input("Введите размер порции (только цифру): ")
        price = input("Введите цену за 1 порцию (только цифру): ")
        d = Dish()
        d.set_dish_information(name, quantity, price)
        name_menu.set_menu(d)

def menu_output(name_menu):
    name_menu.get_menu()
    for i in name_menu.products:
        print(i.name + "(" + i.quantity + "гр." +")" + " - " + i.price + "руб.")

def order_entry(name_menu):
    for i in range(question4):
        question = input("Введите блюдо: ")
        for j in name_menu.products:
            if j.name == question:
                check.set_order(j, j.price)
    check.get_order()
    for i in check.order:
        print(i.name + "(" + i.quantity + "гр." +")" + " - " + i.price + "руб.")
    check.get_result()
    print(str(check.result) + "руб.")

br = Menu()
din = Menu()
bs = Menu()
check = Receipt()

br.set_menu_information("Завтраки")
din.set_menu_information("Ужины")
bs.set_menu_information("Бизнес-ланчи")
check.set_order_information("Сделать заказ")

print('''
Это программа для "Онлайн-заказа еды".
В ней доступны следующие действия:
1 - Заполнить меню
2 - Вывести меню
3 - Сделать заказ
0 - Закончить выполнение программы
Виды меню:
11 - Завтраки
22 - Ужины
33 - Бизнес-ланчи
Чтобы сделать какое либо действие, введите соответствующие цифры.
''')

question = input("Что вы желаете сделать?")
while question != "0":
    if question == "1":
        question1 = int(input("Сколько блюд вы желаете добавить (введите цифру)?  "))
        question2 = input("Какое меню хотите заполнить?")
        if question2 == "11":
            menu_entry(br)
        if question2 == "22":
            menu_entry(din)
        if question2 == "33":
            menu_entry(bs)
        question = input("Что вы желаете сделать?")
    if question == "2":
        question3 = input("Какое меню хотите вывести? ")
        if question3 == "11":
            menu_output(br)
        if question3 == "22":
            menu_output(din)
        if question3 == "33":
            menu_output(bs)
        question = input("Что вы желаете сделать?")
    if question == "3":
        question4 = int(input("Сколько блюд вы желаете заказать (введите цифру)? "))
        question5 = input("Из какого меню? ")
        if question5 == "11":
            order_entry(br)
        if question5 == "22":
            order_entry(din)
        if question5 == "33":
            order_entry(bs)
        question = input("Что вы желаете сделать?")
