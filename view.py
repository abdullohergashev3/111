from database import *

create_table_omborxona()


def menu():
    print("1.Omborxonadagi maxsulotlarni ko'rish")
    print("2.Mahsulot sotib olish")
    print("3.Mahsulot qo'shish")
    answer = int(input("Kiriting: "))
    print()
    if answer == 1:
        check_omborxona()
        menu()
    elif answer == 2:
        buy_product()
        menu()
    elif answer == 3:
        add_product()
        menu()
    else:
        print("Notog'ri raqam kirittingiz!")
        print()
        menu()


menu()
