import re

string = ["a", "ab", "abb", "bb", "aaa"]

proverka = r'a+b*'

for x in string:
    if re.fullmatch(proverka, x):
        print(f"{x} соответсвует")
    else:
        print(f"{x} несоотвествует")