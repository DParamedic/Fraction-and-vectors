from functools import total_ordering


class Point(object):
    "Точка, имеющая три координаты. Объект неизменяем."
    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
    def coord_distance(self, other):
        "Вычисляет расстояние в координатах. Результат -- кортеж с информацией о разнице координат."
        dist_x = other.x - self.x
        dist_y = other.y - self.y
        dist_z = other.z - self.z
        return (dist_x, dist_y, dist_z)
    def __add__(self, dist_other=None):
        "Сложение производится между объектом Point() и кортежем, хранящим в себе информацию о смещении координат или между обЪектом Point() и целым числом n -- в этом случае все координаты сдвигаются на n."
        if type(dist_other) is tuple and len(dist_other) == 3:
            other = Point()
            other.x = self.x + dist_other[0]
            other.y = self.y + dist_other[1]
            other.z = self.z + dist_other[2]
        elif type(dist_other) is int:
            other.x = self.x + dist_other
            other.y = self.y + dist_other
            other.z = self.z + dist_other
        else:
            #реализовать механизм Exception
            pass
        return other
    def change_x(self, x_coord=None, y_coord=None, z_coord=None):
        "Позволяет заменить любую из координат или несколько. Указывать явно. НЕ ПРОВЕРЕННЫЙ МЕТОД."
        self.x = x_coord if x_coord is not None else self.x
        self.y = y_coord if y_coord is not None else self.y
        self.z = z_coord if z_coord is not None else self.z
        return self
    def distance(self, sec_object):
        "Вычисляет дистанцию между двумя точками в числовом представлении."
        return ((self.x - sec_object.x)**2 + (self.y - sec_object.y)**2 + (self.z - sec_object.z)**2)**0.5
    def square_triangle(self, B, C):
        "Вычисляет площадь треугольника, образуемого треми точками"
        first_sect = ((self.x - B.x)**2 + (self.y - B.y)**2 + (self.z - B.z)**2)**0.5
        sec_sect = ((self.x - C.x)**2 + (self.y - C.y)**2 + (self.z - C.z)**2)**0.5
        third_sect = ((B.x - C.x)**2 + (B.y - C.y)**2 + (B.z - C.z)**2)**0.5
        parametr = first_sect + sec_sect + third_sect
        return (parametr / 2 * (parametr / 2 - first_sect) * (parametr / 2 - sec_sect) * (parametr / 2 - third_sect)) ** 0.5
    

class Section(object):
    def __init__(self, point1=Point(), point2=Point()):
        self.point1 = point1
        self.point2 = point2
    def __add__(self, other):
        return self.point1.distance(self.point2) + other.point1.distance(other.point2)
    def __str__(self):
        return self.point1.distance(self.point2)
    def __sub__(self, other):
        return self.point1.distance(self.point2) - other.point1.distance(other.point2)
    
class Directional_section(Section):
    pass
    

@total_ordering
class Vector(object):
    def __init__(self, point1=Point(), point2=Point()):
        self.point1 = point1
        self.point2 = point2
    def __str__(self):
        return str(self.point1) + " - " + str(self.point2)
    def __add__(self, other):
        distance_1 = self.point2.coord_distance(other.point1)
        print(distance_1)
        return Vector(self.point1, other.point2 + distance_1)
    def long_vector(self):
        return self.point1.distance(self.point2)
    def __eq__(self, other):
        return self.long_vector() == other.long_vector()
    def __lt__(self, other):
        return self.long_vector() < other.long_vector()
    def __neg__(self):
        return Vector(self.point2, self.point1)
    def __sub__(self, other):
        other = -other
        return self.__add__(other=other)
        # distance_1 = self.point2.coord_distance(other.point2)
        # return Vector(self.point1, other.point1 + distance_1)
    def __mul__(self, other):
        if type(other) is int or float:
            distance_1 = tuple([item*other for item in self.point1.coord_distance(self.point2)])
            return Vector(self.point1, self.point1 + distance_1)
        else:
            pass
    def __truediv__(self, other):
        if type(other) is int or float:
            other = 1/other
            return self.__mul__(other=other)
                

# def decor_fract(func):
#     pass
# if __name__ == "__main__":
#     A = Point(-1, 4, 6)
#     B = Point(4, 7, 0)
#     C = Point(5, 7, 8)
#     D = Point(9, 8, -3)
#     E = Point(5, 34, -9)
#     F = Point(0, -9, -8)

#     AB = Vector(A, B)
#     CD = Vector(C, D)
#     EF = Vector(E, F)
#     AD = Vector(A, D)
#     vector_a = AB - CD
#     print(AB + EF)

   