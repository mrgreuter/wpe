class myrange2:

    def __new__(cls, start, max=None, step_size=None):

        if max != None:
            cls.max = max
            cls.start = start
            cls.end = max
        else:
            cls.max = start
            cls.start = 0
            cls.end = start

        if step_size != None:
            cls.step_size = step_size
        else:
            cls.step_size = 1
        
        cls.range_list = []
        cls.current_value = cls.start
        while cls.current_value < cls.end:
            cls.range_list.append(cls.current_value)
            cls.current_value += cls.step_size
        return cls.range_list