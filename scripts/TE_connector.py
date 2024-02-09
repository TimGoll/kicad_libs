import math

initial_offset = 29.5
offset = 37.625
radius = 2.9
holes = 9

for i in range(0, holes):
    rot = (initial_offset + i * offset) / 360 * (2 * math.pi)

    print(str(i + 1) + ".")
    print("x: " + str(-1 * radius * math.sin(rot)))
    print("y: " + str(-1 * radius * math.cos(rot)))
    print("---------------")