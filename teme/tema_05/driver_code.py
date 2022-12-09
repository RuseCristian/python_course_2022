class Fractie():

    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        # if self.numitor == self.numarator:
        #     return "1"
        # if self.numitor == 1:
        #     return self.numarator

        return f"{self.numarator}/{self.numitor}"

    def __add__(self, fractie2):
        if type(fractie2) != Fractie:
            raise Exception("Nu ati introdus o fractie")

        if self.numitor == fractie2.numitor:
            return Fractie(self.numarator + fractie2.numarator, self.numitor)

        numarator = self.numarator * fractie2.numitor + self.numitor * fractie2.numarator
        numitor = self.numitor * fractie2.numitor
        return Fractie(numarator, numitor)

    def __sub__(self, fractie2):
        if type(fractie2) != Fractie:
            raise Exception("Nu ati introdus o fractie")

        if self.numitor == fractie2.numitor:
            return Fractie(self.numarator - fractie2.numarator, self.numitor)

        numarator = self.numarator * fractie2.numitor - self.numitor * fractie2.numarator
        numitor = self.numitor * fractie2.numitor
        return Fractie(numarator, numitor)

    def inverse(self):
        return Fractie(self.numitor, self.numarator)


if __name__ == "__main__":

    # to string
    f1 = Fractie(2, 3)
    print(f1.__str__())

    # __str__
    f2 = f1 + Fractie(1, 3)
    print(f2.__str__())

    # __sub
    f3 = f2 - Fractie(2, 3)
    print(f3.__str__())

    # inverse
    f4 = f3.inverse()
    print(f4.__str__())
