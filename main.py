import os

def create_file():
    print('what name do you want to give the plan \n')
    file_name = input()

    try:
        new_file = open("D:/files_for_python/" + file_name +".txt", "x")
        print('enter how much itens in your plan \n')
        hm_itm = int(input())
        for x in range(hm_itm):
            print('enter ' + str(x + 1) + ' item \n')
            what_to_write = input()
            new_file.write(what_to_write + '\n')
        print('plan ' + file_name + ' was created')

    except:
        print('you entered existed name for plan')

def load_file():
    print('write your plan name')
    file_name = input()
    try:
        file = open("D:/files_for_python/" + file_name + ".txt", "r")
        print(file.read())
    except:
        print('you entered an invalid plan name')

def delete_file():
    print('enter file name what you want to remove \n')
    file_name = input()
    os.remove("D:/files_for_python/" + file_name + ".txt")
    print('plan ' + file_name + ' was removed')


print('hi, click "c" if you want to create new plan, click "s" if you want to see existed or "r" if you want to remove plan \n ')

first_check = input()

match first_check:
    case 'c':
         create_file()
    case 's':
        load_file()
    case 'r':
        delete_file()


