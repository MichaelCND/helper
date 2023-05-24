import os

def create_file():
    print('what name do you want to give the timetable \n')
    file_name = input()
    print('enter how much itens in your plan \n')
    hm_itm = int(input())
    new_file = open("D:/files_for_python/" + file_name +".txt", "x")
    for x in range(hm_itm):
        print('enter '+ str(x+1) +' item \n')
        what_to_write = input()
        new_file.write(what_to_write + '\n')

def load_file():
 print('write your timetable name')

print('hi, click "c" if you want to create new plan, or click "s" if you want to see existed \n ')

first_check = input()

match first_check:
    case 'c':
         create_file()
    case 's':
        load_file()


