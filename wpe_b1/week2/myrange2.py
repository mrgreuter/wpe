class myrange2:

    def __new__(cls, range, max_range=None, step_size=None):

        if max_range != None and max_range < range:
            raise ValueError
        elif max_range != 0:
            cls.start = range
            cls.end = max_range
        else:
            cls.start = 0
            cls.end = range
        
        if step_size != None:
            cls.step_size = step_size
        else:
            cls.step_size = 1

        cls.range_list = []
        current_val = cls.start
        while current_val < cls.end:
            cls.range_list.append(current_val)
            current_val += step_size
        return cls.range_list