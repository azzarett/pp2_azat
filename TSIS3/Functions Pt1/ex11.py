def palindrome(s):
    for i in range(0, (int(len(s)/2))):
        if s[i]!=s[-(i+1)]:
            return False
    return True
if palindrome(input("Введите слово: ")):
    print("palindrome")
else:
    print("not palindrome")