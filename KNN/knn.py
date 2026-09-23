import math
data = [
    (2, 40, 45),   
    (3, 45, 50),   
    (4, 60, 62),   
    (5, 65, 68),   
    (7, 80, 82),   
]
new_student = (4.5, 63)

k = 3

distances = []
for x1, x2, y in data:
    distance = math.sqrt((x1 - new_student[0])**2 +(x2 - new_student[1])**2)
    distances.append((distance, y))

distances.sort()

nearest = distances[:k]

prediction = sum(y for distance, y in nearest) / k

print("Distances:")
for distance, y in distances:
    print(round(distance, 2), y)

print("\nNearest", k, "neighbours:")
for distance, y in nearest:
    print("Distance =", round(distance, 2), "Final Marks =", y)

print("\nPredicted Final Marks =", round(prediction, 2))
