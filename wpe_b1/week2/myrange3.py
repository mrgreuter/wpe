class myrange3:

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

        cls.current_value = cls.start
        while cls.current_value < cls.end:
            yield cls.current_value
            cls.current_value += cls.step_size