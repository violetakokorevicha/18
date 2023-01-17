from typing import Union
import datetime as time
import csv


class Rekins:
    def init(self, client: str, dedication: str, size: list, material: float, price: Union[float, int]):
        self.creation_time = str(time.datetime.now())
        self.client = client
        self.dedication = dedication
        self.size = size
        self.material = material
        self.price = price

        # immutable constants
        self.pvn = 21
        self.__labour_pay = 15

        # method has to be booted on initialization
        self.total = self.aprekins()
        self.properties = {
            "time": self.creation_time,
            "client": self.client,
            "dedication": self.dedication,
            "size": self.size,
            "material": self.material,
            "price": self.price,
            "total": self.total,
        }

    def print(self) -> None:
        print(self.properties, sep="\n")

    def aprekins(self) -> Union[int, float]:
        pvn = (self.price + self.__labour_pay) * self.__pvn / 100
        return (self.price + self.__labour_pay) + pvn

    def save(self):
        with open('rekins.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow([val for val in self.properties.values()])
        return None


if __name == 'main':
    a = input("name: ")
    b = input("dedication:")
    c = []
    for i in range(1, 4):
        c.append(input(f"size{i} (int): "))
    d = float(input("material (float): "))
    e = float(input("price (float/int): "))

    instance = Rekins(a, b, c, d, e)
    instance.print()
    instance.save()