def create_cookie(name, code):
    with open(name + ".data", 'w+') as name:
        name.write(code)

def change_cookie(name, new_line):
    with open(name + ".data", 'a+') as ch:
        ch.write(new_line)

def delete_cookie(name):
    import os
    os.remove(name + ".data")