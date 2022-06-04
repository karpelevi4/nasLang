import re

from TOKEN import TOKEN, DICT_TOKENS
import ERR


def checkBracket(tokens, line):
    flag = 0
    for elem in tokens:
        if elem.getTypeToken() == "BRACKET":
            flag += 1
        if elem.getTypeToken() == "BRACKET_BACK":
            flag -= 1
    if flag != 0:
        raise ERR.NotBracket(")", line)


def checkFigureBracket(tokens, line):
    flag = 0
    for elem in tokens:
        if elem.getTypeToken() == "FIGURE_BRACKET":
            flag += 1
        if elem.getTypeToken() == "FIGURE_BRACKET_BACK":
            flag -= 1
    if flag != 0:
        raise ERR.NotFigureBracket("}", line)


class LEXER:

    def __init__(self, kod):
        self.kod = kod
        self.lexemes_lines = list()

    def analise(self):
        for ii in range(len(self.kod)):

            lexemes = list()
            words = self.kod[ii].split()
            for jj in range(len(words)):
                lexemes.append(self.search_token(words[jj], ii + 1, jj + 1))
                if lexemes[0].getTypeToken() == "INT":
                    raise ERR.IntInStartLine(lexemes[0].getValue(), jj + 1)
            checkBracket(lexemes, ii + 1)
            checkFigureBracket(lexemes, ii + 1)
            self.lexemes_lines.append(lexemes)

    def search_token(self, word, num_line, num):

        for elem in DICT_TOKENS:
            result = re.search(DICT_TOKENS[elem], word)
            if result:
                return TOKEN(elem, word, num_line, num)
        raise ERR.FalseSyntaxe(word, num_line, num)

    def show(self):
        for ii in range(len(self.lexemes_lines)):
            # print(self.kod[ii])
            for elem in self.lexemes_lines[ii]:
                elem.toString()

    def get(self):
        return self.lexemes_lines