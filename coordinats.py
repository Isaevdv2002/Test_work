import math

class Point:
    def __init__(self, x=0, y=0):
        """Инициализация координат точки"""
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        """Вычисление расстояния до другой точки"""
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def get_coordinates(self):
        """Возвращает координаты точки в виде кортежа (x, y)"""
        return self.x, self.y

    def set_coordinates(self, x, y):
        """Устанавливает новые координаты точки"""
        self.x = x
        self.y = y

# Получаем от пользователя координаты точек
x1 = float(input("Введите x-координату для первой точки: "))
y1 = float(input("Введите y-координату для первой точки: "))
x2 = float(input("Введите x-координату для второй точки: "))
y2 = float(input("Введите y-координату для второй точки: "))

# Создаем объекты класса Point
point1 = Point(x1, y1)
point2 = Point(x2, y2)

# Выводим информацию о точках и расстоянии между ними
print("Координаты точки 1:", point1.get_coordinates())
print("Координаты точки 2:", point2.get_coordinates())
print("Расстояние между точкой 1 и точкой 2:", point1.distance_to(point2))

# Запрашиваем новые координаты для первой точки
new_x1 = float(input("Введите новую x-координату для первой точки: "))
new_y1 = float(input("Введите новую y-координату для первой точки: "))
point1.set_coordinates(new_x1, new_y1)
print("Новые координаты точки 1:", point1.get_coordinates())
