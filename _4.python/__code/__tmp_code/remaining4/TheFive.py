import mcpi.minecraft as minecraft
import mcpi.block as block

matrix = [
    [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,7],
    [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]
    ]


player = 0

def Refresh():

    mc.setBlocks(0,0,0,29,15,29,block.AIR.id)
    
    for i in range(30):
        for j in range(30):
            mc.setBlock(i,0,j,block.WOOL.id,matrix[i][j])

def check(posX,posY):
    winFlag = 0
    "------------------------------------------------------------"
    if matrix[posX][posY] == matrix[posX-1][posY]:
        if matrix[posX][posY] == matrix[posX-2][posY]:
            if matrix[posX][posY] == matrix[posX-3][posY]:
                if matrix[posX][posY] == matrix[posX-4][posY]:
                    winFlag = 1
                else:
                    if matrix[posX][posY] == matrix[posX+1][posY]:
                        winFlag = 1
            else:
                if matrix[posX][posY] == matrix[posX+1][posY]:
                    if matrix[posX][posY] == matrix[posX+2][posY]:
                        winFlag = 1
        else:
            if matrix[posX][posY] == matrix[posX+1][posY]:
                if matrix[posX][posY] == matrix[posX+2][posY]:
                    if matrix[posX][posY] == matrix[posX+3][posY]:
                        winFlag = 1
    else:
        if matrix[posX][posY] == matrix[posX+1][posY]:
            if matrix[posX][posY] == matrix[posX+2][posY]:
                if matrix[posX][posY] == matrix[posX+3][posY]:
                    if matrix[posX][posY] == matrix[posX+4][posY]:
                        winFlag = 1

    "------------------------------------------------------------"
    if matrix[posX][posY] == matrix[posX][posY-1]:
        if matrix[posX][posY] == matrix[posX][posY-2]:
            if matrix[posX][posY] == matrix[posX][posY-3]:
                if matrix[posX][posY] == matrix[posX][posY-4]:
                    winFlag = 1
                else:
                    if matrix[posX][posY] == matrix[posX][posY+1]:
                        winFlag = 1
            else:
                if matrix[posX][posY] == matrix[posX][posY+1]:
                    if matrix[posX][posY] == matrix[posX][posY+2]:
                        winFlag = 1
        else:
            if matrix[posX][posY] == matrix[posX][posY+1]:
                if matrix[posX][posY] == matrix[posX][posY+2]:
                    if matrix[posX][posY] == matrix[posX][posY+3]:
                        winFlag = 1
    else:
        if matrix[posX][posY] == matrix[posX][posY+1]:
            if matrix[posX][posY] == matrix[posX][posY+2]:
                if matrix[posX][posY] == matrix[posX][posY+3]:
                    if matrix[posX][posY] == matrix[posX][posY+4]:
                        winFlag = 1

    "------------------------------------------------------------"
    if matrix[posX][posY] == matrix[posX-1][posY-1]:
        if matrix[posX][posY] == matrix[posX-2][posY-2]:
            if matrix[posX][posY] == matrix[posX-3][posY-3]:
                if matrix[posX][posY] == matrix[posX-4][posY-4]:
                    winFlag = 1
                else:
                    if matrix[posX][posY] == matrix[posX+1][posY+1]:
                        winFlag = 1
            else:
                if matrix[posX][posY] == matrix[posX+1][posY+1]:
                    if matrix[posX][posY] == matrix[posX+2][posY+2]:
                        winFlag = 1
        else:
            if matrix[posX][posY] == matrix[posX+1][posY+1]:
                if matrix[posX][posY] == matrix[posX+2][posY+2]:
                    if matrix[posX][posY] == matrix[posX+3][posY+3]:
                        winFlag = 1
    else:
        if matrix[posX][posY] == matrix[posX+1][posY+1]:
            if matrix[posX][posY] == matrix[posX+2][posY+2]:
                if matrix[posX][posY] == matrix[posX+3][posY+3]:
                    if matrix[posX][posY] == matrix[posX+4][posY+4]:
                        winFlag = 1
    "------------------------------------------------------------"
    if matrix[posX][posY] == matrix[posX-1][posY+1]:
        if matrix[posX][posY] == matrix[posX-2][posY+2]:
            if matrix[posX][posY] == matrix[posX-3][posY+3]:
                if matrix[posX][posY] == matrix[posX-4][posY+4]:
                    winFlag = 1
                else:
                    if matrix[posX][posY] == matrix[posX+1][posY-1]:
                        winFlag = 1
            else:
                if matrix[posX][posY] == matrix[posX+1][posY-1]:
                    if matrix[posX][posY] == matrix[posX+2][posY-2]:
                        winFlag = 1
        else:
            if matrix[posX][posY] == matrix[posX+1][posY-1]:
                if matrix[posX][posY] == matrix[posX+2][posY-2]:
                    if matrix[posX][posY] == matrix[posX+3][posY-3]:
                        winFlag = 1
    else:
        if matrix[posX][posY] == matrix[posX+1][posY-1]:
            if matrix[posX][posY] == matrix[posX+2][posY-2]:
                if matrix[posX][posY] == matrix[posX+3][posY-3]:
                    if matrix[posX][posY] == matrix[posX+4][posY-4]:
                        winFlag = 1
    "------------------------------------------------------------"
    return winFlag
    

mc = minecraft.Minecraft.create()

mc.postToChat("welcome to nille's world")

Refresh()

while True:
    
    events = mc.events.pollBlockHits()

    for e in events:
        if e.pos.x >= 1 and e.pos.x <= 28 and e.pos.y == 0 and e.pos.z >= 1 and e.pos.z <= 28:
            if player == 0 and matrix[e.pos.x][e.pos.z] == 4:
                mc.setBlock(e.pos.x,e.pos.y,e.pos.z,block.WOOL.id,15)
                matrix[e.pos.x][e.pos.z] = 15
                player = 1
                
            elif player == 1 and matrix[e.pos.x][e.pos.z] == 4:
                mc.setBlock(e.pos.x,e.pos.y,e.pos.z,block.WOOL.id,0)
                matrix[e.pos.x][e.pos.z] = 0
                player = 0

            elif player == 2:
                for i in range(1,29):
                    for j in range(1,29):
                        matrix[i][j] = 4
                Refresh()
                player = 0

            if check(e.pos.x,e.pos.z) and matrix[e.pos.x][e.pos.z] != 4:
                if player == 1:
                    mc.postToChat("BLACK WIN, HIT ANY BLOCK TO RESTART!!!")
                else:
                    mc.postToChat("WHITE WIN, HIT ANY BLOCK TO RESTART!!!")

                player = 2
        
        else:
            mc.postToChat("OUT OF RANGE")


    
        
        
    
