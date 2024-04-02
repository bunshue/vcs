# -*- coding: utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
import glob

mc = minecraft.Minecraft.create()

def menuM():
    print("-----------------")
    print("Minecraft图片扫描仪")
    print("1.扫描")
    print("2.复印")

    choice = int(raw_input("Please choose:  "))
    if choice < 1 or choice > 2:
        print("Sorry,the number is out range!")
    else:
        return choice

def menuS():
    print("")
    print("Minecraft图片扫描仪--扫描")
    print("1.选定左下角方块")
    print("2.选定右上角方块")
    print("3.开始扫描")
    print("4.返回主菜单")

    choice = int(raw_input("Please choose:  "))
    if choice < 1 or choice > 4:
        print("Sorry,the number is out range!")
    else:
        return choice

def menuP():
    print("")
    print("Minecraft图片扫描仪--复印")
    print("1.选择文件")
    print("2.选择左下角方块位置开始复印")
    print("3.返回主菜单")

    choice = int(raw_input("Please choose:  "))
    if choice < 1 or choice > 3:
        print("Sorry,the number is out range!")
    else:
        return choice

state = 0
posLB = (0,0,0)
posRT = (0,0,0)
FNAME = "default.nille"

while True:
    if state == 0:
        select = menuM()
        if select == 1:
            state = 1
        elif select == 2:
            state = 2

    elif state == 1:
        select = menuS()
        if select == 4:
            state = 0
        elif select == 1:
            state = 3
        elif select == 2:
            state = 4
        elif select == 3:
            state = 5

    elif state == 2:
        select = menuP()
        if select == 3:
            state = 0
        elif select == 1:
            state = 6
        elif select == 2:
            state = 7
            
    elif state == 3:
        print("请在游戏中选择一个方块...")
        while state == 3:
    
            events = mc.events.pollBlockHits()

            for e in events:
                posLB = e.pos
                print("左下角方块的坐标是")
                print(posLB)
                state = 1

    elif state == 4:
        print("请在游戏中选择一个方块...")
        while state == 4:
    
            events = mc.events.pollBlockHits()

            for e in events:
                posRT = e.pos
                print("右上角方块的坐标是")
                print(posRT)
                state = 1

    elif state == 5:
        if posLB == posRT:
            print("方块位置选择错误")
        else:
            if posLB.z == posRT.z:
                FNAME = raw_input("请输入保存的文件名:  ")
                                
                f = open(FNAME+".nille","w")
                if posLB.x < posRT.x:
                    rangeMin = posLB.x
                    rangeMax = posRT.x
                else:
                    rangeMax = posLB.x
                    rangeMin = posRT.x

                for y in range(posLB.y,posRT.y+1):
                    line = ""
                    for x in range(rangeMin,rangeMax+1):
                        blockInfo = mc.getBlockWithData(x,y,posRT.z)
                        print(blockInfo)
                        if blockInfo.id ==block.WOOL.id:
                            line = line + str(blockInfo.data)
                        else:
                            line = line + "20"
                        line = line + ","
                    f.write(line + "\n")
                    print(" ")
                f.close()
                print("扫描完成")
                print(" ")
            elif posLB.x == posRT.x:
                FNAME = raw_input("请输入保存的文件名:  ")
                                
                f = open(FNAME+".nille","w")
                if posLB.z < posRT.z:
                    rangeMin = posLB.z
                    rangeMax = posRT.z
                else:
                    rangeMax = posLB.z
                    rangeMin = posRT.z
                    
                for y in range(posLB.y,posRT.y+1):
                    line = ""
                    for z in range(rangeMin,rangeMax+1):
                        blockInfo = mc.getBlockWithData(posRT.x,y,z)
                        print(blockInfo)
                        if blockInfo.id ==block.WOOL.id:
                            line = line + str(blockInfo.data)
                        else:
                            line = line + "20"
                        line = line + ","
                    f.write(line + "\n")
                    print(" ")
                f.close()
                print("扫描完成")
                print(" ")
            else:
                
                print("方块位置选择错误")
                
        state = 0

    elif state == 6:
        print(" ")
        filesIndex = 1
        files = glob.glob("*.nille")
        for filename in files:
            print(str(filesIndex) + ".  "+filename)
            filesIndex = filesIndex + 1
        print("请选择要复印的图片文件：")

        choice = int(raw_input("Please choose:  "))
        if choice < 1 or choice > filesIndex-1:
            print("Sorry,the number is out range!")
        else:
            print("你选择的是：")
            FNAME = files[choice-1]
            print(FNAME)
        
        state = 2

    elif state == 7:
        while state == 7:
    
            events = mc.events.pollBlockHits()

            for e in events:
                baseX = e.pos.x
                baseY = e.pos.y+1
                baseZ = e.pos.z
                                
                f = open(FNAME,"r")
                offsetY = 0
                offsetX = 0
                for line in f.readlines():
                    data = line.split(",")
                    for cell in data:
                        if cell != "\n":
                            color = int(cell)
                            if color > 16:
                                mc.setBlock(baseX+offsetX,baseY+offsetY,baseZ,block.AIR.id)
                            else:
                                mc.setBlock(baseX+offsetX,baseY+offsetY,baseZ,block.WOOL.id,color)

                        offsetX = offsetX + 1

                    offsetY = offsetY + 1
                    offsetX = 0

                print("复印完成")
                print(" ")
                state = 0
