
class prime:
    def __init__(self, number):
        self.number = number

    def filter(self):
        if self.number == 1:
            return False
        for i in range(2, int(int(self.number**0.5)) + 1):
            if self.number % i == 0:
                return False
        return True
input_string = input()
my_list = input_string.split()
for i in range(len(my_list)):
    result = prime(int(my_list[i]))
    if result.filter():
        print(str(my_list[i]) + " ")