import sqlite3
from tabulate import tabulate
from datetime import datetime


def conn():
    return sqlite3.connect('dbt2.db')


def create_user_table():
    con = conn()
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name varchar(30),
        last_name varchar(30),
        birth_day varchar(10),
        phone varchar(20),
        balance integer,
        username varchar(50),
        password varchar(150),
        is_admin boolean default false
    )''')
    con.commit()
    con.close()


def check_user(username: str, phone: str):
    con = conn()
    cur = con.cursor()
    cur.execute('''SELECT * FROM users WHERE username =? AND phone =?''', (username, phone))
    result = cur.fetchone()
    conn.commit()
    conn.close()
    return result


def is_exists():
    print("Buyum sotib olish uchum malumotlaringizni kiritishingiz kerek")
    first_name = input("Ism: ")
    last_name = input("Familya: ")
    birth_day = input("Tugilgan sanangiz: format[yyyy-mm-dd]: ")
    phone = input("Tel nomer: ")
    username = input("Username: ")
    password = input("Password: ")
    phone_data = check_phone(phone)
    brith = check_date(birth_day)
    if phone_data and brith:
        user_data = check_user(username, phone)
        if user_data:
            print("Malumotlar xato kiritildi!")
        else:
            data = dict(
                first_name=first_name,
                last_name=last_name,
                birth_day=birth_day,
                phone=phone,
                username=username,
                password=password,
                is_admin=True
            )
            write_user(data)
            print("Ma'lumot saqlandi!")
    else:
        print("Tugilgan sana yoki tel nomer xato !")


def write_user(data: dict):
    con = conn()
    cur = con.cursor()
    cur.execute('''INSERT INTO users (
        first_name,
        last_name,
        birth_day,
        phone,
        username,
        password,
        is_admin
    ) VALUES (?,?,?,?,?,?,?,?)''', (
        data['first_name'],
        data['last_name'],
        data['birth_day'],
        data['phone'],
        data['username'],
        data['password'],
        data['is_admin']
    ))
    con.commit()
    con.close()


def create_products_table():
    con = conn()
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name varchar(50),
        price integer,
        the_number integer
    )''')
    con.commit()
    con.close()


def buy_product():
    con.conn()
    cur = con.cursor()
    cur.execute('''SELECT * FROM products''')
    print("Sotib olmoxchi bolgan buyumingiz raqamini ")
    answer = int(input("Kiring: "))
    if answer == 1:
        print("Nechta sotib olmoxchisiz")
        answer2 = int(input("Kiriting: "))

        cur.execute('''INSERT INTO products (
            name,
            price,
            the_number
        ) VALUES (?,?,?)''', (
            name,
            price,
            the_number
        ))
        con.commit()
        con.close()


def admin_add_product():
    con = conn()
    cur = con.cursor()
    cur.execute('''SELECT * FROM products''')


    name = input("Ism: ")
    price = int(input("Narxi: "))
    the_number = int(input("Buyum soni: "))
    cur.execute('''INSERT INTO products (
        name,
        price,
        the_number
    ) VALUES (?,?,?)''', (
        name,
        price,
        the_number
    ))
    print("Mahsulot sotuvga qo'yildi!")
    print()
    con.commit()
    con.close()


def admin_delete_product():
    con = conn()
    cur = con.cursor()
    cur.execute('''SELECT * FROM products''')
    answer = int(input("Chiqarib yubormoxchi bolgan buyumingiz raqamini kiriting: "))
    if answer == 1:
        cur.execute('''
        delete from products where id=?''',(answer))
        con.commit()
        con.close()


