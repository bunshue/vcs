"""

python_king07_traits

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
'''
#Traits & TraitsUI-輕松製作圖形界面
#Traits型態入門
#什麼是Traits屬性

from traits.api import HasTraits, Color #❶

class Circle(HasTraits): #❷
    color = Color #❸

c = Circle()

print(c.color)
print(c.color.getRgb())

c.color = "red"
print(c.color.getRgb())
c.color = 0x00ff00
print(c.color.getRgb())
c.color = (0, 255, 255)
print(c.color.getRgb())

from traits.api import TraitError
"""
try:
    c.color = 0.5
except TraitError as ex:
    print(ex[0][:350], "...")

cc = c.configure_traits()
print(cc)
"""

"""
    WARNING

    當使用wxPython作為背景界面庫時，由於TraitsUI 4.4.0中的一個錯誤，程式離開時會導致執行緒崩潰。
    請讀者將本書提供的scpy2\patches\toolkit.py複製到site-packages\traitsui\wx目錄下，覆蓋原有的toolkit.py檔案。

    TIP

    若果在Notebook中執行c.configure_traits()，它會立即傳回False，而不會等待交談視窗關閉。
    當程式單獨執行時configure_traits()會等待界面關閉，並根據使用者點擊的按鈕傳回True或False。
"""
cc = c.color.getRgb()
print(cc)

#Trait屬性的功能

from traits.api import Delegate, HasTraits, Instance, Int, Str

class Parent ( HasTraits ):
    # 起始化: last_name被起始化為'Zhang'
    last_name = Str( 'Zhang' ) #❶

class Child ( HasTraits ):          
    age = Int

    # 驗證: father屬性的值必須是Parent類別的案例
    father = Instance( Parent ) #❷

    # 代理： Child的案例的last_name屬性代理給其father屬性的last_name
    last_name = Delegate( 'father' ) #❸

    # 監聽: 當age屬性的值被修改時，下面的函數將被執行
    def _age_changed ( self, old, new ): #❹
        print('Age changed from %s to %s ' % ( old, new ))
        
p = Parent()
c = Child()

cc = p.last_name
print(cc)

#'Zhang'

c.father = p
print(c.last_name)
p.last_name = "ZHANG"
print(c.last_name)

c.age = 4

#Age changed from 0 to 4 

c.configure_traits();

c.print_traits()

"""
age:       4
father:    <__main__.Parent object at 0x05D9CC90>
last_name: 'ZHANG'
"""
c.get()

#{'age': 4, 'father': <__main__.Parent at 0x5d9cc90>, 'last_name': 'ZHANG'}

c.set(age = 6)

#Age changed from 4 to 6 
#<__main__.Child at 0x5d9c600>

c2 = Child(father=p, age=3)

#Age changed from 0 to 3 

c.trait("age")

#<traits.traits.CTrait at 0x9e23870>

p.trait("last_name").default

#'Zhang'

try:
    c.trait("father").validate(c, "father", 2)
except TraitError as ex:
    print(ex)

#The 'father' trait of a Child instance must be a Parent or None, but a value of 2 <type 'int'> was specified.

c.trait("father").validate(c, "father", p)

#<__main__.Parent at 0x5d9cc90>

c.trait_property_changed("age", 8, 10)
c.age # age屬性值沒有發生變化

#Age changed from 8 to 10 
#6

print(c.trait("age").trait_type)
print(c.trait("father").trait_type)

#Trait型態物件

from traits.api import Float, Int, HasTraits

class Person(HasTraits):
    age = Int(30)
    weight = Float

p1 = Person()
p2 = Person()
print(p1.trait("age") is p2.trait("age"))
print(p1.trait("weight").trait_type is p2.trait("weight").trait_type )

from traits.api import HasTraits, Range

coefficient = Range(-1.0, 1.0, 0.0)

class Quadratic(HasTraits):
    c2 = coefficient
    c1 = coefficient
    c0 = coefficient

class Quadratic2(HasTraits):
    c2 = Range(-1.0, 1.0, 0.0)
    c1 = Range(-1.0, 1.0, 0.0)
    c0 = Range(-1.0, 1.0, 0.0)

q = Quadratic()

print(coefficient is q.trait("c0").trait_type)
print(coefficient is q.trait("c1").trait_type)

q2 = Quadratic2()
q2.trait("c0").trait_type is q2.trait("c1").trait_type

#Trait的元資料

from traits.api import HasTraits, Int, Str, Array, List
   
class MetadataTest(HasTraits):
    i = Int(99, myinfo="test my info") #❶
    s = Str("test", label=u"字串")    #❷
    # NumPy的陣列
    a = Array         #❸
    # 元素為Int的清單
    list = List(Int)  #❹

test = MetadataTest()

cc = test.traits()
print(cc)

print(test.trait("i").default)
print(test.trait("i").myinfo)
print(test.trait("i").trait_type)

print(test.trait("s").label)

test.trait("a").array

print(test.trait("list"))
print(test.trait("list").trait_type)
print(test.trait("list").inner_traits) # list屬性的內定元素所對應的CTrait物件
print(test.trait("list").inner_traits[0].trait_type) # 內定元素所對應的Trait型態物件

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#Trait型態
#預先定義的Trait型態

from traits.api import HasTraits, CFloat, Float, TraitError

class Person(HasTraits):
    cweight = CFloat(50.0)
    weight = Float(50.0)

p = Person()
p.cweight = "90"
print(p.cweight)
try:
    p.weight = "90"
except TraitError as ex:
    print(ex)

#90.0
#The 'weight' trait of a Person instance must be a float, but a value of '90' <type 'str'> was specified.

from traits.api import Enum, List

class Items(HasTraits):
    count = Enum(None, 0, 1, 2, 3, "many")
    # 或是：
    # count = Enum([None, 0, 1, 2, 3, "many"])    

item = Items()
item.count = 2
item.count = "many"
try:
    item.count = 5
except TraitError as ex:
    print(ex)

#The 'count' trait of an Items instance must be None or 0 or 1 or 2 or 3 or 'many', but a value of 5 <type 'int'> was specified.

class Items(HasTraits):
    count_list = List([None, 0, 1, 2, 3, "many"])
    count = Enum(values="count_list")

item = Items()

try:
    item.count = 5    #由於候選值清單中沒有5，因此給予值失敗
except TraitError as ex:
    print(ex)
    
item.count_list.append(5)
item.count = 5       #由於候選值清單中有5，因此給予值成功
print(item.count)

#The 'count' trait of an Items instance must be None or 0 or 1 or 2 or 3 or 'many', but a value of 5 <type 'int'> was specified.

#5

#Property屬性

from traits.api import HasTraits, Float, Property, cached_property

class Rectangle(HasTraits):
    width = Float(1.0) 
    height = Float(2.0)

    #area是一個屬性，當width,height的值變化時，它對應的_get_area函數將被呼叫
    area = Property(depends_on=['width', 'height'])  #❶

    # 透過cached_property修飾器快取_get_area()的輸出
    @cached_property     #❷
    def _get_area(self): #❸
        "area的get函數，注意此函數名和對應的Proerty名的關系"
        print('recalculating')
        return self.width * self.height

r = Rectangle()
print(r.area)  # 第一次取得area，需要進行運算
r.width = 10
print(r.area) # 修改width之後，取得area，需要進行計算
print(r.area) # width和height都沒有發生變化，因此直接傳回快取值，沒有重新計算
"""
recalculating
2.0
recalculating
20.0
20.0
"""

r.edit_traits()
r.edit_traits();

t = r.trait("area") #獲得與area屬性對應的CTrait物件
t._notifiers(True) # _notifiers方法傳回所有的知會物件，當aera屬性改變時，這裡物件將被知會

#Trait屬性監聽

from traits.api import HasTraits, Str, Int

class Child ( HasTraits ):          
    name = Str
    age = Int 
    doing = Str

    def __str__(self):
        return "%s<%x>" % (self.name, id(self))

    # 當age屬性的值被修改時，下面的函數將被執行
    def _age_changed ( self, old, new ): #❶
        print("%s.age changed: form %s to %s" % (self, old, new))

    def _anytrait_changed(self, name, old, new): #❷
        print("anytrait changed: %s.%s from %s to %s" % (self, name, old, new))

def log_trait_changed(obj, name, old, new): #❸
    print("log: %s.%s changed from %s to %s" % (obj, name, old, new))
    
h = Child(name = "HaiYue", age=9)
k = Child(name = "KaiWen", age=2)
h.on_trait_change(log_trait_changed, name="doing") #❹

h.age = 10
h.doing = "sleeping"
k.doing = "playing"

from traits.api import HasTraits, Str, Int, Instance, List, on_trait_change

class HasName(HasTraits):
    name = Str()
    
    def __str__(self):
        return "<%s %s>" % (self.__class__.__name__, self.name)

class Inner(HasName):
    x = Int
    y = Int

class Demo(HasName):
    x = Int
    y = Int
    z = Int(monitor=1) # 有元資料屬性monitor的Int
    inner = Instance(Inner)
    alist = List(Int)
    test1 = Str()
    test2 = Str()
    
    def _inner_default(self):
        return Inner(name="inner1")
            
    @on_trait_change("x,y,inner.[x,y],test+,+monitor,alist[]")
    def event(self, obj, name, old, new):
        print(obj, name, old, new)

d = Demo(name="demo")
d.x = 10 # 與x比對
d.y = 20 # 與y比對
d.inner.x = 1 # 與inner.[x,y]比對
d.inner.y = 2 # 與inner.[x,y]比對
d.inner = Inner(name="inner2") # 與inner.[x,y]比對
d.test1 = "ok" #與 test+比對
d.test2 = "hello" #與test+比對
d.z = 30  # 與+monitor比對
d.alist = [3] # 與alist[]比對
d.alist.extend([4,5]) #與alist[]比對
d.alist[2] = 10 # 與alist[]比對

#Event和Button屬性

from traits.api import HasTraits, Float, Event, on_trait_change

class Point(HasTraits):       #❶
    x = Float(0.0)
    y = Float(0.0)
    updated = Event
            
    @on_trait_change( "x,y" )
    def pos_changed(self):    #❷
        self.updated = True

    def _updated_fired(self): #❸
        self.redraw()
    
    def redraw(self):         #❹
        print("redraw at %s, %s" % (self.x, self.y))

p = Point()
p.x = 1
p.y = 1
p.x = 1 # 由於x的值已經為1，因此不觸發事件
p.updated = True
p.updated = 0 # 給updated賦任何值都能觸發

#動態加入Trait屬性

a = HasTraits()  
a.add_trait("x", Float(3.0))
print(a.x)

#3.0

b = HasTraits()
b.add_trait("a", Instance(HasTraits))
b.a = a

from traits.api import Delegate
b.add_trait("y", Delegate("a", "x", modify=True))    
print(b.y)
b.y = 10    
print(a.x)

class A(HasTraits):
    pass

a = A()
a.x = 3
a.y = "string"
a.traits()

cc = a.trait("x").trait_type
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#TraitsUI入門
#預設界面

from traits.api import HasTraits, Str, Int

class Employee(HasTraits):
    name = Str
    department = Str
    salary = Int
    bonus = Int

Employee().configure_traits();

#用View定義界面
#外部檢視和內定檢視

from traits.api import HasTraits, Str, Int
from traitsui.api import View, Item #❶

class Employee(HasTraits):
    name = Str
    department = Str
    salary = Int
    bonus = Int
    
    view = View(  #❷
        Item('department', label=u"部門", tooltip=u"在哪個部門干活"), #❸
        Item('name', label=u"姓名"),
        Item('salary', label=u"薪水"),
        Item('bonus', label=u"獎金"),
        title=u"員薪水料", width=250, height=150, resizable=True   #❹
    )
    
p = Employee()
p.configure_traits();

from traits.api import HasTraits, Str, Int
from traitsui.api import View, Group, Item #❶

g1 = [Item('department', label=u"部門", tooltip=u"在哪個部門干活"), #❷
      Item('name', label=u"姓名")]
g2 = [Item('salary', label=u"薪水"),
      Item('bonus', label=u"獎金")]

class Employee(HasTraits):
    name = Str
    department = Str
    salary = Int
    bonus = Int

    traits_view = View( #❸
        Group(*g1, label = u'個人訊息', show_border = True),
        Group(*g2, label = u'收入', show_border = True),
        title = u"預設內定檢視")    

    another_view = View( #❹
        Group(*g1, label = u'個人訊息', show_border = True),
        Group(*g2, label = u'收入', show_border = True),
        title = u"另一個內定檢視")    
        
global_view = View( #❺
    Group(*g1, label = u'個人訊息', show_border = True),
    Group(*g2, label = u'收入', show_border = True),
    title = u"外部檢視")    
    
p = Employee()

# 使用內定檢視traits_view 
p.edit_traits() #❻;

cc = Employee.__view_traits__.content.keys()
print(cc)

#['another_view', 'traits_view']

# 使用內定檢視another_view 
p.edit_traits(view="another_view")

# 使用外部檢視view1
p.edit_traits(view=global_view)

"""
    TIP

    用TraitsUI庫建立的界面可以選取背景界面庫，目前支援的有qt4和wx兩種。在啟動程式時加入-toolkit qt4或是-toolkit wx選取使用何種界面庫產生界面。本書中全部使用Qt作為背景界面庫。
