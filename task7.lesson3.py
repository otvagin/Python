def int_func(arg):
    """
    Функция принимет слова из маленьких латинских букв 
    и возвращающую их же, но с прописной первой буквой.
    """
    print(type(arg))
    if type(arg) != str:
            
        print("Несоответствие типа данных!")
            
    return arg.capitalize()
print(int_func("i'd like to develop useful software."))
print(int_func("i'd like to develop useful software.").title())
