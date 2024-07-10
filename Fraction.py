def prime_number(num):
    '''Проверка на простое число. Ввод -- int, вывод -- bool.'''
    k = 0 #counter
    for i in range(2, int(num**0.5+1)):        
        if num % i == 0:
            # print(num % i)
            k += 1
    if k > 0:
        return False
    else:
        return True

class Fraction(object):
    def __init__(self, numerator=None, denominator=None):
        "Числитель и знаменатель, тип данных -- int"
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):        
        return str(self.whole_part()) + " " + str(self.numerator) + "/" + str(self.denominator) if self.whole_part() > 0 else str(self.numerator) + "/" + str(self.denominator)
    def whole_part(self):
        "Нахождение целой части. Ввод: экземпляр Fraction(). Вывод: int"
        return self.numerator // self.denominator if self.numerator >= self.denominator else 0
    def fraction_reduction(self):        
        "Функция по нахождению сокращеной дроби и отделению целой её части."
        if self.numerator >= self.denominator:
            new_whole_part = self.whole_part()
            self.numerator -= new_whole_part * self.denominator
            self = Fraction(self.numerator, self.denominator)
        for item in reversed(range(1, round(self.denominator/2))):
            if self.numerator % item == 0 and self.denominator % item == 0 and item != 1:
                if prime_number(item):
                    while self.numerator % item == 0 and self.denominator % item == 0:
                        self.numerator = self.numerator//item
                        self.denominator = self.denominator//item
        return Fraction(self.numerator, self.denominator)
    def improper_fraction_reduction(self):
        new_whole_part = self.whole_part()
        self.fraction_reduction()
        return Fraction(self.numerator + self.denominator * new_whole_part, self.denominator)

    def __add__(self, other):
        "Сложение между экземплярами Fraction() или между экземплярами Fraction() и int или float"
        if type(other and self) is Fraction:
            pass
        elif type(other) is int:
            other = Fraction(other, 1)
        elif type(other) is float:
            pass
        try:
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            #нахождение неприведенного числителя
            new_denominator = self.denominator * other.denominator
            #нахождение неприведенного знаменателя
            return Fraction(new_numerator, new_denominator).fraction_reduction()
        except TypeError as tp:
            print(tp)
    def __sub__(self, other):
        "Вычитание между экземплярами Fraction() или между экземплярами Fraction() и int или float"
        other = Fraction(other, 1) if type(other) is int or float else other
        self = Fraction(self, 1) if type(self) is int or float else self
        new_numerator = self.numerator * other.denominator - other.numenator * self.denominator
        #Неприведенный числитель
        new_denominator = self.denominator * other.denominator
        #Неприведенный знаменатель
        return Fraction(new_numerator, new_denominator).fraction_reduction()

        
if __name__ == "__main__":       
    var1 = Fraction(5, 24)
    var2 = Fraction(3, 4)
    var3 = Fraction(75, 255)
    var4 = Fraction(60, 510)
    var5 = Fraction(500, 50)
    # var3.fraction_reduction()
    print(var3 + 7)
    # print(var5.improper_fraction_reduction())