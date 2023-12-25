#=============== Program Description ===============
#程式目的： 老鼠走迷宮

class Node:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.next=None

class TraceRecord:
    def __init__(self):
        self.first=None
        self.last=None
        
    def isEmpty(self):
        return self.first==None

    def insert(self,x,y):
        newNode=Node(x,y)
        if self.first==None:
            self.first=newNode
            self.last=newNode
        else:
            self.last.next=newNode
            self.last=newNode
        
    def delete(self):
        if self.first==None:
            print('[佇列已經空了]')
            return
        newNode=self.first
        while newNode.next!=self.last:
            newNode=newNode.next
        newNode.next=self.last.next
        self.last=newNode
        
ExitX= 8	#定義出口的X座標在第八列
ExitY= 10	#定義出口的Y座標在第十行
#宣告迷宮陣列
MAZE= [[1,1,1,1,1,1,1,1,1,1,1,1], \
       [1,0,0,0,1,1,1,1,1,1,1,1], \
       [1,1,1,0,1,1,0,0,0,0,1,1], \
       [1,1,1,0,1,1,0,1,1,0,1,1], \
       [1,1,1,0,0,0,0,1,1,0,1,1], \
       [1,1,1,0,1,1,0,1,1,0,1,1], \
       [1,1,1,0,1,1,0,1,1,0,1,1], \
       [1,1,1,1,1,1,0,1,1,0,1,1], \
       [1,1,0,0,0,0,0,0,1,0,0,1], \
       [1,1,1,1,1,1,1,1,1,1,1,1]]

def chkExit(x,y,ex,ey):
    if x==ex and y==ey:     
        if(MAZE[x-1][y]==1 or MAZE[x+1][y]==1 or MAZE[x][y-1] ==1 or MAZE[x][y+1]==2):
            return 1
        if(MAZE[x-1][y]==1 or MAZE[x+1][y]==1 or MAZE[x][y-1] ==2 or MAZE[x][y+1]==1):
            return 1
        if(MAZE[x-1][y]==1 or MAZE[x+1][y]==2 or MAZE[x][y-1] ==1 or MAZE[x][y+1]==1):
            return 1
        if(MAZE[x-1][y]==2 or MAZE[x+1][y]==1 or MAZE[x][y-1] ==1 or MAZE[x][y+1]==1):
            return 1
    return 0

#主程式


path=TraceRecord()
x=1	
y=1

print('[迷宮的路徑(0的部分)]')
for i in range(10):
    for j in range(12):
        print(MAZE[i][j],end='')
    print()
while x<=ExitX and y<=ExitY:
    MAZE[x][y]=2
    if MAZE[x-1][y]==0:
        x -= 1
        path.insert(x,y)
    elif MAZE[x+1][y]==0:
        x+=1
        path.insert(x,y)
    elif MAZE[x][y-1]==0:
        y-=1
        path.insert(x,y)
    elif MAZE[x][y+1]==0:
        y+=1
        path.insert(x,y)
    elif chkExit(x,y,ExitX,ExitY)==1:
        break
    else:
        MAZE[x][y]=2
        path.delete()
        x=path.last.x
        y=path.last.y
print('[老鼠走過的路徑(2的部分)]')
for i in range(10):
    for j in range(12):
        print(MAZE[i][j],end='')
    print()
