from atm_card import ATMCard

class Customer:
    #kelas anak Customer

    def __init__(self, id, custPin = 1234, custBalance = 10000): #Konstruktor
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    #Getter
    def getID(self):
        return self.id

    def getCustPin(self):
        return self.custPin
        
    def getCustBalance(self):
        return self.custBalance

    #Debet (Mengambil Uang), mengurangi dari saldo
    def debet(self, nominal):
        self.custBalance -= nominal

    #Simpan, menambah dari saldo
    def simpan(self, nominal):
        self.custBalance += nominal