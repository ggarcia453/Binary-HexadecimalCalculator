from Numbers import *


class Solver_Exception(Exception):
    pass


def list_maker_decimal(l:list):
    list2, number, string = [], True, ""
    for i in l:
        if i.isdigit():
            string +=i
        elif i in ["+", "-", "*", "/"]:
            list2.append(string)
            string = ""
            list2.append(i)
        else:
            raise Solver_Exception("Invalid character in Calculator")
    if string != "":
        list2.append(string)
    return list2


def list_maker_hexadecimal(l : list):
    list2, number, string = [], True, ""
    for i in l:
        if i.isdigit():
            string += i
        elif i in ["A", "B", "C", "D", "E", "F"]:
            string += i
        elif i in ["+", "-", "*", "/"]:
            list2.append(string)
            string = ""
            list2.append(i)
        else:
            raise Solver_Exception("Invalid character in Calculator")
    if string != "":
        list2.append(string)
    return list2


def list_maker_binary(l:list):
    list2, number, string = [], True, ""
    for i in l:
        if i in ["0", "1"]:
            string += i
        elif i in ["+", "-", "*", "/"]:
            list2.append(string)
            string = ""
            list2.append(i)
        else:
            raise Solver_Exception("Invalid character in Calculator")
    if string != "":
        list2.append(string)
    return list2


