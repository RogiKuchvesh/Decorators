# Применить написанный логгер к приложению из любого предыдущего д/з.

from decorators2 import logger

path = 'logger_from_import.log'

@logger(path)
def flat_generator(list_of_lists):
    cursor = 0
    while cursor < len(list_of_lists):
        list_ = list_of_lists[cursor]
        for element in list_:
            yield element
        cursor += 1  

if __name__ == '__main__':
    list_of_lists = [
         ['a', 'b', 'c'],
         ['d', 'e', 'f', 'h', False],
         [1, 2, None]
         ]

    print(list(flat_generator(list_of_lists)))
       