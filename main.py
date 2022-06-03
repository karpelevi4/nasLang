from LEXER import LEXER
from PARSER import PARSER
from INTERPR import INTERPR

code1 = ["a = ( 6 + 7 * ( 6 - 5 ) - 2 ) * 2 - 20 ; ",
         "PRINT ( a ) ;",
         "WHILE ( a < 10 ) { a = a + 3 ; PRINT ( a ) ; } ;",
         "b = 6 / a ;",
         "IF ( 40 > b ) { PRINT ( b ) ; } ;",
         "PRINT ( b ) ;",
         ]
code2 = ["LinkedList link_list = { 1 , 3 , 4 } ;",
         "link_list .insertAtEnd ( 2 ) ;",
         "link_list .insertAtHead ( 1 ) ;",
         "link_list .delete ( 2 ) ;",
         "link_list .deleteAtHead ( ) ;",
         "link_list .search ( 2 ) ;",
         "link_list .isEmpty ( ) ;"
        ]


def get_code():
    code = list()
    while True:
        line = input("Введите строку кода: ")
        if line:
            code.append(line)
        else:
            break
    print(f"Введено строк: {len(code)}\n")
    return code


def main():

    # ввод нового кода
    # code = get_code()  

    # поиск лексем
    lexer = LEXER(code1)  

    # показать строки кода
    # print(code)  

    # анализ лексем
    lexer.analise()  

    # получить список лексем
    lexemes = lexer.get()  

    # показать все лексемы
    # lexer.show()  

    # объекты для парсинга
    parser = PARSER(lexemes)  

    # начать парсинг
    parser.parse()  

    # получить список нодов
    node_list = parser.getNodeList()  

    # объекты для запуска
    inter = INTERPR(node_list)  

    # начать запуск
    inter.execute()  

    # показать все переменные
    # print(inter.linkedlist_values)  

    # показать все LL переменные
    # print(inter.variables_values)  


if __name__ == '__main__':
    main()