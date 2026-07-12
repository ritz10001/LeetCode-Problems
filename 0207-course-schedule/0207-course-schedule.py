from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        state = defaultdict(str)
        for k, v in prerequisites:
            graph[k].append(v)
        def dfs(curr):
            if state[curr] == "SEARCHING":
                return False
            if state[curr] == "SAFE":
                return True
            state[curr] = "SEARCHING"
            for prereq in graph[curr]:
                if not dfs(prereq):
                    return False
            state[curr] = "SAFE"
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        