# ch12_15
class Grandfather():
    """ 定義祖父的資產 """
    def __init__(self):
        self.grandfathermoney = 10000
    def get_info1(self):
        print("Grandfather's information")

class Father(Grandfather):      # 父類別是Grandfather
    """ 定義父親的資產 """
    def __init__(self):
        self.fathermoney = 8000
        super().__init__()
    def get_info2(self):
        print("Father's information")

class Ivan(Father):             # 父類別是Father
    """ 定義Ivan的資產 """
    def __init__(self):
        self.ivanmoney = 3000
        super().__init__()
    def get_info3(self):
        print("Ivan's information")
    def get_money(self):        # 取得資產明細
        print("\nIvan資產: ", self.ivanmoney,
              "\n父親資產: ", self.fathermoney,
              "\n祖父資產: ", self.grandfathermoney)

ivan = Ivan()
ivan.get_info3()                # 從Ivan中獲得
ivan.get_info2()                # 流程 Ivan -> Father
ivan.get_info1()                # 流程 Ivan -> Father -> Grandtather
ivan.get_money()                # 取得資產明細
