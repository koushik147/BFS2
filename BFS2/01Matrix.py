class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat) # storing row length
        n=len(mat[0]) # storing column length
        dir = [[0,1],[1,0],[0,-1],[-1,0]] # creating direction array
        q=deque() # creating queue
        
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0: # if matrix value equals to 0
                    q.append((i,j)) # append in queue
                else:
                    mat[i][j]=-1 # decrement by 1
        dist = 0 # assigning dist to 0
        while q:
            size = len(q)
            dist+=1 # incrementing dist by 1
            for _ in range(size):
                curr = q.popleft() # popping the queue and storing in curr
                for x,y in dir: # for in direction array
                    nr = x+curr[0]
                    nc = y+curr[1]
                    if nr>=0 and nr<m and nc>=0 and nc<n and mat[nr][nc]==-1: # boundary check
                        mat[nr][nc] = dist # assinging dist to matrix value
                        q.append((nr,nc)) # appending the value in queue
        return mat # returning matrix