"""
#多模型檢視

from traits.api import HasTraits, Str, Int
from traitsui.api import View, Group, Item

class Employee(HasTraits):
    name = Str
    department = Str
    salary = Int
    bonus = Int

comp_view = View( #❶
    Group(
        Group(
            Item('p1.department', label=u"部門"),
            Item('p1.name', label=u"姓名"),
            Item('p1.salary', label=u"薪水"),
            Item('p1.bonus', label=u"獎金"),
            show_border=True
        ),
        Group(
            Item('p2.department', label=u"部門"),
            Item('p2.name', label=u"姓名"),
            Item('p2.salary', label=u"薪水"),
            Item('p2.bonus', label=u"獎金"),
            show_border=True
        ),
        orientation = 'horizontal'
    ),
    title = u"員工比較"    
)

employee1 = Employee(department = u"開發", name = u"張三", salary = 3000, bonus = 300) #❷
employee2 = Employee(department = u"銷售", name = u"李四", salary = 4000, bonus = 400)

HasTraits().configure_traits(view=comp_view, context={"p1":employee1, "p2":employee2}) #❸;

comp_view.ui({"p1":employee1, "p2":employee2});

#Group物件

from traits.api import HasTraits, Str, Int
from traitsui.api import View, Item, Group, VGrid, VGroup, HSplit, VSplit

class SimpleEmployee(HasTraits):
    first_name = Str
    last_name = Str
    department = Str

    employee_number = Str
    salary = Int
    bonus = Int
    
items1 = [Item(name = 'employee_number', label=u'編號'),
          Item(name = 'department', label=u"部門", tooltip=u"在哪個部門干活"),
          Item(name = 'last_name', label=u"姓"),
          Item(name = 'first_name', label=u"名")]

items2 = [Item(name = 'salary', label=u"薪水"),
          Item(name = 'bonus', label=u"獎金")]

view1 = View(
    Group(*items1, label = u'個人訊息', show_border = True),
    Group(*items2, label = u'收入', show_border = True),
    title = u"標簽頁模式",
    resizable = True    
)
    
view2 = View(
    VGroup(
        VGrid(*items1, label = u'個人訊息', show_border = True, scrollable = True),
        VGroup(*items2, label = u'收入', show_border = True),
    ), 
    resizable = True, width = 400, height = 250, title = u"垂直分群組"    
)

view3 = View(
    HSplit(
        VGroup(*items1, show_border = True, scrollable = True),
        VGroup(*items2, show_border = True, scrollable = True),
    ), 
    resizable = True, width = 400, height = 150, title = u"水平分群組(帶調節欄)"    
)

view4 = View(
    VSplit(
        VGroup(*items1, show_border = True, scrollable = True),
        VGroup(*items2, show_border = True, scrollable = True),
    ), 
    resizable = True, width = 200, height = 300, title = u"垂直分群組(帶調節欄)"    
)

sam = SimpleEmployee()
sam.configure_traits(view=view1)
sam.configure_traits(view=view2)
sam.configure_traits(view=view3)
sam.configure_traits(view=view4);

"""
    TIP

    Item也提供了visible_when和enabled_when屬性，其用法和Group完全相同。
