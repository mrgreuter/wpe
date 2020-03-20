class myrange3:

    def __new__(cls, range, max_range=None, step_size=None):

        if max_range != None and max_range < range:
            raise ValueError
        elif max_range != None:
            cls.start = range
            cls.end = max_range
        else:
            cls.start = 0
            cls.end = range

        cls.current_value = cls.start
        
        if step_size != None: 
            cls.step_size = step_size
        else:
            cls.step_size = 1

        while cls.current_value < cls.end:
            yield cls.current_value
            cls.current_value += cls.step_size


for x in myrange3(5):
    print(x)