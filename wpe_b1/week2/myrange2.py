class myrange2:

    def __new__(cls, start, steps=None, step_size=None):

        if step_size != None:
            cls.step_size = step_size
        else:
            cls.step_size = 1

        if steps != None:
            cls.steps = steps
        else:
            cls.steps = start

        if steps == None:
            cls.start = 0
            cls.end = start
        else:
            cls.start = start
            cls.end = steps
        
        cls.range_list = []
        current_val = cls.start
        while current_val < cls.end:
            cls.range_list.append(current_val)
            current_val += cls.step_size
        return cls.range_list