import sys, re, os

folder = input("Enter folder path: ")
regex = input("Enter regular expression: ")

pattern = re.compile(regex)

for filename in os.lisitdir(folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(folder, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                if pattern.search(line):
                    print(line, end="")