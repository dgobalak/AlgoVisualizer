
class BubbleSort:
    def __init__(self, y: list) -> None:
        self.y = y
        self._sorted = False
        
    def sort(self) -> list:
        while not self._sorted:
            self._sorted = True
            for i in range(len(self.y) - 1):
                a, b = i, i+1
                if self.y[b] <= self.y[a]:
                    self.swap(a, b)
                    self._sorted = False
        return self.y

    def swap(self, a, b):
        self.y[a], self.y[b] = self.y[b], self.y[a]
        