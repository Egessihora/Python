# Шаблон декоратора

def func_decorator(func):
    print("---  some actions ---") # будет выведен один раз в момент декорирования функции
    def wraper(*args, **kwargs):
        print("---  some actions ---")  # будет выполняться перед каждым вызовом функции
        result = func(*args, **kwargs)
        print("---  some actions ---") # будет выполняться после каждого вызова функции
        return result
    return wraper
