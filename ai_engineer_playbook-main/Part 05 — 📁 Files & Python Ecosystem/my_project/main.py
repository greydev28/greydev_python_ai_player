import requests
import numpy as np
print("requests applied successfully!")

list2 = [20,30,40,40,70,80,90]
scores = np.array(list2)

print(f"total: {np.sum(scores)}")
print(f"mean: {np.mean(scores)}")
print(f"mode: {np.mod(scores,3)}")
print(f"mean : {np.mean(scores):.2f}")