"""

from traits.api import HasTraits, Int, Bool, Enum, Property
from traitsui.api import View, HGroup, VGroup, Item

class Shape(HasTraits):
    shape_type = Enum("rectangle", "circle")
    editable = Bool
    x, y, w, h, r = [Int]*5
    
    view = View(
        VGroup(
            HGroup(Item("shape_type"), Item("editable")),
            VGroup(Item("x"), Item("y"), Item("w"), Item("h"), 
                visible_when="shape_type=='rectangle'", enabled_when="editable"),
            VGroup(Item("x"), Item("y"), Item("r"), 
                visible_when="shape_type=='circle'",  enabled_when="editable"),
        ), resizable = True)
    
shape = Shape()
shape.configure_traits();

#組態檢視

from traitsui import menu
[btn.name for btn in menu.ModalButtons]

#[u'Apply', u'Revert', u'OK', u'Cancel', u'Help']

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#用Handler控制界面和模型
#用Handler處理事件

from traits.api import HasTraits, Str, Int
from traitsui.api import View, Item, Group, Handler
from traitsui.menu import ModalButtons

g1 = [Item('department', label=u"部門"),
      Item('name', label=u"姓名")]
g2 = [Item('salary', label=u"薪水"),
      Item('bonus', label=u"獎金")]

class Employee(HasTraits):
    name = Str
    department = Str
    salary = Int
    bonus = Int
    
    def _department_changed(self): #❶
        print(self, "department changed to ", self.department)
        
    def __str__(self): #❷
        return "<Employee at 0x%x>" % id(self)

view1 = View(
    Group(*g1, label = u'個人訊息', show_border = True),
    Group(*g2, label = u'收入', show_border = True),
    title = u"外部檢視",
    kind = "modal",   #❸
    buttons = ModalButtons
)

class EmployeeHandler(Handler): #❹
    def init(self, info):
        super(EmployeeHandler, self).init(info)
        print("init called")
        return True

    def init_info(self, info):
        super( EmployeeHandler, self).init_info(info)
        print("init info called")
        
    def position(self, info):
        super(EmployeeHandler, self).position(info)
        print("position called")
        
    def setattr(self, info, obj, name, value):
        super(EmployeeHandler, self).setattr(info, obj, name, value)
        print("setattr called:%s.%s=%s" % (obj, name, value))
        
    def apply(self, info):
        super(EmployeeHandler, self).apply(info)
        print("apply called")
        
    def close(self, info, is_ok):
        super(EmployeeHandler, self).close(info, is_ok)
        print("close called: %s" % is_ok)
        return True
        
    def closed(self, info, is_ok):
        super(EmployeeHandler, self).closed(info, is_ok)
        print("closed called: %s" % is_ok)
        
    def revert(self, info):
        super(EmployeeHandler, self).revert(info)
        print("revert called")
           
zhang = Employee(name="Zhang")
print("zhang is ", zhang)
zhang.configure_traits(view=view1, handler=EmployeeHandler()) #❺

#Controller和UIInfo物件

from traitsui.api import Controller

view1.kind = "nonmodal"
zhang = Employee(name="Zhang")
c = Controller(zhang)
c.edit_traits(view=view1);

cc = c.get()
print(cc)

cc = c.info.get()
print(cc)

cc = c.info.ui.get()
print(cc)

ui = c.info.ui
cc = ui.context
print(cc)

cc = ui.control # ui物件所表示的實際界面控制項
print(cc)

cc = ui.view
print(cc)

cc = ui._editors
print(cc)

#響應Trait屬性的事件

from traits.api import HasTraits, Bool
from traitsui.api import View, Handler

class MyHandler(Handler):
    def setattr(self, info, object, name, value): #❶
        Handler.setattr(self, info, object, name, value)
        info.object.updated = True #❷
        print("setattr", name)
        
    def object_updated_changed(self, info): #❸
        print("updated changed", "initialized=%s" % info.initialized)
        if info.initialized:
            info.ui.title += "*"

class TestClass(HasTraits):
    b1 = Bool
    b2 = Bool
    b3 = Bool
    updated = Bool(False)

view1 = View('b1', 'b2', 'b3',
             handler=MyHandler(),
             title = "Test",
             buttons = ['OK', 'Cancel'])

tc = TestClass()
tc.configure_traits(view=view1);

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from traits.api import *
from traitsui.api import *

#屬性編輯器

"""
    SOURCE

    traitsuidemo.demo：TraitsUI官方提供的示範程式

