"""
first, find out all genes that are "1" step away. Do this by changing all
gene chars into A/G/C/T and checking if those exist in the gene bank. If yes,
append to the queue.
Use a steps variable to track the "Depth" where we are. Once we clear a loop
of children, then increment steps.
"""
from collections import deque
class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        def bfs():
            queue = deque([startGene])
            steps = 0
            visited = set()
            visited.add(startGene)
            while queue:
                length = len(queue)
                for i in range(length):
                    gene = queue.popleft()
                    if gene == endGene:
                        return steps
                    children = find_children(gene)
                    for c in children:
                        if c not in visited:
                            queue.append(c)
                            visited.add(c)
                steps += 1
            return -1
        def find_children(gene):
            children = []
            bases = ['A', 'C', 'G', 'T']
            for i in range(len(gene)):
                original_char = gene[i]
                for base in bases:
                    if base == original_char:
                        continue  
                    mutation = gene[:i] + base + gene[i+1:]
                    if mutation in bank:
                        children.append(mutation)
            return children
        return bfs()