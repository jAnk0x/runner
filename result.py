class Result():
    def __init__(self, score, name):
        self.score = score
        self.name = name

    def __str__(self):
        return self.name + " " + str(self.score)

    def parse(string):
        l = string.split(" ")
        score = int(l[1])
        name = l[0]
        return Result(score, name)
