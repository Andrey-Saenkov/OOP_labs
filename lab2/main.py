import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
      return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
      return str(self)

    def distance(self, other):
      return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)
class Vector:
    def __init__(self, *args):
        if len(args) == 3:
            self.x, self.y, self.z = args
        elif len(args) == 2:
            self.x = args[1].x - args[0].x
            self.y = args[1].y - args[0].y
            self.z = args[1].z - args[0].z
        else:
            raise ValueError("Неправильное количество аргументов")

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def normalize(self):
        length = self.length()
        return Vector(self.x / length, self.y / length, self.z / length)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        return Vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

    def mixed_product(self, other1, other2):
        return self.dot_product(other1.cross_product(other2))

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def are_collinear(self, other):
        return self.cross_product(other).length() == 0

    def are_coplanar(self, other1, other2):
        return self.mixed_product(other1, other2) == 0

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def angle(self, other):
        dot_product = self.dot_product(other)
        magnitude_product = self.length() * other.length()
        if magnitude_product == 0:
            raise ValueError("Невозможно вычислить угол для нулевого вектора")
        return math.acos(dot_product / magnitude_product)

def get_vector_input():
    x = float(input(f"Введите x-координату : "))
    y = float(input(f"Введите y-координату : "))
    z = float(input(f"Введите z-координату : "))
    return Vector(x, y, z)

def main():
    print("Программа для работы с векторами в трехмерном пространстве.")

    #point1 = Point(0, 0, 0)
    #point2 = Point(0, 0, 0)

    #print("Введите координаты первого вектора:")
    #vector1 = get_vector_input("первой точки")
    #print("Введите координаты второго вектора:")
    #vector2 = get_vector_input("второй точки")
    # Ввод координат для точки 1
  # Ввод координат для точки 1
    x1, y1, z1 = map(float, input("Введите координаты точки 1 (x y z): ").split())
    point1 = Point(x1, y1, z1)

    # Ввод координат для точки 2
    x2, y2, z2 = map(float, input("Введите координаты точки 2 (x y z): ").split())
    point2 = Point(x2, y2, z2)

    print("\nВведите координаты векторов:")
    vector1 = get_vector_input()
    vector2 = get_vector_input()

    operation = input("Выберите операцию (сумма/разность/длина/угол/...) или 'выход' для завершения программы: ")

    if operation == "сумма":
        result = vector1 + vector2
    elif operation == "разность":
        result = vector1 - vector2
    elif operation == "длина вектора":
        result = vector1.length()
    elif operation == "угол":
        #angle_vector = get_vector_input("второго вектора для вычисления угла")
        result = vector1.angle(vector2)
    elif operation == "получение обратного вектора":
        result = -vector1
    elif operation == "единичный вектор":
        result = vector1.normalize()
    elif operation == "Скалярное произведение векторов":
       result = vector1.dot_product(vector2)
    elif operation == "Векторное произведение векторов":
       result = vector1.cross_product(vector2)
    elif operation == "Смешанное произведение векторов":
       result = vector1.mixed_product(vector2, Vector(1, 1, 1))
    elif operation == "Коллинеарность векторов":
       result = vector1.are_collinear(vector2)
    elif operation == "Копланарность векторов":
       result = vector1.are_coplanar(vector2, Vector(2, 2, 2))
    elif operation == "Расстояние между точками":
       result = point1.distance(point2)

    else:
        result = "Некорректная операция"

    print(f"Результат операции: {result}")

if __name__ == "__main__":
    main()
