"""Clean Code in Python - Chapter6: Getting more out of our objects with
descriptors

> Illustrate the basic workings of the descriptor protocol.
"""
class DescriptorClass:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance


class ClientClass:
    descriptor = DescriptorClass()
