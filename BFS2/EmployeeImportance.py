#TimeComplexity: O(n)
#SpaceComplexity: O(n)
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total = 0 # assign total to 0
        adj = {} # creating adjacency dict
        q=deque() # creating queue
        q.append(id) # appending id to queue
        
        for i in employees:
            adj[i.id] = [i.importance,i.subordinates] # assign importance and subordibnates to adj[id]
        
        while q:
            curr = q.popleft() # popping the queue and storing it in curr
            total += adj[curr][0] # adding the adj[curr][0] with total
            
            for subordinate in adj[curr][1]: # iterating through subordinates in adjacency[curr]
                q.append(subordinate) # appending subordinate to queue
        return total # returning total