%exec_python -m traitsuidemo.demo
"""
#編輯器示範程式
"""
    SOURCE

    scpy2.traits.traitsui_editors：示範TraitsUI提供的各種編輯器的用法。
"""
#%exec_python -m scpy2.traits.traitsui_editors

#%%include python traits/traitsui_editors.py 1

class EditorDemoItem(HasTraits):
    code = Code()
    view = View(
        Group(
            Item("item", style="simple", label="simple", width=-300), #❶
            "_",  #❷
            Item("item", style="custom", label="custom"),
            "_",
            Item("item", style="text", label="text"),
            "_",
            Item("item", style="readonly", label="readonly"),
        ),
    )

#%%include python traits/traitsui_editors.py 2
class EditorDemo(HasTraits):
    codes = List(Str)
    selected_item = Instance(EditorDemoItem)  
    selected_code = Str 
    view = View(
        HSplit(
            Item("codes", style="custom", show_label=False,  #❶
                editor=ListStrEditor(editable=False, selected="selected_code")), 
            Item("selected_item", style="custom", show_label=False),
        ),
        resizable=True,
        width = 800,
        height = 400,
        title=u"各種編輯器示範"
    )

    def _selected_code_changed(self):
        item = EditorDemoItem(code=self.selected_code)
        item.add_trait("item", eval(self.selected_code)) #❷
        self.selected_item = item

#%%include python traits/traitsui_editors.py 3
employee = Employee()
demo_list = [u"低通", u"高通", u"帶通", u"帶阻"]

trait_defines ="""
    Array(dtype="int32", shape=(3,3)) #{1}
    Bool(True)
    Button("Click me")
    List(editor=CheckListEditor(values=demo_list))
    Code("print('hello world')")
    Color("red")
    RGBColor("red")
    Trait(*demo_list)
    Directory(os.getcwd())
    Enum(*demo_list)
    File()
    Font()
    HTML('<b><font color="red" size="40">hello world</font></b>')
    List(Str, demo_list)
    Range(1, 10, 5)
    List(editor=SetEditor(values=demo_list))
    List(demo_list, editor=ListStrEditor())
    Str("hello")
    Password("hello")
    Str("Hello", editor=TitleEditor())
    Tuple(Color("red"), Range(1,4), Str("hello"))
    Instance(EditorDemoItem, employee)    
    Instance(EditorDemoItem, employee, editor=ValueEditor())
    Instance(time, time(), editor=TimeEditor())
