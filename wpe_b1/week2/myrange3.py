class myrange3:

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
        
        cls.current_value = cls.start
        while cls.current_value < cls.end:
            yield cls.current_value
            cls.current_value += cls.step_size