class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: 

        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)
        
        visited, recursion_stack = set(), []
        def dfs(node):
            if node in recursion_stack: return False
            if node in visited: return True

            visited.add(node)
            recursion_stack.append(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            recursion_stack.pop()
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True



        # Adjcency list of course and preReqs
        # prereqMap = {course: [] for course in range(numCourses)}
        
        ## Detect Cycle in a Directed Graph

        ## Approach 1: BFS - Kahn's algorithm
        # indegree = [0] * numCourses
        # for course, preReq in prerequisites:
        #     prereqMap[preReq].append(course)
        #     indegree[course] += 1
        
        # course_completed = 0
        # q = deque()
        # for idx, count in enumerate(indegree):
        #     if count == 0:
        #         course_completed += 1
        #         q.append(idx)
        
        # while q:
        #     course = q.popleft()
            
        #     for preReq in prereqMap[course]:
        #         indegree[preReq] -= 1

        #         if indegree[preReq] == 0:
        #             course_completed += 1
        #             q.append(preReq)
        
        # return course_completed == numCourses

        # # stores courses in the current DFS path
        # self.visited = set()
        # self.in_recursion = [False] * numCourses

        # def cycle_detected(course):
        #     self.visited.add(course)
        #     self.in_recursion[course] = True

        #     for preReq in prereqMap[course]:
        #         if preReq in self.visited:
        #             if self.in_recursion[preReq]:
        #                 return True
        #         elif cycle_detected(preReq):
        #                 return True
                    

        #     self.in_recursion[course] = False
        #     return False


        # # # Approach 2: DFS with in_recursion stack
        # for course, preReq in prerequisites:
        #     prereqMap[preReq].append(course)

        # for course in range(numCourses):
        #     if cycle_detected(course):
        #         return False
        # return True







        # # Approach 3: DFS call return if it is possible to take a course or not
        # def dfs(course) -> bool:
        #     if course in visitSet:
        #         return False
        #     if not prereqMap[course]:
        #         return True
        #     visitSet.add(course)

        #     for preReq in prereqMap[course]:
        #         course_possible = dfs(preReq)
        #         if not course_possible:
        #             return False
        #     visitSet.remove(course)
        #     prereqMap[course] = []
        #     return True

        # for course in range(numCourses):
        #     course_possible = dfs(course)
        #     if not course_possible:
        #         return False
        # return True