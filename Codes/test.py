import scipy.spatial
import math
from collections import Counter

x = 0
y = 0
def build_vector(iterable1, iterable2):
	counter1 = Counter(iterable1)
	counter2 = Counter(iterable2)
	all_items = set(counter1.keys()).union(set(counter2.keys()))
	vector1 = [counter1[k] for k in all_items]
	vector2 = [counter2[k] for k in all_items]
	return vector1, vector2

# finding the cosine similarity between the topics
def cosim(v1, v2):
	dot_product = sum(n1 * n2 for n1, n2 in zip(v1, v2) )
	magnitude1 = math.sqrt(sum(n ** 2 for n in v1))
	magnitude2 = math.sqrt(sum(n ** 2 for n in v2))
	if((magnitude1 * magnitude2) != 0):
		return dot_product / (magnitude1 * magnitude2)
	else:
		return 0

file = open('News', 'r', encoding="UTF-8")
for lines in file:
        line = lines.split()
        x = x + 1
        nextFile = open('News', 'r', encoding="UTF-8")
        for lines2 in nextFile:
                line2 = lines2.split()
                y = y + 1
                v1, v2 = build_vector(line, line2)
                similarity = cosim(v1, v2)
                if similarity > 0.70:
                        f = open("DisimilarNews.txt","a+")
                        f.write(lines)
print(x)
print(y)
