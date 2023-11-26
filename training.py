from exercise import Exercise
class Training(Exercise):
    def __init__(self, type, set, count_per_set, break_time):
        super().__init__(type)
        self.set = set
        self.count_per_set = count_per_set
        self.break_time = break_time

    # def exercise(self):
    #     return