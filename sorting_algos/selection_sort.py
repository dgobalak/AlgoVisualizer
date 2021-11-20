
class SelectionSort:
    def __init__(self, y: list) -> None:
        self.y = y
    
    def sort(self) -> list:
        for i in range(len(self.y)):
            min_i, min_val = i, self.y[i]
            for j in range(i, len(self.y)):
                if self.y[j] <= min_val:
                    min_i, min_val = j, self.y[j]
            self.y[i], self.y[min_i] = self.y[min_i], self.y[i]
        return self.y
