class myrange2:

    def __init__(self, range, max_range=0, step_size=1):
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
        self.result = self.start
        return self

    def __next__(self):
        if self.result < self.end:
            self.result += self.step_size
            return self.result
        else:
            StopIteration

a = myrange2(5)
my_iter = iter(a)

#my_iter2 = iter(myrange2(5, 10))
#my_iter3 = iter(myrange2(0, 42, 7))

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))