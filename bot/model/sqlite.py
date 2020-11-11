import sqlite3

class DataBase:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def get_book(self, file_name: str):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `books` WHERE `file_name` = ?", (file_name,)).fetchall()

    def get_music(self, file_name: str):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `musics` WHERE `file_name` = ?", (file_name,)).fetchall()

    def add_book(self, file_name: str, file_id: str):
        with self.connection:
            return self.cursor.execute("INSERT INTO `books` (`file_name`, `file_id`) VALUES (?, ?)", (file_name, file_id))
    
    def get_all_books(self):
        with self.connection:
            self.cursor.execute("SELECT * FROM `books`;")
            return self.cursor.fetchall()

    def add_music(self, file_name: str, file_id: str):
        with self.connection:
            return self.cursor.execute("INSERT INTO `musics` (`file_name`, `file_id`) VALUES (?, ?)", (file_name, file_id))
    
    def get_all_musics(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `musics`;").fetchall()


    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()