import sqlite3
from tabulate import tabulate


def con():
    return sqlite3.connect('omborxona.db')


def create_table_omborxona():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists omborxona(
        id integer primary key autoincrement,
        name varchar(50),
        price integer,
        number integer
        )
    """)
    conn.commit()
    conn.close()


def check_omborxona():
    conn = con()
    cur = conn.cursor()
    query = """
        select * from omborxona
    """
    cur.execute(query)
    data = cur.fetchall()
    print(tabulate(data, headers='keys', tablefmt='fancy_grid'))
    print()
    conn.commit()
    conn.close()


def add_product():
    name = input("Mahsulotni ismi: ")
    price = int(input("Mahsulotni narxi: "))
    numbers = int(input("Mahsulot nechta: "))
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        insert into omborxona(name, price, number)
        values (?, ?, ?)
    """, (name, price, numbers))
    print("Mahsulot saqlandi ")
    print()
    conn.commit()
    conn.cursor()


def buy_product():
    conn = con()
    cur = conn.cursor()
    query = """
            select * from omborxona
        """
    cur.execute(query)
    data = cur.fetchall()
    print(tabulate(data, headers='keys', tablefmt='fancy_grid'))
    answer = int(input("Sotib olmoxchi bolgan mahsulotingizni raqamini kiriting: "))
    n = int(input("Nechta sotib olmoxchi ekanligingizni kiriting: "))
    print()
    data2 = []
    data3 = []
    for i in data:
        data2.append(i[0])
        data3.append(i[3])
    d = False
    for i in data2:
        if answer != 0 and answer == i:
            d = True
    for i in data3:
        if n <= i:
            d = True

    if d:
        cur.execute("""
            update omborxona
            set number=number-?
            where id=?
        """, (n, answer))
        print("Sotildi")
        conn.commit()
        conn.close()
    else:
        print("Xato raqam kiritdingiz yoki buncha mahsulot mavjud emas! ")
