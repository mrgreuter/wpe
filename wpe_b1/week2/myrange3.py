class myrange3:

    def __new__(cls, start, max=None, step_size=1):

        if max != None:
            cls.max = max
            cls.start = start
        else:
            cls.max = start
            cls.start = 0
        
        cls.end = cls.max
        cls.step_size = step_size

        cls.current_value = cls.start
        while cls.current_value < cls.end:
            yield cls.current_value
            cls.current_value += cls.step_size