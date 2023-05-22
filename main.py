import os

def create_file():
    qq =2
    print(qq)
def load_file():
    q=1
    print(q)

print('hi, click "c" if you want to create new plan, or click "s" if you want to see existed ')

first_check = input()

match first_check:
    case 'c':
         create_file()
    case 's':
        load_file()


