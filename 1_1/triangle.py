def triangle_exist(side_a, side_b, side_c):
    result = True
    sides = [side_a, side_b, side_c]
    for side in sides:
        other_sides = sides.copy()
        other_sides.remove(side)
        if side > sum(other_sides):
            return False
    return result


a = b = c = 4

if triangle_exist(a, b, c):
    print("Треугольник существует")
    if a == b == c:
        print("Треугольник равносторонний")
    elif a == b or a == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Треугольник не существует")