class Solver:
    def __init__(self, mode: str):
        if mode in ["Binary", "Decimal", "Hexadecimal", "Conversion"]:
            self.mode = mode
        else:
            raise Solver_Exception("Invalid Mode")

    def solve(self, problem: str, orig: str = "", to: str = ""):
        if self.mode == "Conversion":
            if orig not in ["Binary", "Decimal", "Hexadecimal"]:
                raise Solver_Exception("Type not specified")
            if to not in ["Binary", "Decimal", "Hexadecimal"]:
                raise Solver_Exception("Type not specified")
            if orig == "Binary":
                answer = Binary(problem)
                if to == "Binary":
                    return answer.number
                elif to == "Hexadecimal":
                    return Hexadecimal.num_to_hex(int(answer)).number
                elif to == "Decimal":
                    return Decimal.num_to_decimal(int(answer)).number
            elif orig == "Hexadecimal":
                answer = Hexadecimal(problem)
                if to == "Binary":
                    return Binary.int_to_num(int(answer)).number
                elif to == "Hexadecimal":
                    return answer.number
                elif to == "Decimal":
                    return Decimal.num_to_decimal(int(answer)).number
            else:
                answer = Decimal(problem)
                if to == "Binary":
                    return Binary.int_to_num((int(answer))).number
                elif to == "Hexadecimal":
                    return Hexadecimal.num_to_hex(int(answer)).number
                elif to == "Decimal":
                    return answer.number
        elif self.mode == "Binary":
            list1 = [i for i in problem if i != " "]
            list2 = list_maker_binary(list1)
            list3 = []
            for i in list2:
                try:
                    list3.append(Binary(i))
                except Binary_Exception:
                    if i in ["+", "-", "*", "/"]:
                        list3.append(i)
                    else:
                        raise Solver_Exception("Invalid Character\nMake sure you use capital letters for Hexadecimal")
            while True:
                if "*" in list3 or "/" in list3:
                    mindex = len(list3) + 1 if "*" not in list3 else list3.index("*")
                    dindex = len(list3) + 1 if "/" not in list3 else list3.index("/")
                    if mindex < dindex:
                        try:
                            k1, k2 = list3[mindex - 1], list3[mindex + 1]
                            list3 = list3[:mindex - 1] + [k1 * k2] + list3[mindex + 2:]
                        except IndexError:
                            raise Solver_Exception("Could not Solve")
                    else:
                        try:
                            k1, k2 = list3[dindex - 1], list3[dindex + 1]
                            list3 = list3[:dindex - 1] + [k1 / k2] + list3[dindex + 2:]
                        except IndexError:
                            raise Solver_Exception("Could not solve")
                elif "+" in list3 or "-" in list3:
                    aindex = len(list3) + 1 if "+" not in list3 else list3.index("+")
                    sindex = len(list3) + 1 if "-" not in list3 else list3.index("-")
                    if aindex < sindex:
                        try:
                            k1, k2 = list3[aindex - 1], list3[aindex + 1]
                            list3 = list3[:aindex - 1] + [k1 + k2] + list3[aindex + 2:]
                        except IndexError:
                            raise Solver_Exception("Could not Solve")
                    else:
                        try:
                            k1, k2 = list3[sindex - 1], list3[sindex + 1]
                            list3 = list3[:sindex - 1] + [k1 - k2] + list3[sindex + 2:]
                        except IndexError:
                            raise Solver_Exception("Could not solve")
                else:
                    return list3[0].number
        elif self.mode == "Hexadecimal":
            list1 = [i for i in problem if i != " "]
            list2 = list_maker_hexadecimal(list1)
            list3 = []
            for i in list2:
                try:
                    list3.append(Hexadecimal(i))
                except Hexadecimal_Exception:
                    if i in ["+", "-", "*", "/"]:
                        list3.append(i)
                    else:
                        raise Solver_Exception("Invalid Character\nMake sure you use capital letters for Hexadecimal")
            while True:
                if "*" in list3 or "/" in list3:
                    mindex = len(list3) + 1 if "*" not in list3 else list3.index("*")
                    dindex = len(list3) + 1 if "/" not in list3 else list3.index("/")
                    if mindex < dindex:
                        try:
                            k1, k2 = list3[mindex - 1], list3[mindex + 1]
                            list3 = list3[:mindex - 1] + [k1 * k2] + list3[mindex + 2:]
                        except IndexError:
                            raise Solver_Exception("Could not Solve")
                    else:
                        try:
                            k1, k2 = list3[dindex - 1], list3[dindex + 1]
                            list3 = list3[:dindex - 1] + [k1 / k2] + list3[dindex + 2:]
                        except IndexError:
                            raise Solver_Exception("Could not solve")
                elif "+" in list3 or "-" in list3:
                    aindex = len(list3) + 1 if "+" not in list3 else list3.index("+")
                    sindex = len(list3) + 1 if "-" not in list3 else list3.index("-")
                    if aindex < sindex:
                        try:
                            k1, k2 = list3[aindex - 1], list3[aindex + 1]
                            list3 = list3[:aindex - 1] + [k1 + k2] + list3[aindex + 2:]
                        except IndexError:
                            raise Solver_Exception("Could not Solve")
                    else:
                        try:
                            k1, k2 = list3[sindex - 1], list3[sindex + 1]
                            list3 = list3[:sindex - 1] + [k1 - k2] + list3[sindex + 2:]
                        except IndexError:
                            raise Solver_Exception("Could not solve")
                else:
                    return list3[0].number
        elif self.mode == "Decimal":
            list1 = [i for i in problem if i != " "]
            list2 = list_maker_decimal(list1)
            list3 = [Decimal(i) if i.isdigit() else i for i in list2]
            while True:
                if "*" in list3 or "/" in list3:
                    mindex = len(list3) + 1 if "*" not in list3 else list3.index("*")
                    dindex = len(list3) + 1 if "/" not in list3 else list3.index("/")
                    if mindex < dindex:
                        try:
                            k1, k2 = list3[mindex - 1], list3[mindex + 1]
                            list3 = list3[:mindex - 1] + [k1 * k2] + list3[mindex + 2:]
                        except IndexError:
                            raise Solver_Exception("Could not Solve")
                    else:
                        try:
                            k1, k2 = list3[dindex - 1], list3[dindex + 1]
                            list3 = list3[:dindex - 1] + [k1 / k2] + list3[dindex + 2:]
                        except IndexError:
                            raise Solver_Exception("Could not solve")
                elif "+" in list3 or "-" in list3:
                    aindex = len(list3) + 1 if "+" not in list3 else list3.index("+")
                    sindex = len(list3) + 1 if "-" not in list3 else list3.index("-")
                    if aindex < sindex:
                        try:
                            k1, k2 = list3[aindex - 1], list3[aindex + 1]
                            list3 = list3[:aindex - 1] + [k1 + k2] + list3[aindex + 2:]
                        except IndexError:
                            raise Solver_Exception("Could not Solve")
                    else:
                        try:
                            k1, k2 = list3[sindex - 1], list3[sindex + 1]
                            list3 = list3[:sindex - 1] + [k1 - k2] + list3[sindex + 2:]
                        except IndexError:
                            raise Solver_Exception("Could not solve")
                else:
                    return list3[0].number
        else:
            return "ANSWER_P"
