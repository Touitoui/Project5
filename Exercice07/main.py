def square(number):
    if not isinstance(number, (int, float)):
        print("Le paramètre doit être un nombre !")
        return None
    return number * number

if __name__ == '__main__':
    print(square(2))
    print(square(10))
    print(square("NaN"))
