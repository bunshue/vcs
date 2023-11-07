from turtle import Shape, Screen, Turtle, Vec2D as Vec
import turtle
import math
import sys

# 指定常數:
G = 8  # 設定萬有引力常數
NUM_LOOPS = 7000  # 執行迴圈的次數也就是 time step 模擬更新次數
Ro_X = -152.18  # CSM 的 x 座標
Ro_Y = 329.87  # CSM 的 y 座標
Vo_X = 423.10  # 地月轉移加速度對 x 軸的影響
Vo_Y = -512.26  # 地月轉移加速度對 y 軸的影響


MOON_MASS = 1_250_000

class GravSys():
    """對 n 個物體進行重力模擬"""
    def __init__(self):
        self.bodies = []
        self.t = 0
        self.dt = 0.001


    def sim_loop(self):
        """在每個時間進程中用迴圈處理 bodies list 中各物體"""
        for index in range(NUM_LOOPS):
            self.t += self.dt
            for body in self.bodies:
                body.step()

class Body(Turtle):
    """環繞及投射重力場的運動物體"""
    def __init__(self, mass, start_loc, vel, gravsys, shape):
        super().__init__(shape=shape)
        self.gravsys = gravsys
        self.penup()
        self.mass=mass
        self.setpos(start_loc)
        self.vel = vel
        gravsys.bodies.append(self)
        self.pendown()  # 取消註解會畫出移動軌跡
        
        
    def acc(self):
        """計算物體所受的合力，並傳回加速度向量"""
        a = Vec(0,0)
        for body in self.gravsys.bodies:
            if body != self:
                r = body.pos() - self.pos()
                a += (G * body.mass / abs(r)**3) * r
        return a
    

    def step(self):
        """計算物體的位置、方向和速度"""
        dt = self.gravsys.dt
        a = self.acc()
        self.vel = self.vel + dt * a
        xOld, yOld = self.pos()
        self.setpos(self.pos() + dt * self.vel)
        xNew, yNew = self.pos()
        if self.gravsys.bodies.index(self) == 1:
            dir_radians = math.atan2(yNew-yOld,xNew-xOld)
            dir_degrees = dir_radians * 180 / math.pi
            self.setheading(dir_degrees+90)
            

def main():
    # 設定視窗
    screen = Screen()
    screen.setup(width = 1.0, height = 1.0)  # 使用全螢幕
    screen.bgcolor('black')
    screen.title("Gravity Assist Example")

    # 建立重力系統物件
    gravsys = GravSys()
    
    # 建立月球
    image_moon = 'moon_27x27.gif'
    screen.register_shape(image_moon)
    moon = Body(MOON_MASS, (-250, 0), Vec(500, 0), gravsys, image_moon)
    moon.pencolor('gray')

    # 建立 CSM 的自訂圖案
    csm = Shape('compound')
    cm = ((0, 30), (0, -30), (30, 0))
    csm.addcomponent(cm, 'red', 'red')
    sm = ((-60,30), (0, 30), (0, -30), (-60, -30))
    csm.addcomponent(sm, 'red', 'black')
    nozzle = ((-55, 0), (-90, 20), (-90, -20))
    csm.addcomponent(nozzle, 'red', 'red')
    screen.register_shape('csm', csm)

    # 建立 CSM
    ship = Body(1, (Ro_X, Ro_Y), Vec(Vo_X, Vo_Y), gravsys, "csm")
    ship.shapesize(0.2)
    ship.color('red')
    ship.getscreen().tracer(1, 0)
    ship.setheading(90)

    # 開始進行模擬
    gravsys.sim_loop()

if __name__=='__main__':
    main()
