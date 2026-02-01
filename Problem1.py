class uf:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.size = [1]*n
    
    def _find(self, node):
        temp = node
        while self.roots[temp] != temp:
            temp = self.roots[temp]
        return temp

    def _union(self, f1, f2):
        root1 = self._find(f1)
        root2 = self._find(f2)

        if root1 == root2:
            return False
        elif self.size[root1]>self.size[root2]:
            self.roots[root2] = root1
            self.size[root1] += self.size[root2]
        else:
            self.roots[root1] = root2
            self.size[root2] += self.size[root1]
            
        return True


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        #adding edges from 0 (which is a well.)
        for house in range(1, n+1):
            pipes.append((0, house, wells[house-1]))
        
        pipes.sort(key=lambda x:x[2]) #sort based on cost
        n = n+1
        dsu = uf(n) #considering 0<->(meaning interchangeable)well
        
        res = 0
        count = 0 #count the edges ( exactly n-1 are needed to connect n nodes) 
        for pipe in pipes:
            if dsu._union(pipe[0], pipe[1]):
                res += pipe[2]
                count+=1
            if count==n-1:
                break
        
        return res
