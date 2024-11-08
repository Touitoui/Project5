class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length  # Aire = largeur * longueur

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)  #  = 2 * (largeur + longueur)

if __name__ == '__main__':
    # Test de la classe Rectangle
    rectangle = Rectangle(5, 3) # 5:width & 3:length
    print("Largeur:", rectangle.width)
    print("Longueur:", rectangle.length)
    print("Aire:", rectangle.calculate_area())
    print("Périmètre:", rectangle.calculate_perimeter())
