def errorMessage(message):
    return f"\033[31m {message}"


class FalseSyntaxe(Exception):

    def __init__(self, data, line, position):
        self.data = str(data)
        self.line = line
        self.position = position

    def __str__(self):
        text = f"Неизвестный символ в {self.line} строке, на " \
               f"{self.position} позиции: {self.data}"
        return errorMessage(text)


class FalseKod(Exception):

    def __init__(self, data, line):
        self.data = str(data)
        self.line = line

    def __str__(self):
        text = f"Неизвестная конструкция в {self.line} строке"
        return errorMessage(text)


class NotSymbol(Exception):

    def __init__(self, data, line):
        self.data = data
        self.line = line

    def __str__(self):
        text = f'Не хватает символа "{self.data}" в {self.line} строке'
        return errorMessage(text)


class NotSemicolon(NotSymbol):

    def __init__(self, line):
        data = ";"
        super().__init__(data, line)


class NotBracket(NotSymbol):

    def __init__(self, data, line):
        super().__init__(data, line)


class NotFigureBracket(NotSymbol):

    def __init__(self, data, line):
        super().__init__(data, line)


class IntInStartLine(Exception):

    def __init__(self, data, line):
        self.data = data
        self.line = line

    def __str__(self):
        text = f"Не корректное значение в начале {self.line} строки: {self.data}"
        return errorMessage(text)