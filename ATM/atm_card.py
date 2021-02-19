class ATMCard:
    def __init__(self, defaultPin, defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance

    def getPinAwal(self):
        return self.defaultPin

    def getBalanceAwal(self):
        return self.defaultBalance