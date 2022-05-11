from typing import List
from decimal import Decimal


class Box:

    def __init__(self, contents: List) -> None:
        self.contents = contents

    def return_price(self):
        total_price = 0
        for item in self.contents:
            total_price += item.return_price()

        return total_price


class Phone:

    def __init__(self, price: Decimal):
        self.price = price

    def return_price(self):
        return self.price


class Earphones:

    def __init__(self, price: Decimal):
        self.price = price

    def return_price(self):
        return self.price


class Charger:

    def __init__(self, price: Decimal):
        self.price = price

    def return_price(self):
        return self.price


def extractValues(box: Box) -> int:
        

        pack = box.contents.copy()
        index = 0
        while index < len(pack):

            current = pack[index]
            if isinstance(current, Box):
                for content in current.contents:
                    pack.append(content)
                pack = pack[:index] + pack[index+1:]

            else:
                index += 1

        return pack

def calculateTotalPrice(pack: List):
    
    total_price = 0
    for element in pack:
        total_price += element.return_price()

    return total_price


phone_case_contents = []
phone_case_contents.append(Phone(200))
phone_case_box = Box(phone_case_contents)

big_box_contents = []
big_box_contents.append(phone_case_box)
big_box_contents.append(Charger(10))
big_box_contents.append(Earphones(10))
big_box = Box(big_box_contents)

all_items = extractValues(big_box)

print("Total price: " + str(big_box.return_price()))

print(calculateTotalPrice(all_items))