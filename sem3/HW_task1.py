# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [1, 2, 3, 1, 2]
result = []
for i in my_list:
    if my_list.count(i) > 1 and i not in result:
        result.append(i)

print(result)