"""
demo = EditorDemo()
demo.codes = [s.split("#")[0].strip() for s in trait_defines.split("\n") if s.strip()!=""]
demo.configure_traits()

"""
#物件編輯器

    SOURCE

    scpy2.traits.traitsui_component：TraitsUI的元件示範程式。

%exec_python -m scpy2.traits.traitsui_component
"""

#%%include python traits/traitsui_component.py 1 -r
class Point(HasTraits):
    x = Int
    y = Int
    view = View(HGroup(Item("x"), Item("y")))

#%%include python traits/traitsui_component.py 2 -r
class Shape(HasTraits):
    info = Str #❶
    
    def __init__(self, **traits):
        super(Shape, self).__init__(**traits)
        self.set_info() #❷


class Triangle(Shape):
    a = Instance(Point, ()) #❸
    b = Instance(Point, ())
    c = Instance(Point, ())
    
    view = View(
        VGroup(
            Item("a", style="custom"), #❹
            Item("b", style="custom"),
            Item("c", style="custom"),
        )
    )
    
    @on_trait_change("a.[x,y],b.[x,y],c.[x,y]")
    def set_info(self):
        a,b,c = self.a, self.b, self.c
        l1 = ((a.x-b.x)**2+(a.y-b.y)**2)**0.5
        l2 = ((c.x-b.x)**2+(c.y-b.y)**2)**0.5
        l3 = ((a.x-c.x)**2+(a.y-c.y)**2)**0.5
        self.info = "edge length: %f, %f, %f" % (l1,l2,l3)
    
class Circle(Shape):
    center = Instance(Point, ())
    r = Int
    
    view = View(
        VGroup(
            Item("center", style="custom"), 
            Item("r"),
        )
    )
    
    @on_trait_change("r")
    def set_info(self):
        from math import pi
        self.info = "area:%f" % (pi*self.r**2)

Triangle().configure_traits()
Circle().configure_traits();

#%%include python traits/traitsui_component.py 3 -r
class ShapeSelector(HasTraits):
    select = Enum(*[cls.__name__ for cls in Shape.__subclasses__()]) #❶
    shape = Instance(Shape) #❷
    
    view = View(
        VGroup(
            Item("select"),
            Item("shape", style="custom"), #❸
            Item("object.shape.info", style="custom"), #❹
            show_labels = False
        ),
        width = 350, height = 300, resizable = True
    )
    
    def __init__(self, **traits):
        super(ShapeSelector, self).__init__(**traits)
        self._select_changed()
    
    def _select_changed(self):    #❺
        klass =  [c for c in Shape.__subclasses__() if c.__name__ == self.select][0]
        self.shape = klass()
"""
    SOURCE
    scpy2.traits.traitsui_component_multi_view：使用多個檢視顯示元件。
