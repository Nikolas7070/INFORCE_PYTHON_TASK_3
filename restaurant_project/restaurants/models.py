class EmployeeService:
    def __init__(self, db):
        self.db = db

    def add_employee(self, name, position):
        try:
            insert_employee_query = '''INSERT INTO employees (name, position) VALUES (%s, %s)'''
            self.db.cursor.execute(insert_employee_query, (name, position))
            self.db.connection.commit()
            print("Співробітник успішно доданий.")
        except Error as error:
            print("Помилка при додаванні співробітника:", error)


class VoteService:
    def __init__(self, db):
        self.db = db

    def add_vote(self, user_id, menu_item_id):
        try:
            insert_vote_query = '''INSERT INTO votes (user_id, menu_item_id) VALUES (%s, %s)'''
            self.db.cursor.execute(insert_vote_query, (user_id, menu_item_id))
            self.db.connection.commit()
            print("Голос успішно доданий.")
        except Error as error:
            print("Помилка при додаванні голосу:", error)
