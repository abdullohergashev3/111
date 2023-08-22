from database import *
from utils import *


create_table_user()
create_course_table()
student_course_table()


def admin_menu():
    print("Online kursimizga xush kelibsiz")
    print("\n 1.Kurs qo'shish")
    print("  2.O'quvchilarni ko'rish ")
    answer = int(input("Kiriting: "))
    if answer == 1:
        add_course()
        admin_menu()
    elif answer == 2:
        show_students()
        admin_menu()
    else:
        print("Qayta urining!")
        admin_menu()


def user_menu(username):
    print("Online kursimizga xush kelibsiz")
    print("\n 1.Kurslarni ko'rish")
    print(" 2.Kurslarga qo'shilish")
    print(" 3.Kurslaringizni ko'rish")
    answer = int(input("Kiriting: "))
    if answer == 1:
        show_courses()
        user_menu(username)
    elif answer == 2:
        join_course(username)
        user_menu(username)
    elif answer == 3:
        data = show_my_courses(username)
        if not data:
            print("Siz hali qo'shilmagansiz!")
            user_menu(username)
        user_menu(username)
    else:
        print("Qayta urining!")
        user_menu(username)


def menu():
    print("Online kursimizga xush kelibsiz")
    print("\n 1.Ro'yxatdan o'tish")
    print(" 2.Tizimga kirish")
    answer = int(input("Kiriting: "))
    if answer == 1:
        is_exists()
        menu()
    elif answer == 2:
        username = input("Username: ")
        password = input("password : ")
        login1 = login(username, password)
        if login1 == 1:
            admin_menu()
        elif login1 == 2:
            user_menu(username)


menu()