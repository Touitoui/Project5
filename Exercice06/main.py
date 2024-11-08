def calculate_average(list_number):
    total = 0
    for number in list_number:
        total+= number
    return total / len(list_number)

if __name__ == '__main__':
    # Exemple d'utilisation de la fonction
    numbers = [10, 20, 30, 40, 50]
    average = calculate_average(numbers)
    print("La moyenne est :", average)
