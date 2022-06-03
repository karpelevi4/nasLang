import ERR


class NODE:

    def __init__(self, type_node):
        self.type_node = type_node

    def getTypeNode(self):
        return self.type_node


class AssignNode(NODE):

    def __init__(self, type_node, name_variable, value, type_value):
        super().__init__(type_node)
        self.name_variable = name_variable
        self.value = value
        self.type_value = type_value

    def getNameVariable(self):
        return self.name_variable

    def getValue(self):
        return self.value

    def getTypeValue(self):
        return self.type_value


class OperationNode(NODE):

    def __init__(self, type_node, left_operand, right_operand, sign, final):
        super().__init__(type_node)
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.sign = sign
        self.final = final
        self.dict_main = {
                    "+": 1,
                    "-": 1,
                    "*": 2,
                    "/": 2,
                }

    def getLeftOperand(self):
        return self.left_operand

    def getRightOperand(self):
        return self.right_operand

    def getSign(self):
        return self.sign

    def getFinal(self):
        return self.final

    def operation(self, coord, exp):
        right = int(exp.pop(coord + 1))
        sign = exp.pop(coord)
        left = int(exp.pop(coord - 1))
        result = 0

        if sign == "+":
            result = left + right
        elif sign == "-":
            result = left - right
        elif sign == "*":
            result = left * right
        elif sign == "/":
            result = int(left / right)

        exp.insert(coord - 1, str(result))
        return exp

    def function(self, exp):
        exp = self.count(exp)
        flag = 2
        ii = 0
        while True:
            elem = exp[ii]
            if type(elem) != list:
                if elem in self.dict_main and self.dict_main[elem] == flag:
                    if type(exp[ii - 1]) == list:
                        exp[ii - 1] = self.function(exp[ii - 1])
                    if type(exp[ii + 1]) == list:
                        exp[ii + 1] = self.function(exp[ii + 1])
                    exp = self.operation(ii, exp)
                    ii = 0
                else:
                    ii += 1
            else:
                ii += 1
            if ii == len(exp):
                flag -= 1
                ii = 0

            if flag == 0:
                break
        return exp[0]

    def count(self, line):
        count_line = list()
        ii = 0
        while ii <= len(line):
            if line[ii] == "(":
                ind = len(line) - 1 - line[::-1].index(")")
                count_line.append(self.count(line[ii + 1:ind]))
                ii = ind + 1
            else:
                count_line.append(line[ii])
                ii += 1
            if ii == len(line):
                break
        return count_line

    def runOperationHard(self):
        values = self.left_operand
        new_values = [elem.getValue() for elem in values]
        return int(self.function(new_values)[0])


class WhileNode(NODE):

    def __init__(self, type_node, condition, loop):
        super().__init__(type_node)
        self.condition = condition
        self.loop = loop

    def getCondition(self):
        return self.condition

    def getLoop(self):
        return self.loop


class IfNode(NODE):

    def __init__(self, type_node, condition, loop):
        super().__init__(type_node)
        self.condition = condition
        self.loop = loop

    def getCondition(self):
        return self.condition

    def getLoop(self):
        return self.loop


class PrintNode(NODE):

    def __init__(self, type_node, value, type_value):
        super().__init__(type_node)
        self.value = value
        self.type_value = type_value

    def getValue(self):
        return self.value

    def getTypeValue(self):
        return self.type_value


class LinkedListNode(NODE):

    def __init__(self, type_node, name, values):
        super().__init__(type_node)
        self.name = name
        self.values = values

    def getName(self):
        return self.name

    def getValues(self):
        return self.values


class LinkedListOperatioinNode(NODE):

    def __init__(self, type_node, type_operation, name_variable, values):
        super().__init__(type_node)
        self.type_operation = type_operation
        self.name_variable = name_variable
        self.values = values

    def getTypeOperation(self):
        return self.type_operation

    def getNameVariable(self):
        return self.name_variable

    def getValues(self):
        return self.values