class myrange2:

    def __new__(cls, range, max_range=0, step_size=1):

        if max_range != 0 and max_range < range:
            raise ValueError
        elif max_range != 0:
            cls.start = range
            cls.end = max_range
        else:
            cls.start = 0
            cls.end = range
        
        cls.step_size = step_size

        cls.range_list = []
        current_val = cls.start
        while current_val < cls.end:
            cls.range_list.append(current_val)
            current_val += step_size
        return cls.range_list