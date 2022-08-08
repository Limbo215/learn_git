# git commit -am " "
class House:
    def __init__(self):
        self.t = 20

    def konder(self, x=1):
        self.t -= x
        print(f"vi ohladili pomeschenie na {x} gradusov")

    def batareya(self, x=1):
        self.t += x
        print(f"vi nagreli pomeschenie na {x} gradusov")
