# 4-5 定義抽象基礎類別 (強迫實作 method)

from abc import ABC, abstractmethod

class Base(ABC):
    
    @abstractmethod
    def foo(self):
        pass
    
    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):

    def foo(self):
        pass

    # 未實作 bar
    

c = Concrete()