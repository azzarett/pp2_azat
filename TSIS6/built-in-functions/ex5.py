mytuple = (0, True, False, True)

a = all(mytuple)


if a:
    print(f"Все элементы {mytuple} трушны")
else:
    print(f"Не все в {mytuple} трушны")