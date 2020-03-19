class myrange3:

    def __new__(cls, range, max_range=0, step_size=1):

        if max_range != 0 and max_range < range:
            raise ValueError
        elif max_range != 0:
            cls.start = range
            cls.end = max_range
        else:
            cls.start = 0
            cls.end = range

        cls.current_value = cls.start
        cls.step_size = step_size

        while cls.current_value < cls.end:
            yield cls.current_value
            cls.current_value += cls.step_size


for x in myrange3(5):
    print(x)