"""
#%exec_python -m scpy2.traits.traitsui_component_multi_view 

#%%include python traits/traitsui_component_multi_view.py 1
class Shape(HasTraits):
    info = Str
    view_info = View(Item("info", style="custom", show_label=False))

    def __init__(self, **traits):
        super(Shape, self).__init__(**traits)
        self.set_info()

#%%include python traits/traitsui_component_multi_view.py 2
    view = View(
        VGroup(
            Item("select", show_label=False),
            VSplit( #❶
                Item("shape", style="custom", editor=InstanceEditor(view="view")), #❷
                Item("shape", style="custom", editor=InstanceEditor(view="view_info")), 
                show_labels = False
            )

        ),
        width = 350, height = 300, resizable = True
    )

#自訂編輯器

#%%include python traits/mpl_figure_editor.py 1
import matplotlib
from traits.api import Bool
from traitsui.api import toolkit
from traitsui.basic_editor_factory import BasicEditorFactory
from traits.etsconfig.api import ETSConfig

if ETSConfig.toolkit == "wx":
    # matplotlib采用WXAgg為背景，這樣才能將繪圖控制項內嵌以wx為背景界面庫的traitsUI視窗中
    import wx
    matplotlib.use("WXAgg")
    from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
    from matplotlib.backends.backend_wx import NavigationToolbar2Wx as Toolbar
    from traitsui.wx.editor import Editor
    
elif ETSConfig.toolkit == "qt4":
    matplotlib.use("Qt4Agg")
    from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as Toolbar
    from traitsui.qt4.editor import Editor
    from pyface.qt import QtGui

#%%include python traits/mpl_figure_editor.py 3
class _QtFigureEditor(Editor):
    scrollable = True

    def init(self, parent): #❶
        self.control = self._create_canvas(parent)
        self.set_tooltip()

    def update_editor(self):
        pass

    def _create_canvas(self, parent):
        
        panel = QtGui.QWidget()
        
        def mousemoved(event):           
            if event.xdata is not None:
                x, y = event.xdata, event.ydata
                name = "Axes"
            else:
                x, y = event.x, event.y
                name = "Figure"
                
            panel.info.setText("%s: %g, %g" % (name, x, y))
            
        panel.mousemoved = mousemoved
        vbox = QtGui.QVBoxLayout()
        panel.setLayout(vbox)
        
        mpl_control = FigureCanvas(self.value) #❷
        vbox.addWidget(mpl_control)
        if hasattr(self.value, "canvas_events"):
            for event_name, callback in self.value.canvas_events:
                mpl_control.mpl_connect(event_name, callback)

        mpl_control.mpl_connect("motion_notify_event", mousemoved)  

        if self.factory.toolbar: #❸
            toolbar = Toolbar(mpl_control, panel)
            vbox.addWidget(toolbar)       

        panel.info = QtGui.QLabel(panel)
        vbox.addWidget(panel.info)
        return panel

#%%include python traits/mpl_figure_editor.py 4
class MPLFigureEditor(BasicEditorFactory):
    """
    相當於traits.ui中的EditorFactory，它傳回真正建立控制項的類別
    """    
    if ETSConfig.toolkit == "wx":
        klass = _WxFigureEditor
    elif ETSConfig.toolkit == "qt4":
        klass = _QtFigureEditor  #❶
        
    toolbar = Bool(True)  #❷

import numpy as np

from scpy2.traits import MPLFigureEditor


class SinWave(HasTraits):
    figure = Instance(Figure, ())
    view = View(
        Item("figure", editor=MPLFigureEditor(toolbar=True), show_label=False),
        width = 400,
        height = 300,
        resizable = True)

    def __init__(self, **kw):
        super(SinWave, self).__init__(**kw)
        self.figure.canvas_events = [
            ("button_press_event", self.figure_button_pressed)
        ]
        axes = self.figure.add_subplot(111)
        t = np.linspace(0, 2*np.pi, 200)
        axes.plot(np.sin(t))

    def figure_button_pressed(self, event):
        print(event.xdata, event.ydata)
        
model = SinWave()
model.edit_traits();

'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#函數曲線繪制工具
"""
    SOURCE

    scpy2.traits.traitsui_function_plotter：采用TraitsUI撰寫的函數曲線繪制工具。

