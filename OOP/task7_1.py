import re

class Book:

    def __init__(self, title, author, ISBN, price):
        self.book_title = title
        self.book_author = author
        self.book_ISBN = ISBN
        self.price = price

    def __set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def __set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author

    def __set_ISBN(self, ISBN):
        if len(str(ISBN)) != 13:
            print('Неверный ISBN')
        self.__ISBN = ISBN

    def get_ISBN(self):
        return self.__ISBN

    book_title = property(get_title, __set_title)
    book_author = property(get_author, __set_author)
    book_ISBN = property (get_ISBN, __set_ISBN)

class EBook(Book):

    def __init__(self, title, author, ISBN, price, form, file_size, download_link):
        super().__init__(title, author, ISBN, price)
        self.form = form
        self.file_size = file_size
        self.book_download_link = download_link



    def __set_download_link(self, download_link):
        pattern = r'^https://'
        if re.match(pattern, download_link):
            self.__download_link = download_link
        else:
            print("URL-адрес не начинается с https://")

    def get_download_link(self):
        return self.__download_link

    book_download_link = property(get_download_link, __set_download_link)


class PhysicalBook(Book):
    def __init__(self, title, author, ISBN, price, Weight):
        super().__init__(title, author, ISBN, price)
        self.book_Weight = f"{Weight} гр."
        self.available = 'В наличии'

    def __set_Weight(self, title):
        self.__Weight = title

    def get_Weight(self):
        return self.__Weight

    def update_availability(self, available):
        self.available = available

    book_Weight = property(get_Weight, __set_Weight)


class Customer:
    def __init__(self, name, email, address):
        self.customer_name = name
        self.customer_email = email
        self.customer_address = address
        self.cart = ShoppingCart()
        self.__discount = 0

    def __set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def __set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def __set_discount(self, discount):
        self.__discount = discount

    def get_discount(self):
        return self.__discount


    customer_name = property(get_name, __set_name)
    customer_email = property(get_email, __set_email)
    customer_address = property(get_address, __set_address)
    discount = property(get_discount, __set_discount)


class ShoppingCart:
    def __init__(self):
        self.directory = []

    def add_book(self, book):
        if book.available == 'В наличии':
            self.directory.append(book)
            print(f'Товар добавлен в корзину')
        else:
            print('Товара нет в наличии')

    def delete_book(self, book):
        if book in self.directory:
            self.directory.remove(book)
            print(f'Товар удален из корзины')
        else:
            print('Товар не найден в корзине')

    def calculate_the_amount(self):
        my_sum = 0
        for book in self.directory:
            my_sum += book.price
        return (f"Общая сумма заказа составляет: {my_sum} €")


    def calculate_amount_with_discount(self, discount):
        my_sum = 0
        for book in self.directory:
            my_sum += book.price
        my_sum = round((my_sum * (1 - (discount / 100))), 2)
        return my_sum

    def show_directory(self):
        return self.directory

class PremiumCustomer(Customer):
    def __init__(self, name, email, address, membership_status):
        super().__init__(name, email, address)
        self.customer_membership_status = membership_status

    def __set_membership_status(self, membership_status):
        self.__membership_status = membership_status

    def get_membership_status(self):
        return self.__membership_status

    def apply_discount_to_cart(self, discount):
        if self.customer_membership_status == 'Premium':
            total_with_discount = self.cart.calculate_amount_with_discount(discount)
            print(f"Общая сумма заказа со скидкой {discount}% составляет: {total_with_discount} €")
        else:
            print("Только Premium клиенты могут применять скидку")

    customer_membership_status = property(get_membership_status, __set_membership_status)

class Order:
    def __init__(self, customer):
        self.customer = customer

    def display_order(self):
        customer_name = self.customer.customer_name
        cart_contents = self.customer.cart.show_directory()

        print(f"Имя покупателя: {customer_name}")
        print("Cписок покупок (название книги и цена):")
        for item in cart_contents:
            print(f" - {item.book_title} - {item.price} €")
        if isinstance(self.customer, PremiumCustomer):
            self.customer.apply_discount_to_cart(discount=10)
        else:
            cart_total = self.customer.cart.calculate_the_amount()
            print(f"{cart_total}")



# Создание клиентов
customer1 = Customer('Fidoriya Yarmord', 'FidoriyaYarmord0483@mail.ru', '247 Earline Isle Erdmanshire')
customer2 = Customer('Boaz Elodiya', 'BoazElodiya173@mail.ru', '1168 Kian Squares Apt. 062')
customer3 = Customer('Kate Boris','kate34@mail.ru', 'Minsk, Koltsova 5-10')

# Создание Premium клиентов
customer_Premium1 = PremiumCustomer('Ronald Curry',  'bernard32@jordaan.lp.school.za',
                                    '741 Wolmarans St', 'Premium')

# Создание электронных книг
book1 = EBook('Безумие толпы', 'Дуглас Мюррей', 9785386142865, 25, 'ePub)', 1.8,
              'https://chitatel.by/catalog/book/1851944')
book2 = EBook('Светоч разума', 'Кристер Стурмарк', 	9785171330385, 36, 'PDF', 27,
              'https://oz.by/books/more101096093')

# Создание физических книг
book3 = PhysicalBook('ПУТЕШЕСТВИЕ В ЭЛЕВСИН', 'Пелевин В.О.', 9785041878504, 29.35,
                     489)
book4 = PhysicalBook('KARMALOGIC', 'Ситников А.П.', 9785386104610, 59.78, 840)

print(book4.available)
book4.update_availability('Нет в наличии')
print(book4.available)
book4.update_availability('В наличии')



# Добавление и удаление товаров
customer1.cart.directory.append(book3)
customer_Premium1.cart.directory.append(book3)
customer_Premium1.cart.directory.append(book2)
customer_Premium1.cart.delete_book(book2)
customer3.cart.directory.append(book2)
customer2.cart.add_book(book4)
customer_Premium1.cart.directory.append(book2)


# Просмотр общей стоимости корзин
print(customer1.cart.calculate_the_amount())
print(customer_Premium1.cart.calculate_the_amount())
print(customer2.cart.calculate_the_amount())

# Создание заказов
order1 = Order(customer_Premium1)
order2 = Order(customer1)
order3 = Order(customer2)
order4 = Order(customer3)

order1.display_order()
order2.display_order()
order3.display_order()
order4.display_order()





