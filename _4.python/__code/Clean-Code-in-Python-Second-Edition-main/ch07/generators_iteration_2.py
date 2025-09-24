"""Clean Code in Python - Chapter 7: Generators, Iterators, and Asynchronous Programming

> The Interface for Iteration: sequences

"""

class SequenceWrapper:
    def __init__(self, original_sequence):
        self.seq = original_sequence

    def __getitem__(self, item):
        value = self.seq[item]
        return value

    def __len__(self):
        return len(self.seq)


class MappedRange:
    """Apply a transformation to a range of numbers."""

    def __init__(self, transformation, start, end):
        self._transformation = transformation
        self._wrapped = range(start, end)

    def __getitem__(self, index):
        value = self._wrapped.__getitem__(index)
        result = self._transformation(value)
        return result

    def __len__(self):
        return len(self._wrapped)
