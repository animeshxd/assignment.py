# 6.wap to take two points and calculate distance between them.
import math
A, B = map(int, input("1st points: ").split())
D, E = map(int, input("2nd points: ").split())


D = math.sqrt((D - A) ** 2 + (E - B) ** 2)
print("distance is", D)