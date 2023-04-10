# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
#
# def sort_point(point):
#     return (point[0]**2 + point[1]**2)
#
# points = sorted(points, key=sort_point)
#
# print(points)

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

def name():
    def sort_name(athlet):
            return athlet[0]
    # return sorted(athletes, key=sort_name)

    athletes.sort(key=sort_name)
    return athletes
def old():
    def sort_old(old):
        return old[1]
    return sorted(athletes, key=sort_old)

def height():
    def sort_height(height):
        return height[2]
    return sorted(athletes, key=sort_height)

def weight():
    def sort_weight(weight):
        return weight[3]
    return sorted(athletes, key=sort_weight)

def_list = [None, name(), old(), height(), weight()]

[print(*el) for el in def_list[int(input())]]




