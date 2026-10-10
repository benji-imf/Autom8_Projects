def takes(list):
    for i in list[:-1]:
        print(i, end=", ")
    print("and " + list[-1])

spam = ['apples', 'bananas', 'tofu', 'cats']
takes(spam)