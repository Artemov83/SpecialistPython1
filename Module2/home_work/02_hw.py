# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

# TODO: your code here
n = int(input("Кол-во коров "))
if n % 10 == 1:
    print("На лугу", n, "корова")
elif n % 10 > 1 and n % 10 < 5:
    print("На лугу", n, "коровы")
else:
    print("На лугу", n, "коров")
