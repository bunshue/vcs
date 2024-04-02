import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
mc.postToChat("welcome to nille's world")

def buildField():
    mc.setBlocks(-29,0,-19,29,15,19,block.AIR.id)
    
    mc.setBlocks(-29,0,-19,29,0,19,block.WOOL.id,0)
    mc.setBlocks(-28,0,-18,28,0,18,block.WOOL.id,13)
    mc.setBlocks(0,0,-19,0,0,19,block.WOOL.id,0)
    mc.setBlocks(-29,0,-8,-18,0,8,block.WOOL.id,0)
    mc.setBlocks(29,0,-8,18,0,8,block.WOOL.id,0)
    mc.setBlocks(-28,0,-7,-19,0,7,block.WOOL.id,13)
    mc.setBlocks(28,0,-7,19,0,7,block.WOOL.id,13)        

    mc.setBlocks(29,3,-5,29,3,5,block.WOOL.id,4)
    mc.setBlocks(-29,3,-5,-29,3,5,block.WOOL.id,11)

buildField()

