def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i]==nums[i+1]:
            return True
    return False
inp = input("Введите числа: ")
nums = inp.split()
if has_33(nums)==True:
    print("True")
else:
    print("False")