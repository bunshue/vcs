from turtle import Shape, Screen, Turtle, Vec2D as Vec

# 指定常數:
G = 8  # 設定萬有引力常數
NUM_LOOPS = 4100  # 執行迴圈的次數也就是 time step 模擬更新次數
Ro_X = 0  # CSM 的 x 座標
Ro_Y = -85  # CSM 的 y 座標
Vo_X = 485  # 地月轉移加速度對 x 軸的影響
Vo_Y = 0  # 地月轉移加速度對 y 軸的影響


class GravSys():
    """對 n 個物體進行重力模擬"""
    def __init__(self):
        self.bodies = []
        self.t = 0
        self.dt = 0.001                
            
    def sim_loop(self):
        """在每個時間進程中用迴圈處理 bodies list 中各物體"""
        for _ in range(NUM_LOOPS):
            self.t += self.dt
            for body in self.bodies:
                body.step()
                

class Body(Turtle):
    """環繞及投射重力場的運動物體"""
    def __init__(self, mass, start_loc, vel, gravsys, shape):
        super().__init__(shape=shape)
        self.gravsys = gravsys
        self.penup()
        self.mass = mass
        self.setpos(start_loc)
        self.vel = vel
        gravsys.bodies.append(self)
        #self.resizemode("user")
        #self.pendown()  # 取消註解會畫出移動軌跡
        
    def acc(self):
        """計算物體所受的合力，並傳回加速度向量"""
        a = Vec(0, 0)
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
        self.setpos(self.pos() + dt * self.vel)
        if self.gravsys.bodies.index(self) == 2:  # 找出 CSM 物件，其索引值為 2
            rotate_factor = 0.0006
            self.setheading((self.heading() - rotate_factor * self.xcor()))
            if self.xcor() < -20:
                self.shape('arrow')
                self.shapesize(0.5)
                self.setheading(105)

def main():
    # 設定視窗
    screen = Screen()
    screen.setup(width=1.0, height=1.0)  # 使用全螢幕
    screen.bgcolor('black')
    screen.title("阿波羅 8 號自由返航軌跡模擬")

    # 建立重力系統物件
    gravsys = GravSys()

    # 建立地球
    image_earth = 'earth_100x100.gif'
    screen.register_shape(image_earth)
    earth = Body(1000000, (0, -25), Vec(0, -2.5), gravsys, image_earth)
    earth.pencolor('white')
    earth.getscreen().tracer(0, 0)  # 設定畫面更新

    # 建立月球
    image_moon = 'moon_27x27.gif'
    screen.register_shape(image_moon)
    moon = Body(32000, (344, 42), Vec(-27, 147), gravsys, image_moon)
    moon.pencolor('gray')

    # 建立 CSM 的自訂圖案
    csm = Shape('compound')
    cm = ((0, 30), (0, -30), (30, 0))
    csm.addcomponent(cm, 'white', 'white')
    sm = ((-60, 30), (0, 30), (0, -30), (-60, -30))
    csm.addcomponent(sm, 'white', 'black')    
    nozzle = ((-55, 0), (-90, 20), (-90, -20))
    csm.addcomponent(nozzle, 'white', 'white')
    screen.register_shape('csm', csm)

    # 建立 CSM
    ship = Body(1, (Ro_X, Ro_Y), Vec(Vo_X, Vo_Y), gravsys, 'csm')
    ship.shapesize(0.2)
    ship.color('white')
    ship.getscreen().tracer(1, 0)
    ship.setheading(90)

    # 開始進行模擬
    gravsys.sim_loop()

if __name__ == '__main__':
    main()
