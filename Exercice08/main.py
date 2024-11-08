def log_decorator(func):
    def before_after():
        print("Avant")
        func()
        print("Apres")
    return before_after


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

if __name__ == '__main__':
    function_test()
