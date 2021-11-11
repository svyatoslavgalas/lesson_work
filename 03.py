# A. Начало и конец совпадают
# Функция принимает в качестве аргумента список строк.
# Необходимо вернуть количество строк,
# длина которых составляет 2 символа и более,
# а первый и последний символы этих строк совпадают.
# Примечание: в python нет оператора ++. Но += сработает.
def match_ends(words):
    pass


print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
print(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
print(match_ends(['aaa', 'be', 'abc', 'hello']), 1)


# B. Начинающиеся с X в начале
# Функция принимает в качестве аргумента список строк.
# Необходимо вернуть отсортированный список строк, в котором:
# сначала идет группа строк, начинающихся на 'x', затем все остальные.
# Наример: из ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] получится
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Подсказка: это можно сделать при помощи склеивания 2х заранее отсортированных списков
def front_x(words):
    pass


print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']), ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


# D. Удаление соседей
# Дан список чисел.
# Нужно вернуть список, где все соседние элементы
# были бы сведены к одному элементу.
# Таким образом, из [1, 2, 2, 3, 4, 4] получится [1, 2, 3, 4].
def remove_adjacent(nums):
    pass

print(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
print(remove_adjacent([2, 2, 3, 3, 3, 3]), [2, 3])
print(remove_adjacent([4, 5, 5, 4, 4]), [4, 5, 4])
print(remove_adjacent([]), [])
