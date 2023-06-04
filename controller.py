import model, view

def main():
    view.greetings()
    print()
    view.print_menu()
    while True:
        mode = int(input())
        if mode == 1:
            model.show_data() # если записной книжки нет, добавить вывод: у вас нет записной книжки
        elif mode == 2:
            model.add_data()
        elif mode == 3:
            model.find_data()
        elif mode == 4:
            model.edit_data()
        elif mode == 5:
            model.del_data()
        elif mode == 0:
            view.goodbye()
            break
        else:
            view.error()
            continue        
        
    
