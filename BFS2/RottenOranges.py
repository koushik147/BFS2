class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid) # setting row length
        n=len(grid[0]) # setting column length
        time=0
        freshcount=0
        q=deque() # creating queue
        dir = [[1,0],[0,1],[-1,0],[0,-1]] # declaring direction array
        for i in range(m): 
            for j in range(n):
                if grid[i][j] == 2: # if grid value is equal to 2 then append that value to queue
                    q.append((i,j))
                elif grid[i][j] == 1: # else if grid value is equal to 1 then increment the freshcount value by 1
                    freshcount+=1
        while q and freshcount!=0: # run until q is not none and freshcount not equal to 0
            time+=1
            size = len(q) # setting the size of q
            for i in range(size):  
                curr = q.popleft() # popping the queue and storing it to curr
                for r,c in dir: # for iterating in directions array
                    nr = r+curr[0] 
                    nc = c + curr[1]
                    if nr>=0 and nr<m and nc>=0 and nc<n: # boundary check
                        if grid[nr][nc] == 1: # if grid value is equal to 1
                            grid[nr][nc] = 2 # assign it to 2
                            freshcount-=1 # decrement freshcount by 1 
                            q.append((nr,nc)) # appending nr and nc to q
                            
        if freshcount == 0: # if freshcount is equal to 0
            return time # returning time
        else:
            return -1 # returning -1