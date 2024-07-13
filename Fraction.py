def prime_number(num):
    """Проверка на простое число. Ввод -- int, вывод -- bool."""
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
        if self.whole_part() > 0:
            new_whole_part = self.whole_part()
            self = self.fraction_reduction()
            return str(new_whole_part) + " " + str(self.numerator) + "/" + str(self.denominator)
        else:
            return str(self.numerator) + "/" + str(self.denominator)
    def whole_part(self):
        "Нахождение целой части. Ввод: экземпляр Fraction(). Вывод: int"
        return self.numerator // self.denominator if self.numerator >= self.denominator else 0
    def fraction_reduction_improper(self):        
        "Функция по сокращению дроби. "
        for item in reversed(range(1, round(self.denominator/2))):
            if prime_number(item):
                if self.numerator % item == 0 and self.denominator % item == 0 and item != 1:
                    while self.numerator % item == 0 and self.denominator % item == 0:
                        self.numerator = self.numerator//item
                        self.denominator = self.denominator//item
        return Fraction(self.numerator, self.denominator)
    def fraction_reduction(self):
        self.fraction_reduction_improper()
        if self.numerator >= self.denominator:
            new_whole_part = self.whole_part()
            self.numerator -= new_whole_part * self.denominator
        return Fraction(self.numerator, self.denominator)

    def __add__(self, other):
        "Сложение между экземплярами Fraction() или между экземплярами Fraction() и int или float"
        if type(self) is Fraction and type(other) is Fraction:
            pass
        elif type(other) is int:
            other = Fraction(other, 1)
        elif type(other) is float:
            list_div_num = str(other).split(".")
            len_num = len(list_div_num[-1])
            new_dec_denominator = int("1" + len_num * "0")
            new_dec_numerator = int(list_div_num[0] + list_div_num[1])
            other = Fraction(new_dec_numerator, new_dec_denominator)
            print(other)
        try:
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            #нахождение неприведенного числителя
            new_denominator = self.denominator * other.denominator
            #нахождение неприведенного знаменателя
            return Fraction(new_numerator, new_denominator).fraction_reduction_improper()
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
        return Fraction(new_numerator, new_denominator).fraction_reduction_improper()

        
if __name__ == "__main__":       
    var1 = Fraction(1, 2)
    var2 = Fraction(1, 5)
    var3 = Fraction(75, 255)
    var4 = Fraction(60, 510)
    var5 = Fraction(501, 50)
    # var3.fraction_reduction()
    print(var1 + var2)
    # print(var5.improper_fraction_reduction())