%exec_python -m scpy2.traits.traitsui_function_plotter

    WARNING

    Code對應的編輯器程式碼存在BUG，請讀者將patches/pygments_highlighter.py複製到site-packages/pyface/ui/qt4/code_editor下覆蓋原有的檔案。
"""
""" NG
from traits.api import HasTraits, Color #❶
from traits.api import Delegate, HasTraits, Instance, Int, Str
from matplotlib.figure import Figure

#%%include python traits/traitsui_function_plotter.py 2
class FunctionPlotter(HasTraits):
    figure = Instance(Figure, ()) #❶
    code = Code()  #❷
    points = List(Instance(Point), [])  #❸
    draw_button = Button("Plot")

    view = View(
        VSplit(
            Item("figure", editor=MPLFigureEditor(toolbar=True), show_label=False), 
            HSplit(
                VGroup(
                    Item("code", style="custom"), 
                    HGroup(
                        Item("draw_button", show_label=False),
                    ),
                    show_labels=False
                ),
                Item("points", editor=point_table_editor, show_label=False) 
            )
        ),
        width=800, height=600, title="Function Plotter", resizable=True
    )

#%%include python traits/traitsui_function_plotter.py 1
class Point(HasTraits):
    x = Float()
    y = Float()

    point_table_editor = TableEditor(
        columns=[ObjectColumn(name='x', width=100, format="%g"),
                 ObjectColumn(name='y', width=100, format="%g")],
    editable=True,
    sortable=False,
    sort_model=False,
    auto_size=False,
    row_factory=Point)

