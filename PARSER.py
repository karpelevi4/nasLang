from LEXER import LEXER
from SINT_TREE import AssignNode, OperationNode, WhileNode, IfNode, LinkedListNode, PrintNode, LinkedListOperatioinNode
import ERR


class PARSER:

    def __init__(self, kod):
        self.kod = kod
        self.node_list = list()

    def parse(self):
        # for line in self.kod:
        for ii in range(len(self.kod)):
            line = self.kod[ii]

            if line[-1].getTypeToken() != "SEMICOLON":
                raise ERR.NotSemicolon(ii + 1)

            if line[0].getTypeToken() == "VAR" and line[1].getTypeToken() == "ASSIGNMENT":
                self.node_list.append(self.setAssign(line))
            elif line[0].getTypeToken() == "PRINT_TRIGGER":
                self.node_list.append(self.setPrint(line))
            elif line[0].getTypeToken() == "IF_TRIGGER":
                self.node_list.append(self.setIf(line))
            elif line[0].getTypeToken() == "WHILE_TRIGGER":
                self.node_list.append(self.setWhile(line))
            elif line[0].getTypeToken() == "LINKED_LIST_TRIGGER":
                self.node_list.append(self.setLinkedList(line))
            elif line[1].getTypeToken() == "LL_INSERT_END":
                self.node_list.append(self.setLLInsertAtEnd(line))

            elif line[1].getTypeToken() == "LL_INSERT_HEAD":

                self.node_list.append(self.setLLInsertAtHead(line))
            elif line[1].getTypeToken() == "LL_DELETE":

                self.node_list.append(self.setLLDelete(line))
            elif line[1].getTypeToken() == "LL_DELETE_HEAD":

                self.node_list.append(self.setLLDeleteAtHead(line))
            elif line[1].getTypeToken() == "LL_SEARCH":

                self.node_list.append(self.setLLSearch(line))
            elif line[1].getTypeToken() == "LL_IS_EMPTY":

                self.node_list.append(self.setLLIsEmpty(line))
            else:
                raise ERR.FalseKod(line[1].getValue(), ii + 1)
        return self.node_list

    def setAssign(self, line):
        name_variable = line[0].getValue()
        value = line[2:len(line)-1]
        if len(value) == 1:
            type_token = value[0].getTypeToken()
            if type_token == "INT":
                return AssignNode("Assign", name_variable, value, type_token)
            if type_token == "VAR":
                return AssignNode("Assign", name_variable, value, type_token)
        else:
            if len(value) == 3:
                return AssignNode("Assign", name_variable, self.setOperation(value), "Operation")
            else:
                return AssignNode("Assign", name_variable, self.setOperation(value), "OperationHard")

    def setPrint(self, line):
        value = line[2:len(line)-2]
        if len(value) == 1:
            type_value = value[0].getTypeToken()
            if type_value == "INT":
                return PrintNode("Print", int(value), type_value)
                # self.node_list.append(PrintNode("Print", value, type_value))
            elif type_value == "VAR":
                return PrintNode("Print", value, type_value)
                # self.node_list.append(PrintNode("Print", value, type_value))
            else:
                pass
        else:
            pass

    def setIf(self, line):
        flag = 1
        condition = list()
        loop = list()
        line_kod = list()
        for elem in line:
            if flag == 1 and elem.getValue() == "(":
                flag = 2
            elif flag == 2:
                if elem.getValue() == ")":
                    flag = 3
                    continue
                condition.append(elem)
            elif flag == 3 and elem.getValue() == "{":
                flag = 4
            elif flag == 4:
                if elem.getValue() == "}":
                    flag = 5
                    continue
                    #############################################
                line_kod.append(elem)
                if elem.getValue() == ";":
                    loop.append(line_kod)
                    line_kod = list()
        ready_loop = list()
        for line in loop:
            if line[0].getTypeToken() == "VAR" and line[1].getTypeToken() == "ASSIGNMENT":
                ready_loop.append(self.setAssign(line))
            elif line[0].getTypeToken() == "PRINT_TRIGGER":
                ready_loop.append(self.setPrint(line))
            else:
                print("ERROR")

        # print([elem.getValue() for elem in condition])
        # print(ready_loop[0].getValue()[0].getValue())
        return IfNode("If", condition, ready_loop)

    def setWhile(self, line):
        flag = 1
        condition = list()
        loop = list()
        line_kod = list()
        for elem in line:
            if flag == 1 and elem.getValue() == "(":
                flag = 2
            elif flag == 2:
                if elem.getValue() == ")":
                    flag = 3
                    continue
                condition.append(elem)
            elif flag == 3 and elem.getValue() == "{":
                flag = 4
            elif flag == 4:
                if elem.getValue() == "}":
                    flag = 5
                    continue

                line_kod.append(elem)
                if elem.getValue() == ";":
                    loop.append(line_kod)
                    line_kod = list()
        ready_loop = list()
        # print([elem.getValue() for elem in loop[0]])
        for line in loop:
            if line[0].getTypeToken() == "VAR" and line[1].getTypeToken() == "ASSIGNMENT":
                ready_loop.append(self.setAssign(line))
            elif line[0].getTypeToken() == "PRINT_TRIGGER":
                ready_loop.append(self.setPrint(line))
            else:
                print("ERROR")

        # print([elem.getValue() for elem in condition])
        # print(ready_loop[1])
        return WhileNode("While", condition, ready_loop)

    def setOperation(self, value):
        if len(value) == 3:
            left_operand = value[0]
            sign = value[1]
            right_operand = value[2]
            return OperationNode("Operation", left_operand, right_operand, sign, final=True)
        else:
            condition = [elem.getValue() for elem in value]
            return OperationNode("Operation", value, None, None, final=False)

    def setLinkedList(self, line):
        name_linked_list = line[1].getValue()
        values = line[4:len(line)-2]
        new_values = list()
        for elem in values:
            if elem.getTypeToken() != "VIRGULE":
                new_values.append(elem)
        return LinkedListNode("LinkedList", name_linked_list, new_values)

    def setLLInsertAtEnd(self, line):
        name_variable = line[0].getValue()
        value = line[3]
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLInsertAtEnd", name_variable, value)

    def setLLInsertAtHead(self, line):
        name_variable = line[0].getValue()
        value = line[3]
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLInsertAtHead", name_variable, value)

    def setLLDelete(self, line):
        name_variable = line[0].getValue()
        value = line[3]
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLDelete", name_variable, value)

    def setLLDeleteAtHead(self, line):
        name_variable = line[0].getValue()
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLDeleteAtHead", name_variable, None)

    def setLLSearch(self, line):
        name_variable = line[0].getValue()
        value = line[3]
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLSearch", name_variable, value)

    def setLLIsEmpty(self, line):
        name_variable = line[0].getValue()
        return LinkedListOperatioinNode("LinkedListOperationNode", "setLLIsEmpty", name_variable, None)

    def getNodeList(self):
        return self.node_list