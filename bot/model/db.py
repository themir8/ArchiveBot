import psycopg2

class DataBase:

    def __init__(self):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = psycopg2.connect(dbname='archivebot', user='mirzohidov', 
                        password='coder', host='localhost', port=6432)
        self.cursor = self.connection.cursor()

    # def get_subscriptions(self, status = True):
    #     """Получаем всех активных подписчиков бота"""
    #     with self.connection:
    #         self.cursor.execute("SELECT * FROM users WHERE status = %s", (status,))
    #         return self.cursor.fetchall()

    # def book_exists(self, file_name):
    #     """Проверяем, есть ли уже юзер в базе"""
    #     with self.connection:
    #         self.cursor.execute('SELECT * FROM books WHERE file_name = %s', (file_name,))
    #         result = self.cursor.fetchall()
    #         return bool(len(result))


    # def add_subscriber(self, user_id, username, status = True):
    #     """Добавляем нового подписчика"""
    #     with self.connection:
    #         return self.cursor.execute("INSERT INTO users (user_id, username, status) VALUES(%s, %s, %s)", (user_id, username, status))

    # def update_subscription(self, user_id, status):
    #     """Обновляем статус подписки пользователя"""
    #     with self.connection:
    #         return self.cursor.execute("UPDATE users SET status = %s WHERE user_id = %s", (status, user_id))

    # def get_all_from_users(self):
    #     with self.connection:
    #         self.cursor.execute("SELECT * FROM users;")
    #         return self.cursor.fetchall()

    # def add_book(self, file_name, file_id, author):
    #     from datetime import datetime
    #     date = datetime.now()
    #     with self.connection:
    #         return self.cursor.execute("INSERT INTO books (file_name, file_name, author, date) VALUES (%s, %s, %s, %s)", (file_name, file_name, author, date))



    def get_book(self, file_name: str):
        with self.connection:
            self.cursor.execute("SELECT * FROM books WHERE file_name = %s", (file_name,))
            return self.cursor.fetchall()

    def get_music(self, file_name: str):
        with self.connection:
            self.cursor.execute("SELECT * FROM musics WHERE file_name = %s", (file_name,))
            return self.cursor.fetchall()

    def add_book(self, file_name: str, file_id: str):
        with self.connection:
            return self.cursor.execute("INSERT INTO books (file_name, file_id) VALUES (%s, %s)", (file_name, file_id))
    
    def get_all_books(self):
        with self.connection:
            self.cursor.execute("SELECT * FROM books;")
            return self.cursor.fetchall()

    def add_music(self, file_name: str, file_id: str):
        with self.connection:
            return self.cursor.execute("INSERT INTO musics (file_name, file_id) VALUES (%s, %s)", (file_name, file_id))
    
    def get_all_musics(self):
        with self.connection:
            self.cursor.execute("SELECT * FROM musics;")
            return self.cursor.fetchall()

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
        self.cursor.close()

# db = DataBase()

# book = db.get_book("Practical Data Science with Python 3.epub")
# print(book[0][2])
# button = db.get_all_books()
# print(button)