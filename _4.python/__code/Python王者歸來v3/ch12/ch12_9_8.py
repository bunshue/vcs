# ch12_9_8.py
class Father():
    def hometown(self):
        print('我住在台北')

class Son(Father):
    pass

hung = Father()
ivan = Son()
hung.hometown()
ivan.hometown()




