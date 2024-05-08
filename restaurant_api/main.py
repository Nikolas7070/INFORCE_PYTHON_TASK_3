import psycopg2
from psycopg2 import Error
from datetime import date


class Database:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                dbname="postgres", user="postgres", password="49952004", host="127.0.0.1", port="5432"
            )
            self.cursor = self.connection.cursor()
            print("Подключение к базе данных установлено успешно")
        except Error as error:
            print("Ошибка при подключении к базе данных:", error)

    def __del__(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Соединение с базой данных закрыто")


class Authentication:
    def __init__(self, db):
        self.db = db

    def add_user(self, username, password, email):
        try:
            insert_user_query = '''INSERT INTO users (username, email, password) VALUES (%s, %s, %s)'''
            self.db.cursor.execute(insert_user_query, (username, email, password))
            self.db.connection.commit()
            print("Пользователь успешно добавлен.")
        except Error as error:
            print("Ошибка при добавлении пользователя:", error)

    def remove_user(self, user_id):
        try:
            delete_user_query = '''DELETE FROM users WHERE user_id = %s'''
            self.db.cursor.execute(delete_user_query, (user_id,))
            self.db.connection.commit()
            print("Пользователь успешно удален.")
        except Error as error:
            print("Ошибка при удалении пользователя:", error)


class RestaurantService:
    def __init__(self, db):
        self.db = db

    def add_restaurant(self, name, owner):
        try:
            insert_restaurant_query = '''INSERT INTO restaurants (name, owner) VALUES (%s, %s)'''
            self.db.cursor.execute(insert_restaurant_query, (name, owner))
            self.db.connection.commit()
            print("Ресторан успешно добавлен.")
        except Error as error:
            print("Ошибка при добавлении ресторана:", error)

    def remove_restaurant(self, restaurant_id):
        try:
            delete_restaurant_query = '''DELETE FROM restaurants WHERE restaurant_id = %s'''
            self.db.cursor.execute(delete_restaurant_query, (restaurant_id,))
            self.db.connection.commit()
            print("Ресторан успешно удален.")
        except Error as error:
            print("Ошибка при удалении ресторана:", error)


class MenuService:
    def __init__(self, db):
        self.db = db

    def add_menu(self, restaurant_id, item_name, description, price, days=date.today()):
        try:
            insert_menu_query = '''INSERT INTO menu (restaurant_id, item_name, description, price, days) 
                                   VALUES (%s, %s, %s, %s, %s)'''
            self.db.cursor.execute(insert_menu_query, (restaurant_id, item_name, description, price, days))
            self.db.connection.commit()
            print("Пункт меню успешно добавлен.")
        except Error as error:
            print("Ошибка при добавлении пункта меню:", error)

    def get_menu(self, restaurant_id, days=date.today()):
        try:
            get_menu_query = '''SELECT item_name, description, price FROM menu 
                                WHERE restaurant_id = %s AND days = %s'''
            self.db.cursor.execute(get_menu_query, (restaurant_id, days))
            menu_items = self.db.cursor.fetchall()

            if menu_items:
                print(f"Меню для ресторана с id {restaurant_id} на день {days}:")
                for item in menu_items:
                    print(f"Название: {item[0]}, Описание: {item[1]}, Цена: {item[2]}")
            else:
                print(f"Меню для ресторана с id {restaurant_id} на день {days} отсутствует.")
        except Error as error:
            print("Ошибка при получении меню:", error)

    def remove_menu(self, item_id):
        try:
            delete_menu_query = '''DELETE FROM menu WHERE item_id = %s'''
            self.db.cursor.execute(delete_menu_query, (item_id,))
            self.db.connection.commit()
            print("Пункт меню успешно удален.")
        except Error as error:
            print("Ошибка при удалении пункта меню:", error)


# Создание экземпляра базы данных
db = Database()

# Создание сервиса аутентификации, ресторанов и меню с передачей экземпляра базы данных
auth_service = Authentication(db)
restaurant_service = RestaurantService(db)
menu_service = MenuService(db)


def crate_db():
    try:
        connection = psycopg2.connect(dbname="postgres", user="postgres", password="49952004", host="127.0.0.1",
                                      port="5432")
        print("Подключение установлено")
        cursor = connection.cursor()

        # Створення таблиці "users"
        create_users_table_query = '''CREATE TABLE IF NOT EXISTS users (
                                          user_id SERIAL PRIMARY KEY,
                                          username TEXT NOT NULL,
                                          email TEXT NOT NULL UNIQUE,
                                          password TEXT NOT NULL
                                          )'''
        cursor.execute(create_users_table_query)

        # Створення таблиці "menu"
        create_menu_table_query = '''CREATE TABLE IF NOT EXISTS menu (
                                    item_id SERIAL PRIMARY KEY,
                                    item_name TEXT NOT NULL,
                                    restaurant_id INTEGER NOT NULL,
                                    days INTEGER NOT NULL,
                                    description TEXT,
                                    price NUMERIC(10, 2) NOT NULL
                                    )'''
        cursor.execute(create_menu_table_query)

        # Створення таблиці "orders"
        create_orders_table_query = '''CREATE TABLE IF NOT EXISTS orders (
                                      order_id SERIAL PRIMARY KEY,
                                      customer_name TEXT NOT NULL,
                                      item_id INTEGER NOT NULL,
                                      quantity INTEGER NOT NULL,
                                      FOREIGN KEY (item_id) REFERENCES menu (item_id)
                                      )'''
        cursor.execute(create_orders_table_query)

        # Вставка начальных данных в таблицу "menu"
        initial_menu_items = [
            ('Pizza', 'Delicious pizza with various toppings', 10.99),
            ('Burger', 'Juicy beef burger with cheese and fries', 8.99),
            ('Salad', 'Fresh garden salad with dressing', 6.99)
        ]
        insert_menu_items_query = '''INSERT INTO menu (item_name, description, price) VALUES (%s, %s, %s)'''
        cursor.executemany(insert_menu_items_query, initial_menu_items)

        # Фиксация изменений и закрытие соединения с базой данных
        connection.commit()
        print("База данных успешно создана.")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL:", error)

    finally:
        # Закрытие соединения с базой данных
        if connection:
            cursor.close()
            connection.close()
