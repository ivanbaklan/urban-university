import os
import sqlite3

DB_FILE_NAME = "product_telegram.db"


def initiate_db():
    connection = sqlite3.connect(DB_FILE_NAME)
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
        );
        """
    )

    cursor.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_email ON Users (email);
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        price INTEGER
        );
        """
    )

    cursor.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_title ON Products (title);
        """
    )

    for i in range(1, 5):
        cursor.execute(
            "INSERT INTO Products (title, description, price) VALUES (?, ?, ?);",
            (f"Product {i}", f"описание {i}", f"{i * 100}"),
        )

    connection.commit()
    connection.close()


def add_user(username, email, age, balance=1000):
    if not os.path.exists(DB_FILE_NAME):
        initiate_db()
    connection = sqlite3.connect(DB_FILE_NAME)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?);",
        (f"{username}", f"{email}", f"{age}", f"{balance}"),
    )
    connection.commit()
    connection.close()


def is_included(username):
    if not os.path.exists(DB_FILE_NAME):
        initiate_db()
    connection = sqlite3.connect(DB_FILE_NAME)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM Users WHERE username = ?", (username,)
    )
    if cursor.fetchone():
        return True
    return False


def get_all_products():
    if not os.path.exists(DB_FILE_NAME):
        initiate_db()
    connection = sqlite3.connect(DB_FILE_NAME)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM Products;
        """
    )
    products = cursor.fetchall()
    connection.close()
    return products
