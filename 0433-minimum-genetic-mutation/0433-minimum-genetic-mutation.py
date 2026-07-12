from collections import deque
class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        mutations = 0
        queue = deque([startGene])
        visited = set()

        def validMutations(currentGene):
            valid = []
            for mutation in bank:
                differ = 0
                for i in range(len(currentGene)):
                    if differ > 1:
                        break
                    if currentGene[i] != mutation[i]:
                        differ += 1
                if differ == 1 and mutation not in visited:
                    valid.append(mutation)
                    visited.add(mutation)
            return valid

        while queue:
            for i in range(len(queue)):
                currentGene = queue.popleft()
                if currentGene == endGene:
                    return mutations
                valid_mutations = validMutations(currentGene)
                queue.extend(valid_mutations)
            mutations += 1
        return -1


        



        

        