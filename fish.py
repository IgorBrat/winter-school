import datetime
from typing import List, Union
import os

class FishInfo:
    def __init__(self, name: str, price_in_uah_per_kilo: float, origin: str, catch_date: datetime, due_date: datetime) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.origin = origin
        self.catch_date = catch_date
        self.due_date = due_date

class Fish:
    def __init__(self, age_in_months: int, weight: float, fish_info: FishInfo) -> None:
        self.age_in_months = age_in_months
        self.weight = weight
        self.fish_info = fish_info

class FishBox:
    def __init__(self, fish_info: FishInfo, weight: float, package_date: datetime, height: float, width: float, length: float, is_alive: bool) -> None:
        self.fish_info = fish_info
        self.weight = weight
        self.package_date = package_date
        self.height = height
        self.width = width
        self.length = length
        self.is_alive = is_alive

class FishShop:
    frozen_fish_boxes = {}
    fresh_fishes = {}
    salmon_boxes = []
    korop_boxes = []
    okun_boxes = []
    salmons = []
    korops = []
    okuns = []
    def add_fish_box(self, fish_box: FishBox) -> None:
        if fish_box.fish_info.name=="salmon":
            self.salmon_boxes.append(fish_box)
            self.frozen_fish_boxes["salmon"] = self.salmon_boxes
        if fish_box.fish_info.name=="korop":
            self.korop_boxes.append(fish_box)
            self.frozen_fish_boxes["korop"] = self.korop_boxes
        if fish_box.fish_info.name=="okun":
            self.okun_boxes.append(fish_box)
            self.frozen_fish_boxes["okun"] = self.okun_boxes
    def add_fish(self, fish: Fish) -> None:
        if fish.fish_info.name=="salmon":
            self.salmons.append(fish)
            self.fresh_fishes["salmon"]=self.salmons
        if fish.fish_info.name=="korop":
            self.korops.append(fish)
            self.fresh_fishes["korop"]=self.korops
        if fish.fish_info.name=="okun":
            self.okuns.append(fish)
            self.fresh_fishes["okun"]=self.okuns
    def sell_fish(self, name: str, weight: float, is_fresh: bool) -> Union[str, float]:
        sold = 0
        if is_fresh == True:
            for it in self.fresh_fishes:
                if it==name:
                    for fish in self.fresh_fishes[it]:
                        if fish.weight >= weight:
                            sold += 1
                            fish.weight -= weight
                            return name, weight*fish.fish_info.price_in_uah_per_kilo
                            if fish.weight == 0:
                                self.fresh_fishes[it].delete(fish)
        if is_fresh == False:
            for it in self.frozen_fish_boxes:
                if it==name:
                    for fish_box in self.frozen_fish_boxes[it]:
                        if fish_box.weight >= weight:
                            sold += 1
                            fish_box.weight -= weight
                            return name, weight*fish_box.fish_info.price_in_uah_per_kilo
                            if fish_box.weight == 0:
                                self.frozen_fish_boxes[it].delete(fish_box)
        if sold==0:
            print("We don`t have that fish in proper amount.")
            return "", 0
    def get_fresh_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
        list = []
        for name in self.fresh_fishes:
            for fish in self.fresh_fishes[name]:
                price = fish.fish_info.price_in_uah_per_kilo
                break
            list.append((name, price))
        return sorted(list, key=lambda obj: obj[1])
    def get_frozen_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
        list = []
        for name in self.frozen_fish_boxes:
            for fish_box in self.frozen_fish_boxes[name]:
                price = fish_box.fish_info.price_in_uah_per_kilo
                break
            list.append((name, price))
        return sorted(list, key=lambda obj: obj[1])

fishery = FishShop()
clear = lambda: os.system('cls')
clear()
it = 0
while (it!=6):
    print("1 - Add frozen fish box\n2 - Add fresh fish\n3 - Sell fish\n4 - Get list of fresh fishes sorted by price\n5 - Get list of frozen fishes sorted by price\n6 - Exit\nChoose option:")
    it = int(input())
    clear()
    if it==1:
        name = str(input("Enter name of fish: "))
        price_in_uah_per_kilo = float(input("Enter price in uah per kilo: "))
        origin = str(input("Enter origin of fish: "))
        catch_date = datetime.date(2005, 12, 12)
        due_date = datetime.date(2006, 2, 1)
        info = FishInfo(name, price_in_uah_per_kilo, origin, catch_date, due_date)
        weight = float(input("Enter weight of box: "))
        package_date = datetime.date(2005, 12, 13)
        height = float(input("Enter height of box: "))
        width = float(input("Enter width of box: "))
        length = float(input("Enter length of box: "))
        is_alive = False
        box = FishBox(info, weight, package_date, height, width, length, is_alive)
        fishery.add_fish_box(box)
        clear()
    if it==2:
        name = str(input("Enter name of fish: "))
        price_in_uah_per_kilo = float(input("Enter price in uah per kilo: "))
        origin = str(input("Enter origin of fish: "))
        catch_date = datetime.date(2005, 12, 12)
        due_date = datetime.date(2006, 2, 1)
        info = FishInfo(name, price_in_uah_per_kilo, origin, catch_date, due_date)
        age_in_months = int(input("Enter age in months: "))
        weight = float(input("Enter weight: "))
        fish = Fish(age_in_months, weight, info)
        fishery.add_fish(fish)
        clear()
    if it==3:
        name = str(input("Enter name of fish: "))
        weight = float(input("Enter weight: "))
        is_fresh = bool(input("It has to be fresh? "))
        sold_fish = fishery.sell_fish(name, weight, is_fresh)
        print(sold_fish)
    if it==4:
        print(fishery.get_fresh_fish_names_sorted_by_price())
    if it==5:
        print(fishery.get_frozen_fish_names_sorted_by_price())
    if it==6:
        clear()
