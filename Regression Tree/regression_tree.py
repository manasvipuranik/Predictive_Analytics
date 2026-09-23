import numpy as np

X = np.array([
    [2,40], [3,45], [4,60],
    [5,65], [7,80], [7,70]
])

y = np.array([45,50,62,66,82,74])

best_error = float('inf')

for feature in range(2):
    for split in sorted(set(X[:,feature]))[:-1]:

        left = y[X[:,feature] <= split]
        right = y[X[:,feature] > split]

        error = (len(left)*np.var(left) +
                 len(right)*np.var(right)) / len(y)

        if error < best_error:
            best_error = error
            best_feature = feature
            best_split = split


print("Best Feature:", best_feature)
print("Best Split:", best_split)
print("Minimum Error:", round(best_error,2))

left = y[X[:,best_feature] <= best_split]
right = y[X[:,best_feature] > best_split]

print("Left Leaf Prediction:", np.mean(left))
print("Right Leaf Prediction:", np.mean(right))