#%%include python traits/traitsui_function_plotter.py 3
    def __init__(self, **kw):
        super(FunctionPlotter, self).__init__(**kw)
        self.figure.canvas_events = [ #❶
            ("button_press_event", self.memory_location),
            ("button_release_event", self.update_location)
        ]
        self.button_press_status = None #儲存滑鼠按鍵按下時的狀態
        self.lines = [] #儲存所有曲線
        self.functions = [] #儲存所有的曲線函數
        self.env = {} #程式碼的執行環境

        self.axe = self.figure.add_subplot(1, 1, 1)
        self.axe.callbacks.connect('xlim_changed', self.update_data) #❷
        self.axe.set_xlim(0, 1)
        self.axe.set_ylim(0, 1)
        self.points_line, = self.axe.plot([], [], "kx", ms=8, zorder=1000) #資料點

#%%include python traits/traitsui_function_plotter.py 4
    def memory_location(self, evt):
        if evt.button in (1, 3):
            self.button_press_status = time.clock(), evt.x, evt.y
        else:
            self.button_press_status = None

    def update_location(self, evt):
        if evt.button in (1, 3) and self.button_press_status is not None:
            last_clock, last_x, last_y = self.button_press_status
            if time.clock() - last_clock > 0.5: #❶
                return
            if ((evt.x - last_x) ** 2 + (evt.y - last_y) ** 2) ** 0.5 > 4: #❷
                return

        if evt.button == 1:
            if evt.xdata is not None and evt.ydata is not None:
                point = Point(x=evt.xdata, y=evt.ydata) #❸
                self.points.append(point)
        elif evt.button == 3:
            if self.points:
                self.points.pop() #❹

#%%include python traits/traitsui_function_plotter.py 5
    @on_trait_change("points[]")
    def _points_changed(self, obj, name, new):
        for point in new:
            point.on_trait_change(self.update_points, name="x, y") #❶
        self.update_points()

    def update_points(self): #❷
        arr = np.array([(point.x, point.y) for point in self.points])
        if arr.shape[0] > 0:
            self.points_line.set_data(arr[:, 0], arr[:, 1])
        else:
            self.points_line.set_data([], [])
        self.update_figure()

    def update_figure(self): #❸
        if self.figure.canvas is not None: #❹
            self.figure.canvas.draw_idle()

#%%include python traits/traitsui_function_plotter.py 6
    def update_data(self, axe):
        xmin, xmax = axe.get_xlim()
        x = np.linspace(xmin, xmax, 500)
        for line, func in zip(self.lines, self.functions):
            y = func(x)
            line.set_data(x, y)
        self.update_figure()

#%%include python traits/traitsui_function_plotter.py 7
    def _draw_button_fired(self):
        self.plot_lines()

    def plot_lines(self):
        xmin, xmax = self.axe.get_xlim() #❶
        x = np.linspace(xmin, xmax, 500)
        self.env = {"points": np.array([(point.x, point.y) for point in self.points])} #❷
        exec(self.code in self.env)

        results = []
        for line in self.lines:
            line.remove()
        self.axe.set_color_cycle(None) #重設彩色循環
        self.functions = []
        self.lines = []
        for name, value in self.env.items(): #❸
            if name.startswith("_"): #忽略以_開頭的名字
                continue
            if callable(value):
                try:
                    y = value(x)
                    if y.shape != x.shape: #輸出陣列應該與輸入陣列的形狀一致
                        raise ValueError("the return shape is not the same as x")
                except Exception as ex:
                    import traceback
                    print("failed when call function {}\n".format(name))
                    traceback.print_exc()
                    continue

                results.append((name, y))
                self.functions.append(value)

        for (name, y), function in zip(results, self.functions):
            #若果函數有plot_parameters屬性,則用其作為plot()的參數
            kw = getattr(function, "plot_parameters", {})  #❹
            label = kw.get("label", name)
            line, = self.axe.plot(x, y, label=label, **kw)
            self.lines.append(line)

        points = self.env.get("points", None) #❺
        if points is not None:
            self.points = [Point(x=x, y=y) for x, y in np.asarray(points).tolist()]

        self.axe.legend()
        self.update_figure()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
