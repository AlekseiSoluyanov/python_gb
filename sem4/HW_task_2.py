# Напишите функцию принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) ->
# {True: "rev", "YES": 'acc', 4: "stroka"}

def hashable_dicts(**kwargs):
    pets = dict()
    for k, v in kwargs.items():
        if isinstance(v, (list, dict, set, bytearray)):
            v = str(v)
        pets[v] = k
    return pets


print(hashable_dicts(dog='Cooper', cat={'Barsik': 2, 'Murka': 3},
                     turtle=['bill', 'Cooper', 'Sharik'],
                     hamster={'edward', 'homa'}))
