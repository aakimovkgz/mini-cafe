

from views import (create_cafe, update_cafe, get_cafe, wrong_command, show_menu, update_receipt_status,
                   create_employee, create_food, create_menu, get_current_user, create_order)
from config import (CAFE_ID, EMPLOYEE_ID, FOOD_ID, MENU_ID, ORDER_ID, RECEIPT_ID, SESSION_USER)


def main():
    while True:
        user = get_current_user(session_user=SESSION_USER)
        
        user_action = input(
                            "Enter 1 to show menu\n"
                            "Enter 2 to order\n"
                        )
        if user_action == '1':
            show_menu()
        elif user_action == '2':
            create_order(order_id=ORDER_ID, receipt_id=RECEIPT_ID, user=SESSION_USER)
        elif user_action == '11':
            action = input(
                            "Enter 1 if you want create employee\n"
                            "Enter 2 if you want update employee\n"
                            "Enter 3 get info employee\n"
                        )
            if action == '1':
                create_employee(emp_id=EMPLOYEE_ID)
            elif action == '2':
                pass
            elif action == '3':
                pass
            else:
                wrong_command()
        elif user_action == '22':
            action = input(
                            "Enter 1 if you want create food\n"
                            "Enter 2 if you want update food\n"
                            "Enter 3 get info food\n"
                        )
            if action == '1':
                create_food(food_id=FOOD_ID, user=user)
            elif action == '2':
                pass
            elif action == '3':
                pass
            else:
                wrong_command()
        elif user_action == '33':
            action = input(
                            "Enter 1 if you want create cafe\n"
                            "Enter 2 if you want update cafe\n"
                            "Enter 3 get info cafe\n "
                        )
            if action == '1':
                create_cafe(cafe_id=CAFE_ID)
            elif action == '2':
                update_cafe()
            elif action == '3':
                get_cafe()
            else:
                wrong_command()
        elif user_action == '44':
            action = input(
                            "Enter 1 if you want create menu\n"
                            "Enter 2 if you want update menu\n"
                            "Enter 3 get info menu\n"
                        )
            if action == '1':
                create_menu(menu_id=MENU_ID, user=user)
            elif action == '2':
                pass
            elif action == '3':
                pass
            else:
                wrong_command()
        elif user_action == '55':
            update_receipt_status()
        elif user_action == '66':
            break
        else:
            wrong_command()


if __name__ == '__main__':
    main()
