# Треугольник существует только тогда, когда сумма любых двух его сторон больше
# третьей. Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является
# ли треугольник разносторонним, равнобедренным или равносторонним.

triangle_sides = []
for i in ['a', 'b', 'c']:
    triangle_sides.append(int(input(f'Введите длину стороны {i}: ')))

for i in range(3):
    if triangle_sides[i] > triangle_sides[i - 1] + triangle_sides[(i + 1) % 3]:
        print('Треугольника с такими сторонами не существует')
        break
else:
    if triangle_sides[0] == triangle_sides[1] == triangle_sides[2]:
        print('Треугольник равносторонний')
    elif triangle_sides[0] == triangle_sides[1] or \
            triangle_sides[1] == triangle_sides[2] or \
            triangle_sides[0] == triangle_sides[2]:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
