peoples = ("man"+str(i) for i in range(100))

class Peoples:
    def __init__(self, name, power=None):
        self.name = name
        self.power = power
        self.place = None
        self.winrate_avg = None
        self.FtPlayed = 0
        self.FirstFtDate = None
        self.LastFtDate = None

for i, p, in enumerate(peoples):
    p = Peoples(i, 101-i)



winrate_in_percent = people1.power - people2.power / 2 + 50
