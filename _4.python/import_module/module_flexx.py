"""
要一次執行一個


"""

import sys
import time

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from flexx import flx


class Example(flx.Widget):
    # 内置CSS定义样式
    CSS = """
    .flx-Label {
        background: #9d9;
        width:300px;
        height:100px
    }
    """

    def init(self):
        flx.Label(text="hello world你好世界")


# 网页的标题名和样式定义，注意这个样式是指html或body的背景颜色定义
app = flx.App(Example, title="網頁標題", style="background:pink;")
# 导出或者保存为一张单html文件
# app.export('example.html', link=0)  # 匯出檔案
app.launch("browser")  # show it now in a browser
# flx.run()  # enter the mainloop
flx.start()  # 与run小区别就是退出循环，还可再启动

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 带CSS的转动的点组成的圆：

from time import time
from flexx import flx


class Circle(flx.Label):
    CSS = """
    body {
    /*body的背景颜色这种方法*/
    /*background-color: rgb(49, 107, 233);*/
    background-color:black;
        }
    .flx-Circle {
        /*圆点为red，注意可以直接如下，也可以使用：#f00为红色*/
        background: blue;
        /*background-color:black;*/
        border-radius: 10px;
        width: 10px;
        height: 10px;
    }
    """


class Circles(flx.Widget):
    def init(self):
        with flx.PinboardLayout():
            self._circles = [Circle() for i in range(32)]
        self.tick()

    def tick(self):
        global Math, window
        t = time()
        for i, circle in enumerate(self._circles):
            x = Math.sin(i * 0.2 + t) * 30 + 50
            y = Math.cos(i * 0.2 + t) * 30 + 50
            circle.apply_style(dict(left=x + "%", top=y + "%"))
        window.setTimeout(self.tick, 30)


# m = flx.App(Circles).launch('app')  #指定火狐浏览器，容易报错
m = flx.App(Circles).launch()  # 打开默认浏览器，谷歌浏览器
flx.run()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 6 带滑动条的sin绘图：

from flexx import flx


class SineExample(flx.Widget):
    def init(self):
        time = [i / 100 for i in range(100)]
        with flx.VBox():
            with flx.HBox():
                # 文本标签
                flx.Label(text="Frequency:")
                # 滑动条设置
                self.slider1 = flx.Slider(min=1, max=10, value=5, flex=1)
                flx.Label(text="Phase:")
                self.slider2 = flx.Slider(min=0, max=6, value=0, flex=1)
            # 绘图控件
            self.plot = flx.PlotWidget(
                flex=1,
                xdata=time,
                xlabel="time",
                ylabel="amplitude",
                title="a sinusoid",
            )

    @flx.reaction
    def __update_amplitude(self, *events):
        global Math
        freq, phase = self.slider1.value, self.slider2.value
        ydata = []
        for x in self.plot.xdata:
            ydata.append(Math.sin(freq * x * 2 * Math.PI + phase))
        self.plot.set_data(self.plot.xdata, ydata)


m = flx.launch(SineExample)
flx.run()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 7 主题表单：

from flexx import flx


class ThemedForm(flx.Widget):
    CSS = """
    .flx-Button {
        background: #9d9;
    }
    .flx-LineEdit {
        border: 2px solid #9d9;
    }
    """

    def init(self):
        with flx.HFix():
            with flx.FormLayout() as self.form:
                self.b1 = flx.LineEdit(title="Name:", text="Hola")
                self.b2 = flx.LineEdit(title="Age:", text="Hello world")
                self.b3 = flx.LineEdit(title="Favorite color:", text="Foo bar")
                flx.Button(text="Submit1")
                # flx.Widget(flex=1)  #有间隙空行

            with flx.FormLayout() as self.form:
                self.b4 = flx.LineEdit(title="Name:", text="Hola")
                self.b5 = flx.LineEdit(title="Age:", text="Hello world")
                self.b6 = flx.LineEdit(title="Favorite color:", text="Foo bar")
                flx.Button(text="Submit2")
                flx.Widget(flex=1)  # 没有间隙空行的


# m = flx.launch(ThemedForm, 'app')  #报错，这是默认火狐浏览器的
m = flx.launch(ThemedForm)  # 启动本机默认的谷歌浏览器
flx.run()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# NG
# 示例1：创建一个简单的按钮应用
from flexx import flx


class MyApp(flx.App):
    def init(self):
        with flx.VBox():
            self.button = flx.Button(text="Click me")
            self.label = flx.Label(text="Hello, Flexx!")

    @flx.reaction("button.pointer_click")
    def on_button_click(self, *events):
        self.label.set_text("Button clicked!")


app = MyApp()
app.launch()

# 在这个示例中，我们创建了一个简单的Flexx应用程序，包含一个按钮和一个标签。当用户点击按钮时，标签的文本会更新为#“Button clicked!”。

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# NG
# 示例2：创建一个实时更新的图表应用
import numpy as np
from flexx import flx


class ChartApp(flx.App):
    def init(self):
        self.plot = flx.PlotWidget()
        self.plot.set_style(flex=1)

        self.x = np.linspace(0, 10, 100)
        self.y = np.sin(self.x)

        self.plot.plot(self.x, self.y)

        self.timer = flx.Timer(callback=self.update_plot, interval=1000)

    def update_plot(self):
        self.y = np.sin(self.x + np.random.rand())
        self.plot.plot(self.x, self.y)


app = ChartApp()
app.launch()

# 在这个示例中，我们创建了一个实时更新的图表应用程序，每秒更新一次图表的数据。用户可以看到随着时间的推移，图表中的数据会不断变化。

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# NG
import flexx
from flexx import app, ui


class HelloWorld(ui.Widget):
    def init(self):
        with ui.VBox():
            self.label = ui.Label("Hello World")
            self.button = ui.Button(text="Click me")

    @app.connect("button.mouse_down")
    def _button_pressed(self, *events):
        self.label.text = "Button Clicked"


# 启动 Flexx 应用
app.serve(HelloWorld)
app.start()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# NG
import flexx
from flexx import app, ui


class ResponsiveLayout(ui.Widget):
    def init(self):
        with ui.HBox():
            with ui.VBox():
                self.button1 = ui.Button(text="Button 1")
                self.button2 = ui.Button(text="Button 2")
            self.label = ui.Label("Result: ")

    @app.connect("button1.mouse_down")
    def _button1_pressed(self, *events):
        self.label.text = "Result: Button 1 Pressed"

    @app.connect("button2.mouse_down")
    def _button2_pressed(self, *events):
        self.label.text = "Result: Button 2 Pressed"


# 启动 Flexx 应用
app.serve(ResponsiveLayout)
app.start()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
