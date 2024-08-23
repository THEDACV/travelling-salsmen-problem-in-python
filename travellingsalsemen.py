from itertools import permutations
from sys import maxsize

def travelling_salesman_problem(graph, s):
    vertex = []
    for i in range(len(graph)):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    permutation_count = 0
    for p in permutations(vertex):
        permutation_count += 1
        current_pathweight = 0
        k = s
        for i in p:
            current_pathweight += graph[k][i]
            k = i
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)

    print(f"Total number of permutations: {permutation_count}")
    return min_path

if __name__ == "__main__":
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]

    s = 0
    print(f"Minimum Cost: {travelling_salesman_problem(graph, s)}")