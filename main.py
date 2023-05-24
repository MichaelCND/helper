import os

def create_file():
    print('what name do you want to give the timetable \n')
    file_name = input()

    try:
        new_file = open("D:/files_for_python/" + file_name +".txt", "x")

    except:
        print('you entered existed name for timetable')

    print('enter how much itens in your plan \n')
    hm_itm = int(input())
    for x in range(hm_itm):
        print('enter ' + str(x + 1) + ' item \n')
        what_to_write = input()
        new_file.write(what_to_write + '\n')

def load_file():
    print('write your timetable name')
    file_name = input()
    try:
        file = open("D:/files_for_python/" + file_name + ".txt", "r")
        print(file.read())
    except:
        print('you entered an invalid timetable name')


print('hi, click "c" if you want to create new plan, or click "s" if you want to see existed \n ')

first_check = input()

match first_check:
    case 'c':
         create_file()
    case 's':
        load_file()


