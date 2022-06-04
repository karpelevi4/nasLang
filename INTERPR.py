from LEXER import LEXER
from PARSER import PARSER


class INTERPR:

    def __init__(self, node_list):
        self.node_list = node_list
        self.variables_values = dict()
        self.linkedlist_values = dict()

    def execute(self):
        for node in self.node_list:
            node_type = node.getTypeNode()
            if node_type == "Print":
                self.executePrint(node)
            elif node_type == "If":
                self.executeIf(node)
            elif node_type == "While":
                self.executeWhile(node)
            elif node_type == "Assign":
                self.executeAssign(node)
            elif node_type == "LinkedList":
                self.executeLinkedList(node)
            elif node_type == "LinkedListOperationNode":
                self.executeLinkedListOperation(node)
            else:
                print("ERROR")

    def executeAssign(self, node):
        name_variable = node.getNameVariable()
        type_value = node.getTypeValue()


        if type_value == "INT":
            value = node.getValue()[0].getValue()
            self.variables_values[name_variable] = value
        elif type_value == "VAR":
            # print(value)
            value = node.getValue()[0].getValue()
            self.variables_values[name_variable] = self.variables_values[value]
        elif type_value == "Operation":
            value = self.executeOperation(node.getValue())
            self.variables_values[name_variable] = value
        elif type_value == "OperationHard":
            value = node.getValue()
            values = value.getLeftOperand()
            value = self.executeHardOperation(value)
            self.variables_values[name_variable] = value


    def executePrint(self, node):
        type_value = node.getTypeValue()
        if type_value == "INT":
            value = node.getValue()
            print(value[0].getValue())
        elif type_value == "VAR":
            name_variable = node.getValue()[0].getValue()
            if name_variable in self.variables_values:
                value = self.variables_values[name_variable]
                print(value)
            else:
                print("ERROR")
        elif type_value == "Operation":
            pass
        else:
            print("ERROR")

    def executeIf(self, node):
        condition = node.getCondition()
        loop = node.getLoop()
        value_one = condition[0]
        sign = condition[1]
        value_two = condition[2]

        if value_one.getTypeToken() == "VAR":
            value_one_condition = self.variables_values[value_one.getValue()]
        else:
            value_one_condition = value_one.getValue()

        if value_two.getTypeToken() == "VAR":
            value_two_condition = self.variables_values[value_two.getValue()]
        else:
            value_two_condition = value_two.getValue()

        value_sign = sign.getValue()
        type_sign = sign.getTypeToken()
        if type_sign == "SIGN_GREATER":
            if int(value_one_condition) > int(value_two_condition):
                for node_loop in loop:
                    node_type = node_loop.getTypeNode()
                    if node_type == "Print":
                        self.executePrint(node_loop)
                    elif node_type == "Assign":
                        self.executeAssign(node_loop)

        elif type_sign == "SIGN_LESS":
            if int(value_one_condition) < int(value_two_condition):
                for node_loop in loop:
                    node_type = node_loop.getTypeNode()
                    if node_type == "Print":
                        self.executePrint(node_loop)
                    elif node_type == "Assign":
                        self.executeAssign(node_loop)

        elif type_sign == "EQUALS":
            if int(value_one_condition) == int(value_two_condition):
                for node_loop in loop:
                    node_type = node_loop.getTypeNode()
                    if node_type == "Print":
                        self.executePrint(node_loop)
                    elif node_type == "Assign":
                        self.executeAssign(node_loop)

    def executeWhile(self, node):
        while True:
            condition = node.getCondition()
            loop = node.getLoop()
            value_one = condition[0]
            sign = condition[1]
            value_two = condition[2]

            if value_one.getTypeToken() == "VAR":
                value_one_condition = self.variables_values[value_one.getValue()]
            else:
                value_one_condition = value_one.getValue()

            if value_two.getTypeToken() == "VAR":
                value_two_condition = self.variables_values[value_two.getValue()]
            else:
                value_two_condition = value_two.getValue()
            type_sign = sign.getTypeToken()

            if type_sign == "SIGN_GREATER":
                if int(value_one_condition) > int(value_two_condition):
                    for node_loop in loop:
                        node_type = node_loop.getTypeNode()
                        if node_type == "Print":
                            self.executePrint(node_loop)
                        elif node_type == "Assign":
                            self.executeAssign(node_loop)
                else:
                    break
            elif type_sign == "SIGN_LESS":

                if int(value_one_condition) < int(value_two_condition):
                    for node_loop in loop:
                        node_type = node_loop.getTypeNode()
                        if node_type == "Print":
                            self.executePrint(node_loop)
                        elif node_type == "Assign":
                            self.executeAssign(node_loop)
                else:
                    break
            elif type_sign == "EQUALS":
                if int(value_one_condition) == int(value_two_condition):
                    for node_loop in loop:
                        node_type = node_loop.getTypeNode()
                        if node_type == "Print":
                            self.executePrint(node_loop)
                        elif node_type == "Assign":
                            self.executeAssign(node_loop)
                else:
                    break

    def executeOperation(self, node):
        left = node.getLeftOperand()
        right = node.getRightOperand()
        if left.getTypeToken() == "VAR":
            left_operand = self.variables_values[left.getValue()]
        else:
            left_operand = left.getValue()

        if right.getTypeToken() == "VAR":
            right_operand = self.variables_values[right.getValue()]
        else:
            right_operand = right.getValue()
        sign = node.getSign()
        final = node.getFinal()
        value = 0
        if final:
            if sign.getTypeToken() == "PLUS_SIGN":
                value = int(left_operand) + int(right_operand)
            if sign.getTypeToken() == "MINUS_SIGN":
                value = int(left_operand) - int(right_operand)
            if sign.getTypeToken() == "MULTIPLY_SIGN":
                value = int(left_operand) * int(right_operand)
            if sign.getTypeToken() == "DIVIDE_SIGN":
                value = int(left_operand) / int(right_operand)
        else:
            pass
        return int(value)

    def executeHardOperation(self, node):
        values = node.getLeftOperand()
        exp = [elem.getValue() for elem in values]
        value = node.function(exp)
        return value

    def executeLinkedList(self, node):
        name = node.getName()
        values = node.getValues()
        new_values = [elem.getValue() for elem in values]
        self.linkedlist_values[name] = new_values

    def executeLinkedListOperation(self, node):
        type_operation = node.getTypeOperation()

        if type_operation == "setLLInsertAtEnd":
            name_variable = node.getNameVariable()
            value = node.getValues()
            value_type = value.getTypeToken()
            value = value.getValue()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                values.append(value)
                self.linkedlist_values[name_variable] = values
            else:
                print("ERROR")

        elif type_operation == "setLLInsertAtHead":
            name_variable = node.getNameVariable()
            value = node.getValues()
            value_type = value.getTypeToken()
            value = value.getValue()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                values = [value] + values
                self.linkedlist_values[name_variable] = values
            else:
                print("ERROR")

        elif type_operation == "setLLDelete":
            name_variable = node.getNameVariable()
            value = node.getValues()
            value_type = value.getTypeToken()
            value = value.getValue()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                result = values.pop(int(value))
                self.linkedlist_values[name_variable] = values
                print(f"Element is deleted: {result}")
            else:
                print("ERROR")

        elif type_operation == "setLLDeleteAtHead":
            name_variable = node.getNameVariable()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                result = values.pop(0)
                self.linkedlist_values[name_variable] = values
                print(f"Element is deleted: {result}")
            else:
                print("ERROR")

        elif type_operation == "setLLSearch":
            name_variable = node.getNameVariable()
            value = node.getValues()
            value_type = value.getTypeToken()
            value = value.getValue()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                print(f"Element on position {value}: {values[int(value)]}")
            else:
                print("ERROR")

        elif type_operation == "setLLIsEmpty":
            name_variable = node.getNameVariable()
            if name_variable in self.linkedlist_values:
                values = self.linkedlist_values[name_variable]
                if len(values) == 0:
                    print("LinkedList is empty.")
                else:
                    print("LinkedList is NOT empty.")
            else:
                print("ERROR")

        else:
            pass