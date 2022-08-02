class Number:
    def __init__(self, string: str, pos_neg: bool = False):
        self.negative = pos_neg
        self.number = string


class Binary_Exception(Exception):
    pass


class Hexadecimal_Exception(Exception):
    pass


class Decimal_Exception(Exception):
    pass


class Binary(Number):
    def __init__(self, string: str, pos_neg: bool = False):
        for i in string:
            if i not in ['0', '1']:
                raise Binary_Exception("Binary Numbers include only \"0\" and \"1\"")
        while string[0] == "0" and len(string) > 1:
            string = string[1:]
        super().__init__(string, pos_neg)

    def __add__(self, other):
        if type(other) != Binary:
            raise Binary_Exception("Binary Numbers can only be added to other binary numbers")
        else:
            add_string = ""
            s1, s2, carry = self.number[::-1], other.number[::-1], '0'
            if len(s1) > len(s2):
                for _ in range(len(s1) - len(s2)):
                    s2 += "0"
            elif len(s2) > len(s1):
                for _ in range(len(s2) - len(s1)):
                    s1 += "0"
            for i in range(len(s1)):
                if s1[i] == "0":
                    if s2[i] == "0":
                        add_string += carry
                        carry = "0"
                    else:
                        if carry == "0":
                            add_string += "1"
                        else:
                            add_string += "0"
                            carry = "1"
                else:
                    if s2[i] == "0":
                        if carry == "0":
                            add_string += "1"
                        else:
                            add_string += "0"
                    else:
                        if carry == "0":
                            add_string += "0"
                            carry = "1"
                        else:
                            add_string += "1"
            if carry == "1":
                add_string += "1"
            return Binary(add_string[::-1])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if type(other) != Binary:
            raise Binary_Exception("Binary Numbers can only be subtracted from other binary numbers")
        return self + Binary(other.number, not other.negative)

    def __gt__(self, other):
        if type(other) != Binary:
            raise Binary_Exception("Binary Numbers can only be compared to other binary numbers")
        if self.number == "0" and other.number == "0":
            return False
        if self.negative and not other.negative:
            return False
        elif not self.negative and other.negative:
            return True
        s1, s2 = self.number, other.number
        if len(s1) > len(s2):
            return True if not self.negative else False
        elif len(s1) < len(s2):
            return False if not self.negative else True
        else:
            while True:
                if s1[0] == s2[0]:
                    s1, s2 = s1[1:], s2[1:]
                    if s1 == "" and s2 == "":
                        return False
                elif s1[0] == "1":
                    return True if not self.negative else False
                else:
                    return False if not self.negative else True

    def __eq__(self, other):
        if type(other) != Binary:
            return False
        if self.number == "0" and other.number == "0":
            return True
        return self.number == other.number and self.negative == other.negative

    def __ge__(self, other):
        if type(other) != Binary:
            raise Binary_Exception("Binary Numbers can only be compared to other binary numbers")
        return self > other or self == other

    def __str__(self):
        return self.number if not self.negative else '-' + self.number

    def __int__(self):
        s1, return_num = self.number[::-1], 0
        for i in range(len(s1)):
            return_num += (2 ** i) * int(s1[i])
        return -1 * return_num if self.negative else return_num

    def __rsub__(self, other):
        if type(other) != Binary:
            raise Binary_Exception("Binary Numbers can only be subtracted from other binary numbers")
        return Binary(self.number, self.negative) + other

    def __mul__(self, other):
        if type(other) != Binary:
            raise Binary_Exception("Binary Numbers can only be multiplied to other binary numbers")
        a, b = int(self), int(other)
        c = a * b
        return Binary.int_to_num(c)

    def __floordiv__(self, other):
        if type(other) != Binary:
            raise Binary_Exception("Binary Numbers can only be divided from other binary numbers")
        a, b = int(self), int(other)
        if a // b == int(a / b):
            return Binary.int_to_num(a // b)
        else:
            raise Binary_Exception("Could not divide Binary numbers")

    def __truediv__(self, other):
        return self // other

    @staticmethod
    def int_to_num(num: int):
        negative = True if num < 0 else False
        if num < 0:
            num = num * -1
        return_str = ""
        while True:
            return_str += str(num % 2)
            num = num // 2
            if num == 0:
                break
        return Binary(return_str[::-1], negative)


class Hexadecimal(Number):
    def __init__(self, string: str, negative: bool = False):
        for i in string:
            if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]:
                raise Hexadecimal_Exception("Invalid Character added to Hexadecimal Number ")
        super().__init__(string, negative)

    def __int__(self):
        s1, number = self.number[::-1], 0
        for i in range(len(s1)):
            number += (16 ** i) * Hexadecimal.ind_num(s1[i])
        return number if not self.negative else -1 * number

    @staticmethod
    def ind_num(car: str):
        if car not in ["A", "B", "C", "D", "E", "F"]:
            return int(car)
        elif car == "A":
            return 10
        elif car == "B":
            return 11
        elif car == "C":
            return 12
        elif car == "D":
            return 13
        elif car == "E":
            return 14
        elif car == "F":
            return 15

    @staticmethod
    def num_to_hex(num: int):
        d = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        neg = False if num > 0 else True
        if num < 0:
            num = num * -1
        return_str = ""
        while True:
            a = num % 16
            if a >= 10:
                return_str += d[a]
            else:
                return_str += str(a)
            num = num // 16
            if num == 0:
                break
        return Hexadecimal(return_str[::-1], neg)

    def __str__(self):
        return self.number if not self.negative else '-' + self.number

    def __eq__(self, other):
        if type(other) != Hexadecimal:
            return False
        return self.number == other.number and self.negative == other.negative

    def __gt__(self, other):
        if type(other) != Hexadecimal:
            raise Hexadecimal_Exception("Hexadecimal Numbers can only be compared to other Hexadecimal Numbers")
        return int(self) > int(other)

    def __ge__(self, other):
        return self > other or self == other

    def __add__(self, other):
        if type(other) != Hexadecimal:
            raise Hexadecimal_Exception("Hexadecimal Numbers can only be added to other Hexadecimal Numbers")
        return Hexadecimal.num_to_hex(int(self) + int(other))

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if type(other) != Hexadecimal:
            raise Hexadecimal_Exception("Hexadecimal Numbers can only be subtracted from other Hexadecimal Numbers")
        return Hexadecimal.num_to_hex(int(self) - int(other))

    def __mul__(self, other):
        if type(other) != Hexadecimal:
            raise Hexadecimal_Exception("Hexadecimal Numbers can only be multiplied to other Hexadecimal Numbers")
        return Hexadecimal.num_to_hex(int(self) * int(other))

    def __truediv__(self, other):
        return self // other

    def __floordiv__(self, other):
        if type(other) != Hexadecimal:
            raise Hexadecimal_Exception("Hexadecimal Numbers can only be divided from other Hexadecimal Numbers")
        a,b = int(self), int(other)
        if a//b == int(a/b):
            return Hexadecimal.num_to_hex(a//b)
        else:
            raise Hexadecimal_Exception("Could not divide Hexadecimal Numbers")


class Decimal(Number):
    def __init__(self, string: str, pos_neg: bool = False):
        if not string.isdigit():
            raise Decimal_Exception("Decimal Numbers can only include digits 0-9")
        super().__init__(string, pos_neg)

    def __int__(self):
        return -1 * int(self.number) if self.negative else int(self.number)

    def __str__(self):
        return '-'+ self.number if self.negative else self.number

    def __add__(self, other):
        if type(other) != Decimal:
            raise Decimal_Exception("Decimal Numbers can only be added to other Decimal Numbers")
        answer = int(self) + int(other)
        return Decimal.num_to_decimal(answer)

    def __sub__(self, other):
        if type(other) != Decimal:
            raise Decimal_Exception("Decimal Numbers can only be subtracted to other Decimal Numbers")
        answer = int(self) - int(other)
        return Decimal.num_to_decimal(answer)

    def __mul__(self, other):
        if type(other) != Decimal:
            raise Decimal_Exception("Decimal Numbers can only be multiplied to other Decimal Numbers")
        answer = int(self) * int(other)
        return Decimal.num_to_decimal(answer)

    def __truediv__(self, other):
        if type(other) != Decimal:
            raise Decimal_Exception("Decimal Numbers can only be divided to other Decimal Numbers")
        a,b = int(self), int(other)
        if a // b == int(a/b):
            return Decimal.num_to_decimal(a//b)
        else:
            raise Decimal_Exception("Calculator does not support decimals")

    def __floordiv__(self, other):
        return self / other

    def __pos__(self):
        self.negative = self.negative

    def __neg__(self):
        self.negative = not self.negative

    @staticmethod
    def num_to_decimal(i : int):
        negative = False if i > 0 else True
        string = str(abs(i))
        return Decimal(string, negative)
