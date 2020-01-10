##### heap_sort_ID.py

class Solution(object):
    
    def heap_sort(self,nums): #heap_sort為控制台，將下面設好的funtion一一使用
        answer = [] #創一個空的list裝root
        self.heapify(nums)
        while len(nums) != 0: #list裡面還有東西就繼續跑while
            answer.append(nums.pop(0)) #把root用pop弄到answer=[]裡面
            self.heapify(nums) #剩下的tree可能不會是heap的狀態所以需要再heapify
        answer.reverse()
        return answer #把剛root pop 到answer=[]的結果return出來
    
    def getpar(self, ind:int): #找尋每個值的parent在哪
        if ind <= 0: #如果index=0或小於0表示該值沒有parent
            return
        return int((ind+1)/2-1) 
    
    
    def checkup(self, ind: int, arr: list): #比較parent與child
        
        par_ind = self.getpar(ind) #確認parent的index
        if par_ind is None:
            return
        
        self_val = arr[ind]
        par_val = arr[par_ind]
        
        if par_val < self_val: #swap 若parent小於child則換位子(因為是Maxheap)
            arr[ind] = par_val
            arr[par_ind] = self_val
            
        self.checkup(par_ind,arr)
        
    
    def heapify(self, arr:list): #將輸入的list變成heap(Maxheap)
        for i in reversed(range(len(arr))): #從大到小開始找
            self.checkup(i,arr) #尋找parent 需要時換位子
