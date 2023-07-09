class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0) -> None:
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self) -> str:
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        g = self.galleons + other.galleons
        s = self.sickles + other.sickles
        k = self.knuts + other.knuts
        return Vault(g, s, k)


potter = Vault(100, 50, 20)
print(potter)

weasley = Vault(20, 50, 100)
print(weasley)

total = potter + weasley + potter
print(total)
