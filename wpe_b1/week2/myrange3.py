class myrange3:

    def __init__(self, range, max_range=0, step_size=1):
        self.current_value = 0
        if max_range != 0 and max_range < range:
            raise ValueError
        elif max_range != 0:
            self.start = range
            self.end = max_range
        else:
            self.start = 0
            self.end = range
        
        self.step_size = step_size

    def __iter__(self):
        self.current_value = self.start
        return self

    def __next__(self):
        if self.current_value < self.end:
            self.current_value += self.step_size
            return self.current_value
        else:
            raise StopIteration

a = myrange3(4)
print(next(a))
print(next(a))