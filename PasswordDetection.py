import re
password = input("Input password: ")

def strong(sec):
    if len(sec) >= 8:
        re.compile(r'''(
            [a-zA-Z\d]           
    )''', re.VERBOSE)
        print("Strong")

    else:
        print("Weak")

strong(password)