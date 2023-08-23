from database2 import *
from utils2 import *


create_user_table()
create_products_table()


def menu():
    print("Online do'konimizga xush kelibsiz")
    print("1.Buyum sotib olish")
    print("2.Buyum qo'shish")
    answer = int(input("Kiriting: "))
    print()
    if answer == 1:
        is_exists()
        if is_exists:
            buy_product()
        menu()
    elif answer == 2:
        admin_menu()
        menu()
    else:
        print("Hato raqam kiritingiz")
        menu()


def admin_menu():
    print("Admin menu")
    print("1.Buyum qo'shish")
    print("2.Buyumni chiqarib yuborish")
    answer = int(input("Kiriting: "))
    print()
    if answer == 1:
        admin_add_product()
        admin_menu()
    elif answer == 2:
        admin_delete_product()
        admin_menu()
    else:
        print("Hato raqam kiritingiz")
        admin_manu()


menu()