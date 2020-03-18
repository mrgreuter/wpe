class myrange2:

    def __init__(self, range, max_range=0, step_size=1):
        if max_range != 0 and max_range < range:
            raise ValueError
        self.range = range
        self.max_range = max_range
        self.step_size = step_size

    def __iter__(self):
        self.result = 0
        return self

    def __next__(self):
        if self.max_range > self.range:
            self.result = 
        if self.resul
        else:
            StopIteration